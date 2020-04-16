# Creating a Manual Backup<a name="en-us_topic_0037139097"></a>

## Function<a name="section4850156117316"></a>

This API is used to create a manual backup.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/backups

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.63%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.260000000000005%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p40188499163133"><a name="p40188499163133"></a><a name="p40188499163133"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b1157666055"><a name="b1157666055"></a><a name="b1157666055"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.7%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b164557708"><a name="b164557708"></a><a name="b164557708"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b1227660779"><a name="b1227660779"></a><a name="b1227660779"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.7%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>Dictionary data structure. For details, see <a href="#table35260043174853">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p49586916144357"><a name="p49586916144357"></a><a name="p49586916144357"></a>Specifies the manual backup object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  backup field data structure description

    <a name="table35260043174853"></a>
    <table><thead align="left"><tr id="row29173707174853"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.1"><p id="p14260042174853"><a name="p14260042174853"></a><a name="p14260042174853"></a><strong id="b958028371"><a name="b958028371"></a><a name="b958028371"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.080000000000002%" id="mcps1.2.5.1.2"><p id="p14212742174853"><a name="p14212742174853"></a><a name="p14212742174853"></a><strong id="b840760184"><a name="b840760184"></a><a name="b840760184"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.180000000000003%" id="mcps1.2.5.1.3"><p id="p10381414174853"><a name="p10381414174853"></a><a name="p10381414174853"></a><strong id="b1987773143"><a name="b1987773143"></a><a name="b1987773143"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p35588178174853"><a name="p35588178174853"></a><a name="p35588178174853"></a><strong id="b1009301562"><a name="b1009301562"></a><a name="b1009301562"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64070195174853"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p22303345174853"><a name="p22303345174853"></a><a name="p22303345174853"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.2 "><p id="p61740531174853"><a name="p61740531174853"></a><a name="p61740531174853"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.180000000000003%" headers="mcps1.2.5.1.3 "><p id="p34927138174853"><a name="p34927138174853"></a><a name="p34927138174853"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p3737443117563"><a name="p3737443117563"></a><a name="p3737443117563"></a>Specifies the backup description. It contains a maximum of 256 characters and cannot contain the following special characters: !&lt;&gt;='&amp;"</p>
    </td>
    </tr>
    <tr id="row43181693175641"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p8056259175641"><a name="p8056259175641"></a><a name="p8056259175641"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.2 "><p id="p48577249175641"><a name="p48577249175641"></a><a name="p48577249175641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.180000000000003%" headers="mcps1.2.5.1.3 "><p id="p42443136175641"><a name="p42443136175641"></a><a name="p42443136175641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row289628251872"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.1 "><p id="p642874641872"><a name="p642874641872"></a><a name="p642874641872"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.080000000000002%" headers="mcps1.2.5.1.2 "><p id="p399020841872"><a name="p399020841872"></a><a name="p399020841872"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.180000000000003%" headers="mcps1.2.5.1.3 "><p id="p108433321872"><a name="p108433321872"></a><a name="p108433321872"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p58946721872"><a name="p58946721872"></a><a name="p58946721872"></a>Specifies the backup name. It must be 4 to 64 characters in length and start with a letter. It is case-sensitive and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
    "backup": {
    "description": "My Backup",
    "instance": "44b277eb-39be-4921-be31-3d61b43651d7",
    "name": "backup"
    }
    }
    
    
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  4**  Parameter description

    <a name="table30427456"></a>
    <table><thead align="left"><tr id="row47542385"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a><strong id="b1818790356"><a name="b1818790356"></a><a name="b1818790356"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.980000000000004%" id="mcps1.2.4.1.2"><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a><strong id="b1261223626"><a name="b1261223626"></a><a name="b1261223626"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a><strong id="b1865465272"><a name="b1865465272"></a><a name="b1865465272"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10023380"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p6587426"><a name="p6587426"></a><a name="p6587426"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p63819464"><a name="p63819464"></a><a name="p63819464"></a>Dictionary data structure. For details, see <a href="#table64140254">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p17946858"><a name="p17946858"></a><a name="p17946858"></a>Specifies the manual backup information.</p>
    </td>
    </tr>
    <tr id="row59779301181040"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p10285245181040"><a name="p10285245181040"></a><a name="p10285245181040"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p27798501181040"><a name="p27798501181040"></a><a name="p27798501181040"></a>Dictionary data structure. For details, see <a href="#table64061058181519">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p37086085181040"><a name="p37086085181040"></a><a name="p37086085181040"></a>Indicates the extended parameter.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  backup field data structure description

    <a name="table64140254"></a>
    <table><thead align="left"><tr id="row21591473"><th class="cellrowborder" valign="top" width="25.06250625062506%" id="mcps1.2.4.1.1"><p id="p4078883"><a name="p4078883"></a><a name="p4078883"></a><strong id="b1601941430"><a name="b1601941430"></a><a name="b1601941430"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.6041604160416%" id="mcps1.2.4.1.2"><p id="p61954093"><a name="p61954093"></a><a name="p61954093"></a><strong id="b2092844387"><a name="b2092844387"></a><a name="b2092844387"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p52225656"><a name="p52225656"></a><a name="p52225656"></a><strong id="b1647472196"><a name="b1647472196"></a><a name="b1647472196"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10401864181111"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p52243281181122"><a name="p52243281181122"></a><a name="p52243281181122"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p3847386181122"><a name="p3847386181122"></a><a name="p3847386181122"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43202819181122"><a name="p43202819181122"></a><a name="p43202819181122"></a>Indicates the creation time.</p>
    </td>
    </tr>
    <tr id="row2419756"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p29485073152938"><a name="p29485073152938"></a><a name="p29485073152938"></a>dataStore</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p54196734153418"><a name="p54196734153418"></a><a name="p54196734153418"></a>Dictionary data structure. For details, see <a href="#table64243102">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59806312152938"><a name="p59806312152938"></a><a name="p59806312152938"></a>Indicates the database version.</p>
    </td>
    </tr>
    <tr id="row29216213181137"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p19627321181146"><a name="p19627321181146"></a><a name="p19627321181146"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p46309135181146"><a name="p46309135181146"></a><a name="p46309135181146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60052454181146"><a name="p60052454181146"></a><a name="p60052454181146"></a>Indicates the backup description.</p>
    </td>
    </tr>
    <tr id="row62813962174428"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p28454753174428"><a name="p28454753174428"></a><a name="p28454753174428"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p23133666174428"><a name="p23133666174428"></a><a name="p23133666174428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61887659174428"><a name="p61887659174428"></a><a name="p61887659174428"></a>Indicates the backup UUID.</p>
    </td>
    </tr>
    <tr id="row2791503318123"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p1378668318126"><a name="p1378668318126"></a><a name="p1378668318126"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p4297956618126"><a name="p4297956618126"></a><a name="p4297956618126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p854191061412"><a name="p854191061412"></a><a name="p854191061412"></a>Indicates the primary node ID of the DB instance.</p>
    <div class="note" id="note154191014142"><a name="note154191014142"></a><a name="note154191014142"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1954151015148"><a name="p1954151015148"></a><a name="p1954151015148"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row13887165181219"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p55723032181222"><a name="p55723032181222"></a><a name="p55723032181222"></a>locationRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p17271744181222"><a name="p17271744181222"></a><a name="p17271744181222"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p56834037181222"><a name="p56834037181222"></a><a name="p56834037181222"></a>This is a reserved string and has no meanings.</p>
    </td>
    </tr>
    <tr id="row46332525174435"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p14339543174435"><a name="p14339543174435"></a><a name="p14339543174435"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p20652316174435"><a name="p20652316174435"></a><a name="p20652316174435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62224914174435"><a name="p62224914174435"></a><a name="p62224914174435"></a>Indicates the backup file name.</p>
    </td>
    </tr>
    <tr id="row34844678174435"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p41941392181242"><a name="p41941392181242"></a><a name="p41941392181242"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p41809621181242"><a name="p41809621181242"></a><a name="p41809621181242"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p31136163181242"><a name="p31136163181242"></a><a name="p31136163181242"></a>This is a reserved string and has no meanings.</p>
    </td>
    </tr>
    <tr id="row9098921174441"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p38860997181255"><a name="p38860997181255"></a><a name="p38860997181255"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p60733057181255"><a name="p60733057181255"></a><a name="p60733057181255"></a>Double</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p20430581181255"><a name="p20430581181255"></a><a name="p20430581181255"></a>Indicates the file size in GB. Here its value is <strong id="b829175505154351"><a name="b829175505154351"></a><a name="b829175505154351"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="row19451175174441"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p1577563218134"><a name="p1577563218134"></a><a name="p1577563218134"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p275778218134"><a name="p275778218134"></a><a name="p275778218134"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2205378918134"><a name="p2205378918134"></a><a name="p2205378918134"></a>Indicates the backing up status with the value <strong id="b84235270616328"><a name="b84235270616328"></a><a name="b84235270616328"></a>BUILDING</strong>.</p>
    </td>
    </tr>
    <tr id="row25497538174441"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p62607073181315"><a name="p62607073181315"></a><a name="p62607073181315"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p38008120181315"><a name="p38008120181315"></a><a name="p38008120181315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58758900181315"><a name="p58758900181315"></a><a name="p58758900181315"></a>Indicates the completion time with the returned value <strong id="b84235270616546"><a name="b84235270616546"></a><a name="b84235270616546"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="row27314178174653"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p64964841174653"><a name="p64964841174653"></a><a name="p64964841174653"></a>backuptype</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p27660731174653"><a name="p27660731174653"></a><a name="p27660731174653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25926754174653"><a name="p25926754174653"></a><a name="p25926754174653"></a>The default value is <strong id="b130085847154130"><a name="b130085847154130"></a><a name="b130085847154130"></a>1</strong>, indicating a manual backup.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  dataStore field data structure description

    <a name="table64243102"></a>
    <table><thead align="left"><tr id="row4043462"><th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.1"><p id="p59085005"><a name="p59085005"></a><a name="p59085005"></a><strong id="b280622447"><a name="b280622447"></a><a name="b280622447"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.42%" id="mcps1.2.4.1.2"><p id="p35921916"><a name="p35921916"></a><a name="p35921916"></a><strong id="b1821187701"><a name="b1821187701"></a><a name="b1821187701"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p23994101"><a name="p23994101"></a><a name="p23994101"></a><strong id="b647837019"><a name="b647837019"></a><a name="b647837019"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64473998"><td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.1 "><p id="p55011311"><a name="p55011311"></a><a name="p55011311"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.42%" headers="mcps1.2.4.1.2 "><p id="p17743659"><a name="p17743659"></a><a name="p17743659"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p49175803141056"><a name="p49175803141056"></a><a name="p49175803141056"></a>Indicates the DB engine. Valid value:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row40466701"><td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.1 "><p id="p56577386"><a name="p56577386"></a><a name="p56577386"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.42%" headers="mcps1.2.4.1.2 "><p id="p25105132"><a name="p25105132"></a><a name="p25105132"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p50194896154118"><a name="p50194896154118"></a><a name="p50194896154118"></a>Indicates the database version.</p>
    <p id="p20249826"><a name="p20249826"></a><a name="p20249826"></a>For example, 5.6.30.</p>
    </td>
    </tr>
    <tr id="row38087787153458"><td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.1 "><p id="p7245770153458"><a name="p7245770153458"></a><a name="p7245770153458"></a>version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.42%" headers="mcps1.2.4.1.2 "><p id="p26424346153458"><a name="p26424346153458"></a><a name="p26424346153458"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p59997264153458"><a name="p59997264153458"></a><a name="p59997264153458"></a>Indicates the database version ID. Its value is unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  extendparam field data structure description

    <a name="table64061058181519"></a>
    <table><thead align="left"><tr id="row2890742181519"><th class="cellrowborder" valign="top" width="25.06250625062506%" id="mcps1.2.4.1.1"><p id="p32823530181519"><a name="p32823530181519"></a><a name="p32823530181519"></a><strong id="b287451907"><a name="b287451907"></a><a name="b287451907"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.6041604160416%" id="mcps1.2.4.1.2"><p id="p2838432181519"><a name="p2838432181519"></a><a name="p2838432181519"></a><strong id="b673075092"><a name="b673075092"></a><a name="b673075092"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p28586417181519"><a name="p28586417181519"></a><a name="p28586417181519"></a><strong id="b1763217376"><a name="b1763217376"></a><a name="b1763217376"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33798472181519"><td class="cellrowborder" valign="top" width="25.06250625062506%" headers="mcps1.2.4.1.1 "><p id="p53321674181519"><a name="p53321674181519"></a><a name="p53321674181519"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.6041604160416%" headers="mcps1.2.4.1.2 "><p id="p4999605181519"><a name="p4999605181519"></a><a name="p4999605181519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7019864181619"><a name="p7019864181619"></a><a name="p7019864181619"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "backup": {
            "created": "2016-09-12T01:17:05",
            "dataStore": {
                "type": "MySQL",
                "version": "5.6.30",
                "version_id": "e8a8b8cc-63f8-4fb5-8d4a-24c502317a61"
            },
            "description": "123",
            "id": "2f4ddb93-b901-4b08-93d8-1d2e472f30fe",
            "instance_id": "0bc7300c-dc63-45d4-aa3b-d85bf577baac",
            "locationRef": null,
            "name": "test01",
            "parent_id": null,
            "size": null,
            "status": "BUILDING",
            "updated": null,
            "backuptype": "1"
        },
        "extendparam": {
        "jobs": [
                    "ff80808157127d9301571bf8160c001d"
                ]
          }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

