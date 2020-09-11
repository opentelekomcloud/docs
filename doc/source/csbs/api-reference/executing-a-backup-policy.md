# Executing a Backup Policy<a name="EN-US_TOPIC_0059304230"></a>

## Function<a name="section27745186"></a>

This API is used to manually execute a backup policy and create a backup task.

## URI<a name="section48380088"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/providers/\{provider\_id\}/checkpoints

-   Parameter description

    **Table  1**  Parameter description

    <a name="table7530457"></a>
    <table><thead align="left"><tr id="row11630735"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23446209"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20094757"><a name="p20094757"></a><a name="p20094757"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p17062614"><a name="p17062614"></a><a name="p17062614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p39894459"><a name="p39894459"></a><a name="p39894459"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row24922659"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5469531"><a name="p5469531"></a><a name="p5469531"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p40378851"><a name="p40378851"></a><a name="p40378851"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p49461475"><a name="p49461475"></a><a name="p49461475"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46956548"><a name="p46956548"></a><a name="p46956548"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b6168145214140"><a name="b6168145214140"></a><a name="b6168145214140"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section32767614"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table52229063"></a>
    <table><thead align="left"><tr id="row65530572"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p625933685013"><a name="p625933685013"></a><a name="p625933685013"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p182592363502"><a name="p182592363502"></a><a name="p182592363502"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p18274736115011"><a name="p18274736115011"></a><a name="p18274736115011"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p16274336125014"><a name="p16274336125014"></a><a name="p16274336125014"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5129585"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12843259"><a name="p12843259"></a><a name="p12843259"></a>checkpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p33671049"><a name="p33671049"></a><a name="p33671049"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p43000452"><a name="p43000452"></a><a name="p43000452"></a>checkpoint_req</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p60484563"><a name="p60484563"></a><a name="p60484563"></a>For details, see the <strong id="b1527619422077"><a name="b1527619422077"></a><a name="b1527619422077"></a>checkpoint_req</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **checkpoint\_req**

    **Table  3**  Parameter description of field  **checkpoint\_req**

    <a name="table302559"></a>
    <table><thead align="left"><tr id="row61892580"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1174315396503"><a name="p1174315396503"></a><a name="p1174315396503"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p197431839185015"><a name="p197431839185015"></a><a name="p197431839185015"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p174313914502"><a name="p174313914502"></a><a name="p174313914502"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p1874318391501"><a name="p1874318391501"></a><a name="p1874318391501"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62362224"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p18175365"><a name="p18175365"></a><a name="p18175365"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p62918475"><a name="p62918475"></a><a name="p62918475"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p63231721"><a name="p63231721"></a><a name="p63231721"></a>checkpoint_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p21495816"><a name="p21495816"></a><a name="p21495816"></a>Backup parameters</p>
    </td>
    </tr>
    <tr id="row59244624"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34085202"><a name="p34085202"></a><a name="p34085202"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9437993"><a name="p9437993"></a><a name="p9437993"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p26279997"><a name="p26279997"></a><a name="p26279997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p48305013"><a name="p48305013"></a><a name="p48305013"></a>Backup policy ID. Refer to the backup policy ID that is returned by the API of <a href="querying-the-backup-policy-list.md">Querying the Backup Policy List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** checkpoint\_param **

    **Table  4**  Parameter description of field** checkpoint\_param **

    <a name="table20391994"></a>
    <table><thead align="left"><tr id="row65655933"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p337684013505"><a name="p337684013505"></a><a name="p337684013505"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p33764400504"><a name="p33764400504"></a><a name="p33764400504"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p9376164085017"><a name="p9376164085017"></a><a name="p9376164085017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p43921840205018"><a name="p43921840205018"></a><a name="p43921840205018"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24015598"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66215252"><a name="p66215252"></a><a name="p66215252"></a>auto_trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p61835195"><a name="p61835195"></a><a name="p61835195"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p42594890"><a name="p42594890"></a><a name="p42594890"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p27634090"><a name="p27634090"></a><a name="p27634090"></a>Whether automatic trigger is enabled</p>
    </td>
    </tr>
    <tr id="row47380224"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12592924"><a name="p12592924"></a><a name="p12592924"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p13393884"><a name="p13393884"></a><a name="p13393884"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p11162792"><a name="p11162792"></a><a name="p11162792"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31770985"><a name="p31770985"></a><a name="p31770985"></a>ID list of resources to be backed up</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/providers/{provider_id}/checkpoints
    {
      "checkpoint" : {
        "plan_id" : "62171999-3df1-42f7-9513-6f9b1bea4744",
        "parameters" : {
          "auto_trigger" : false,
          "resources" : [ "7a32a8b5-7977-4e24-b5da-e0eb457db75b", "b2b433bf-7dd6-4a74-aa8f-85673dfbda48" ]
        }
      }
    }
    ```


## Response<a name="section26473078"></a>

-   Parameter description

    **Table  5**  Parameter description

    <a name="table52875024"></a>
    <table><thead align="left"><tr id="row50783343"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p86411943195020"><a name="p86411943195020"></a><a name="p86411943195020"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1065774315012"><a name="p1065774315012"></a><a name="p1065774315012"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p86577430503"><a name="p86577430503"></a><a name="p86577430503"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20239584"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p28793606"><a name="p28793606"></a><a name="p28793606"></a>checkpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3397638"><a name="p3397638"></a><a name="p3397638"></a>checkpoint_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6773298"><a name="p6773298"></a><a name="p6773298"></a>See the <strong id="b5945142883710"><a name="b5945142883710"></a><a name="b5945142883710"></a>checkpoint_resp</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **checkpoint\_resp**

    **Table  6**  Parameter description of field  **checkpoint\_resp**

    <a name="table11766233"></a>
    <table><thead align="left"><tr id="row37931945"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p550144617506"><a name="p550144617506"></a><a name="p550144617506"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1851744615019"><a name="p1851744615019"></a><a name="p1851744615019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p3517946165011"><a name="p3517946165011"></a><a name="p3517946165011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56022305"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41512818"><a name="p41512818"></a><a name="p41512818"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p37831566"><a name="p37831566"></a><a name="p37831566"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p44458025"><a name="p44458025"></a><a name="p44458025"></a>Status. The value can be protecting, deleting, available, or error.</p>
    </td>
    </tr>
    <tr id="row64577910"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63428245"><a name="p63428245"></a><a name="p63428245"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10652664"><a name="p10652664"></a><a name="p10652664"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57559436"><a name="p57559436"></a><a name="p57559436"></a>Creation time, for example, 2016-12-06T21:20:29.898823</p>
    </td>
    </tr>
    <tr id="row48272879"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17789141"><a name="p17789141"></a><a name="p17789141"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12243410"><a name="p12243410"></a><a name="p12243410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52192186"><a name="p52192186"></a><a name="p52192186"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row67076492"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64486787"><a name="p64486787"></a><a name="p64486787"></a>resource_graph</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p43536399"><a name="p43536399"></a><a name="p43536399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36787444"><a name="p36787444"></a><a name="p36787444"></a>Resource diagram, which displays the mapping relationship between resources and backups. If the value is null, the backup contains only the resource backup of the entire system.</p>
    </td>
    </tr>
    <tr id="row62651542"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41610169"><a name="p41610169"></a><a name="p41610169"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5461607"><a name="p5461607"></a><a name="p5461607"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16134202512151"><a name="p16134202512151"></a><a name="p16134202512151"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row22088927"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p44372630"><a name="p44372630"></a><a name="p44372630"></a>protection_plan</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10578331"><a name="p10578331"></a><a name="p10578331"></a>plan_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51538488"><a name="p51538488"></a><a name="p51538488"></a>Backup policy information</p>
    </td>
    </tr>
    <tr id="row1551632045"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1953573548"><a name="p1953573548"></a><a name="p1953573548"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1253893146"><a name="p1253893146"></a><a name="p1253893146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p195447318418"><a name="p195447318418"></a><a name="p195447318418"></a>Additional information about the backup object, such as the backup creation mode</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **plan\_resp**

    **Table  7**  Parameter description of field  **plan\_resp**

    <a name="table13868018"></a>
    <table><thead align="left"><tr id="row35028525"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p14861154825011"><a name="p14861154825011"></a><a name="p14861154825011"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1386124816506"><a name="p1386124816506"></a><a name="p1386124816506"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p486111482500"><a name="p486111482500"></a><a name="p486111482500"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24335246"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24997922"><a name="p24997922"></a><a name="p24997922"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64411810"><a name="p64411810"></a><a name="p64411810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49974111"><a name="p49974111"></a><a name="p49974111"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row47113817"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p58122826"><a name="p58122826"></a><a name="p58122826"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31296560"><a name="p31296560"></a><a name="p31296560"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51993463"><a name="p51993463"></a><a name="p51993463"></a>Backup policy name</p>
    </td>
    </tr>
    <tr id="row65287983"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53835255"><a name="p53835255"></a><a name="p53835255"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19158168"><a name="p19158168"></a><a name="p19158168"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8307777"><a name="p8307777"></a><a name="p8307777"></a>Backup object list</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  8**  Parameter description of field  **resource**

    <a name="table1841371"></a>
    <table><thead align="left"><tr id="row58395968"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p54231752165020"><a name="p54231752165020"></a><a name="p54231752165020"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p14381652145018"><a name="p14381652145018"></a><a name="p14381652145018"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p043817522505"><a name="p043817522505"></a><a name="p043817522505"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56034597"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42508527"><a name="p42508527"></a><a name="p42508527"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61118200"><a name="p61118200"></a><a name="p61118200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p51627143"><a name="p51627143"></a><a name="p51627143"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row1050513353349"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10242210163618"><a name="p10242210163618"></a><a name="p10242210163618"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p182422103364"><a name="p182422103364"></a><a name="p182422103364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p98113652114"><a name="p98113652114"></a><a name="p98113652114"></a>Entity object type of backup objects</p>
    <p id="p424214104366"><a name="p424214104366"></a><a name="p424214104366"></a>The value is fixed at <strong id="b195203197301"><a name="b195203197301"></a><a name="b195203197301"></a>OS::Nova::Server</strong>, indicating that the object type is ECSs.</p>
    </td>
    </tr>
    <tr id="row9527550"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33534096"><a name="p33534096"></a><a name="p33534096"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34352802"><a name="p34352802"></a><a name="p34352802"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31113586"><a name="p31113586"></a><a name="p31113586"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row9502115994217"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p777318533616"><a name="p777318533616"></a><a name="p777318533616"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10773185103617"><a name="p10773185103617"></a><a name="p10773185103617"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1677325193612"><a name="p1677325193612"></a><a name="p1677325193612"></a>Additional information of the resource</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "checkpoint" : {
        "status" : "protecting",
        "created_at" : "2016-12-06T21:20:29.898823",
        "id" : "14626f11-b54a-44ea-8e69-7463e527506a",
        "resource_graph" : null,
        "project_id" : "b942cc8342734d15bcb246babb1953cf",
        "protection_plan" : {
          "id" : "6a6cda7e-7b89-4b14-8e5c-3b6821a97d2c",
          "resources" : [ {
            "type" : "OS::Nova::Server",
            "id" : "1c960fe4-e679-421a-97cd-4f7463d2344b",
            "name" : "server0",
            "extra_info": "{}"
          } ],
          "name" : "backup"
        },
        "extra_info": "{"created_by": "manual"}"
      }
    }
    ```


## Status Codes<a name="section36931111"></a>

-   Normal

    <a name="table34230627"></a>
    <table><thead align="left"><tr id="row32432861"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p9816121"><a name="p9816121"></a><a name="p9816121"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p56908304"><a name="p56908304"></a><a name="p56908304"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46169932"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p48777045"><a name="p48777045"></a><a name="p48777045"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58626578"><a name="p58626578"></a><a name="p58626578"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table51132396"></a>
    <table><thead align="left"><tr id="row21973438"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p35018071"><a name="p35018071"></a><a name="p35018071"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p17891472"><a name="p17891472"></a><a name="p17891472"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39923089"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12544771"><a name="p12544771"></a><a name="p12544771"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p9493517"><a name="p9493517"></a><a name="p9493517"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row18332795"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8561437"><a name="p8561437"></a><a name="p8561437"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p22387820"><a name="p22387820"></a><a name="p22387820"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row163791"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13267148"><a name="p13267148"></a><a name="p13267148"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p897193"><a name="p897193"></a><a name="p897193"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row8074739"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p50074116"><a name="p50074116"></a><a name="p50074116"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p29471561"><a name="p29471561"></a><a name="p29471561"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row63917458"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p9931649"><a name="p9931649"></a><a name="p9931649"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p66266137"><a name="p66266137"></a><a name="p66266137"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row59524323"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p56740874"><a name="p56740874"></a><a name="p56740874"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p32608110"><a name="p32608110"></a><a name="p32608110"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

