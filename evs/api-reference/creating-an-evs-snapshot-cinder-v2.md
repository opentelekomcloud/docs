# Creating an EVS Snapshot<a name="evs_04_2093"></a>

## Function<a name="section17386310104128"></a>

This API is used to create an EVS snapshot.

## URI<a name="section48475837104128"></a>

-   URI format

    POST /v2/\{project\_id\}/snapshots

-   Parameter description

    <a name="table28484833104128"></a>
    <table><thead align="left"><tr id="row60547305104128"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p5384679104128"><a name="p5384679104128"></a><a name="p5384679104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p33505894104128"><a name="p33505894104128"></a><a name="p33505894104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p29622926104128"><a name="p29622926104128"></a><a name="p29622926104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p8749302104128"><a name="p8749302104128"></a><a name="p8749302104128"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p37604871104128"><a name="p37604871104128"></a><a name="p37604871104128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p26095712104128"><a name="p26095712104128"></a><a name="p26095712104128"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33377962104128"></a>

-   Parameter description

    <a name="table1572462410119"></a>
    <table><thead align="left"><tr id="row2724724141119"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="p20724132431116"><a name="p20724132431116"></a><a name="p20724132431116"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="p3724122431120"><a name="p3724122431120"></a><a name="p3724122431120"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p15724192491114"><a name="p15724192491114"></a><a name="p15724192491114"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="p0724324121113"><a name="p0724324121113"></a><a name="p0724324121113"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row147241024121113"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p187251024171111"><a name="p187251024171111"></a><a name="p187251024171111"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="p67255248118"><a name="p67255248118"></a><a name="p67255248118"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p127251724191119"><a name="p127251724191119"></a><a name="p127251724191119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p16725122411114"><a name="p16725122411114"></a><a name="p16725122411114"></a>Specifies the information of the snapshot to be created. For details, see <a href="#li39126135104128">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li39126135104128"></a>Parameters in the  **snapshot**  field

    <a name="table16590896104128"></a>
    <table><thead align="left"><tr id="row60389002104128"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p59671014104128"><a name="p59671014104128"></a><a name="p59671014104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.2"><p id="p1513999104128"><a name="p1513999104128"></a><a name="p1513999104128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.34%" id="mcps1.1.5.1.3"><p id="p55525100104128"><a name="p55525100104128"></a><a name="p55525100104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.339999999999996%" id="mcps1.1.5.1.4"><p id="p1239270104128"><a name="p1239270104128"></a><a name="p1239270104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12756475104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p26641549104128"><a name="p26641549104128"></a><a name="p26641549104128"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p10481847104128"><a name="p10481847104128"></a><a name="p10481847104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p43723298104128"><a name="p43723298104128"></a><a name="p43723298104128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p51926262104128"><a name="p51926262104128"></a><a name="p51926262104128"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row64683174104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p4845737104128"><a name="p4845737104128"></a><a name="p4845737104128"></a>force</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p56960425104128"><a name="p56960425104128"></a><a name="p56960425104128"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p50391693104128"><a name="p50391693104128"></a><a name="p50391693104128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p32530251113919"><a name="p32530251113919"></a><a name="p32530251113919"></a>Specifies the flag for forcibly creating a snapshot. The default value is <strong id="b842352706181613"><a name="b842352706181613"></a><a name="b842352706181613"></a>false</strong>.</p>
    <a name="ul60750582141455"></a><a name="ul60750582141455"></a><ul id="ul60750582141455"><li>If this parameter is set to <strong id="b1283675572152242"><a name="b1283675572152242"></a><a name="b1283675572152242"></a>false</strong> and the disk is in the <strong id="b842352706181628"><a name="b842352706181628"></a><a name="b842352706181628"></a>attaching</strong> state, the snapshot cannot be forcibly created.</li><li>If this parameter is set to <strong id="b174167542715230"><a name="b174167542715230"></a><a name="b174167542715230"></a>true</strong> and the disk is in the <strong id="b842352706181628_1"><a name="b842352706181628_1"></a><a name="b842352706181628_1"></a>attaching</strong> state, the snapshot can be forcibly created.</li></ul>
    </td>
    </tr>
    <tr id="row26995886104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p39183164104128"><a name="p39183164104128"></a><a name="p39183164104128"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p19719755104128"><a name="p19719755104128"></a><a name="p19719755104128"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p53796355104128"><a name="p53796355104128"></a><a name="p53796355104128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p62537483104128"><a name="p62537483104128"></a><a name="p62537483104128"></a>Specifies the snapshot metadata.</p>
    </td>
    </tr>
    <tr id="row25966436104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p22906600104128"><a name="p22906600104128"></a><a name="p22906600104128"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p43495312104128"><a name="p43495312104128"></a><a name="p43495312104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p33459397104128"><a name="p33459397104128"></a><a name="p33459397104128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p25856622104128"><a name="p25856622104128"></a><a name="p25856622104128"></a>Specifies the snapshot description. The value can be <strong id="b84235270618184"><a name="b84235270618184"></a><a name="b84235270618184"></a>null</strong>. <span id="text503174715201714"><a name="text503174715201714"></a><a name="text503174715201714"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row31383010104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p58995861104128"><a name="p58995861104128"></a><a name="p58995861104128"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p13935408104128"><a name="p13935408104128"></a><a name="p13935408104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p55026268104128"><a name="p55026268104128"></a><a name="p55026268104128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p27942720104128"><a name="p27942720104128"></a><a name="p27942720104128"></a>Specifies the snapshot name. <span id="text1418954783201721"><a name="text1418954783201721"></a><a name="text1418954783201721"></a>The value can contain a maximum of 255 bytes.</span></p>
    <div class="note" id="note12652884103214"><a name="note12652884103214"></a><a name="note12652884103214"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p46767097103214"><a name="p46767097103214"></a><a name="p46767097103214"></a>When creating a backup for a disk, a snapshot will be created and named with prefix <strong id="b84235270616432"><a name="b84235270616432"></a><a name="b84235270616432"></a>autobk_snapshot_</strong>. The EVS console has imposed operation restrictions on snapshots with prefix <strong id="b842352706164512"><a name="b842352706164512"></a><a name="b842352706164512"></a>autobk_snapshot_</strong>. Therefore, you are advised not to use <strong id="b842352706164552"><a name="b842352706164552"></a><a name="b842352706164552"></a>autobk_snapshot_</strong> as the name prefix for the snapshots you created. Otherwise, the snapshots cannot be used normally.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "snapshot": {
            "name": "snap-001", 
            "description": "Daily backup", 
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635", 
            "force": false, 
            "metadata": { }
        }
    }
    ```


## Response<a name="section26860493104128"></a>

-   Parameter description

    <a name="table6828747432"></a>
    <table><thead align="left"><tr id="row382812473312"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p198297471937"><a name="p198297471937"></a><a name="p198297471937"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p2082911475318"><a name="p2082911475318"></a><a name="p2082911475318"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p182916473314"><a name="p182916473314"></a><a name="p182916473314"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row168291947832"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p982919471312"><a name="p982919471312"></a><a name="p982919471312"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p08292471734"><a name="p08292471734"></a><a name="p08292471734"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p208298477312"><a name="p208298477312"></a><a name="p208298477312"></a>Specifies the snapshot information. For details, see <a href="#li52620487104128">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    <tr id="row5943559134615"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li52620487104128"></a>Parameters in the  **snapshot**  field

    <a name="table3822335104128"></a>
    <table><thead align="left"><tr id="row44730354104128"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p66388932104128"><a name="p66388932104128"></a><a name="p66388932104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p8794435104128"><a name="p8794435104128"></a><a name="p8794435104128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p53776742104128"><a name="p53776742104128"></a><a name="p53776742104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41515896104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p7344400104128"><a name="p7344400104128"></a><a name="p7344400104128"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p58025504104128"><a name="p58025504104128"></a><a name="p58025504104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p63859146104128"><a name="p63859146104128"></a><a name="p63859146104128"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row37861410104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p46875355104128"><a name="p46875355104128"></a><a name="p46875355104128"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p38807409104128"><a name="p38807409104128"></a><a name="p38807409104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4381265104128"><a name="p4381265104128"></a><a name="p4381265104128"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row39431393104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p39826261104128"><a name="p39826261104128"></a><a name="p39826261104128"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p4701738104128"><a name="p4701738104128"></a><a name="p4701738104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p45139478104128"><a name="p45139478104128"></a><a name="p45139478104128"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="row3602118104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p23336160104128"><a name="p23336160104128"></a><a name="p23336160104128"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p11180798104128"><a name="p11180798104128"></a><a name="p11180798104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p7230824104128"><a name="p7230824104128"></a><a name="p7230824104128"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="row65077419104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p36779556104128"><a name="p36779556104128"></a><a name="p36779556104128"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p26354021104128"><a name="p26354021104128"></a><a name="p26354021104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p36300897104128"><a name="p36300897104128"></a><a name="p36300897104128"></a>Specifies the time when the snapshot was created.</p>
    <p id="p1277514183418"><a name="p1277514183418"></a><a name="p1277514183418"></a><span id="text56625358415"><a name="text56625358415"></a><a name="text56625358415"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row58272623104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p22462033104128"><a name="p22462033104128"></a><a name="p22462033104128"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p7485408104128"><a name="p7485408104128"></a><a name="p7485408104128"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p55185187104128"><a name="p55185187104128"></a><a name="p55185187104128"></a>Specifies the snapshot metadata.</p>
    </td>
    </tr>
    <tr id="row26904637104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p31791970104128"><a name="p31791970104128"></a><a name="p31791970104128"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p25012792104128"><a name="p25012792104128"></a><a name="p25012792104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p27759637104128"><a name="p27759637104128"></a><a name="p27759637104128"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row48510149104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p37007959104128"><a name="p37007959104128"></a><a name="p37007959104128"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p44854718104128"><a name="p44854718104128"></a><a name="p44854718104128"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p19441706104128"><a name="p19441706104128"></a><a name="p19441706104128"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="row40757631104128"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p13033849104128"><a name="p13033849104128"></a><a name="p13033849104128"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p49108876104128"><a name="p49108876104128"></a><a name="p49108876104128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p13680922104128"><a name="p13680922104128"></a><a name="p13680922104128"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p24641261550"><a name="p24641261550"></a><a name="p24641261550"></a><span id="text123011106519"><a name="text123011106519"></a><a name="text123011106519"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "snapshot": {
            "status": "creating", 
            "description": "Daily backup", 
            "created_at": "2013-02-25T03:56:53.081642", 
            "metadata": { }, 
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635", 
            "size": 1, 
            "id": "ffa9bc5e-1172-4021-acaf-cdcd78a9584d", 
            "name": "snap-001", 
            "updated_at": "2013-02-25T03:56:53.081642"
        }
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section10171239104128"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

