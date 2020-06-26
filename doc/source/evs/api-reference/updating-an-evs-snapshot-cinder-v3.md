# Updating an EVS Snapshot<a name="evs_04_3058"></a>

## Function<a name="section4805694511340"></a>

This API is used to update an EVS snapshot.

## URI<a name="section268627411340"></a>

-   URI format

    PUT /v3/\{project\_id\}/snapshots/\{snapshot\_id\}

-   Parameter description

    <a name="table5655293911340"></a>
    <table><thead align="left"><tr id="row4718979611340"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p6427715211340"><a name="p6427715211340"></a><a name="p6427715211340"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p3906685711340"><a name="p3906685711340"></a><a name="p3906685711340"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p1029885411340"><a name="p1029885411340"></a><a name="p1029885411340"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2890086411340"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p5926863811340"><a name="p5926863811340"></a><a name="p5926863811340"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p3603037711340"><a name="p3603037711340"></a><a name="p3603037711340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p3277940011340"><a name="p3277940011340"></a><a name="p3277940011340"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row2657914711340"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p542726811340"><a name="p542726811340"></a><a name="p542726811340"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p3695552511340"><a name="p3695552511340"></a><a name="p3695552511340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p4060754311340"><a name="p4060754311340"></a><a name="p4060754311340"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section87667311340"></a>

-   Parameter description

    <a name="evs_04_2095_table741545961616"></a>
    <table><thead align="left"><tr id="evs_04_2095_row8415125912161"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="evs_04_2095_p15415175914166"><a name="evs_04_2095_p15415175914166"></a><a name="evs_04_2095_p15415175914166"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="evs_04_2095_p16415155919169"><a name="evs_04_2095_p16415155919169"></a><a name="evs_04_2095_p16415155919169"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.3"><p id="evs_04_2095_p1741511599167"><a name="evs_04_2095_p1741511599167"></a><a name="evs_04_2095_p1741511599167"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.1.5.1.4"><p id="evs_04_2095_p7415059161614"><a name="evs_04_2095_p7415059161614"></a><a name="evs_04_2095_p7415059161614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2095_row3416259191613"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="evs_04_2095_p16416195961611"><a name="evs_04_2095_p16416195961611"></a><a name="evs_04_2095_p16416195961611"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="evs_04_2095_p94161059141619"><a name="evs_04_2095_p94161059141619"></a><a name="evs_04_2095_p94161059141619"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="evs_04_2095_p841615914166"><a name="evs_04_2095_p841615914166"></a><a name="evs_04_2095_p841615914166"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.1.5.1.4 "><p id="evs_04_2095_p15416155911161"><a name="evs_04_2095_p15416155911161"></a><a name="evs_04_2095_p15416155911161"></a>Specifies the information of the snapshot to be updated. For details, see <a href="#evs_04_2095_li143506387236">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="evs_04_2095_li143506387236"></a>Parameters in the  **snapshot**  field

    <a name="evs_04_2095_table16590896104128"></a>
    <table><thead align="left"><tr id="evs_04_2095_row60389002104128"><th class="cellrowborder" valign="top" width="19.61%" id="mcps1.1.5.1.1"><p id="evs_04_2095_p59671014104128"><a name="evs_04_2095_p59671014104128"></a><a name="evs_04_2095_p59671014104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.59%" id="mcps1.1.5.1.2"><p id="evs_04_2095_p1513999104128"><a name="evs_04_2095_p1513999104128"></a><a name="evs_04_2095_p1513999104128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.580000000000002%" id="mcps1.1.5.1.3"><p id="evs_04_2095_p55525100104128"><a name="evs_04_2095_p55525100104128"></a><a name="evs_04_2095_p55525100104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.220000000000006%" id="mcps1.1.5.1.4"><p id="evs_04_2095_p1239270104128"><a name="evs_04_2095_p1239270104128"></a><a name="evs_04_2095_p1239270104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2095_row33272036104128"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.1 "><p id="evs_04_2095_p43959720162736"><a name="evs_04_2095_p43959720162736"></a><a name="evs_04_2095_p43959720162736"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.59%" headers="mcps1.1.5.1.2 "><p id="evs_04_2095_p3967568162736"><a name="evs_04_2095_p3967568162736"></a><a name="evs_04_2095_p3967568162736"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.580000000000002%" headers="mcps1.1.5.1.3 "><p id="evs_04_2095_p52937605162736"><a name="evs_04_2095_p52937605162736"></a><a name="evs_04_2095_p52937605162736"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.220000000000006%" headers="mcps1.1.5.1.4 "><p id="evs_04_2095_p60087598162736"><a name="evs_04_2095_p60087598162736"></a><a name="evs_04_2095_p60087598162736"></a>Specifies the snapshot name. <span id="evs_04_2095_text278683662201749"><a name="evs_04_2095_text278683662201749"></a><a name="evs_04_2095_text278683662201749"></a>The value can contain a maximum of 255 bytes.</span></p>
    <div class="note" id="evs_04_2095_note154651827114612"><a name="evs_04_2095_note154651827114612"></a><a name="evs_04_2095_note154651827114612"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2095_evs_04_2093_p46767097103214"><a name="evs_04_2095_evs_04_2093_p46767097103214"></a><a name="evs_04_2095_evs_04_2093_p46767097103214"></a>When creating a backup for a disk, a snapshot will be created and named with prefix <strong id="evs_04_2095_evs_04_2093_b84235270616432"><a name="evs_04_2095_evs_04_2093_b84235270616432"></a><a name="evs_04_2095_evs_04_2093_b84235270616432"></a>autobk_snapshot_</strong>. The EVS console has imposed operation restrictions on snapshots with prefix <strong id="evs_04_2095_evs_04_2093_b842352706164512"><a name="evs_04_2095_evs_04_2093_b842352706164512"></a><a name="evs_04_2095_evs_04_2093_b842352706164512"></a>autobk_snapshot_</strong>. Therefore, you are advised not to use <strong id="evs_04_2095_evs_04_2093_b842352706164552"><a name="evs_04_2095_evs_04_2093_b842352706164552"></a><a name="evs_04_2095_evs_04_2093_b842352706164552"></a>autobk_snapshot_</strong> as the name prefix for the snapshots you created. Otherwise, the snapshots cannot be used normally.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2095_row12756475104128"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.1 "><p id="evs_04_2095_p48879957162736"><a name="evs_04_2095_p48879957162736"></a><a name="evs_04_2095_p48879957162736"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.59%" headers="mcps1.1.5.1.2 "><p id="evs_04_2095_p66962416162736"><a name="evs_04_2095_p66962416162736"></a><a name="evs_04_2095_p66962416162736"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.580000000000002%" headers="mcps1.1.5.1.3 "><p id="evs_04_2095_p55246620162736"><a name="evs_04_2095_p55246620162736"></a><a name="evs_04_2095_p55246620162736"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.220000000000006%" headers="mcps1.1.5.1.4 "><p id="evs_04_2095_p45791232162736"><a name="evs_04_2095_p45791232162736"></a><a name="evs_04_2095_p45791232162736"></a>Specifies the snapshot description. <span id="evs_04_2095_text123973587201810"><a name="evs_04_2095_text123973587201810"></a><a name="evs_04_2095_text123973587201810"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2095_row26493997162819"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.1 "><p id="evs_04_2095_p12659426162825"><a name="evs_04_2095_p12659426162825"></a><a name="evs_04_2095_p12659426162825"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.59%" headers="mcps1.1.5.1.2 "><p id="evs_04_2095_p18780582162825"><a name="evs_04_2095_p18780582162825"></a><a name="evs_04_2095_p18780582162825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.580000000000002%" headers="mcps1.1.5.1.3 "><p id="evs_04_2095_p44832203162825"><a name="evs_04_2095_p44832203162825"></a><a name="evs_04_2095_p44832203162825"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.220000000000006%" headers="mcps1.1.5.1.4 "><p id="evs_04_2095_p7529849162825"><a name="evs_04_2095_p7529849162825"></a><a name="evs_04_2095_p7529849162825"></a>Specifies also the snapshot name. You can specify either parameter <strong id="evs_04_2095_b84235270614459"><a name="evs_04_2095_b84235270614459"></a><a name="evs_04_2095_b84235270614459"></a>name</strong> or <strong id="evs_04_2095_b842352706144516"><a name="evs_04_2095_b842352706144516"></a><a name="evs_04_2095_b842352706144516"></a>display_name</strong>. If both parameters are specified, the <strong id="evs_04_2095_b2131783664144619"><a name="evs_04_2095_b2131783664144619"></a><a name="evs_04_2095_b2131783664144619"></a>name</strong> value is used. <span id="evs_04_2095_text131358535201823"><a name="evs_04_2095_text131358535201823"></a><a name="evs_04_2095_text131358535201823"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2095_row40792854162816"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.1.5.1.1 "><p id="evs_04_2095_p53442063162825"><a name="evs_04_2095_p53442063162825"></a><a name="evs_04_2095_p53442063162825"></a>display_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.59%" headers="mcps1.1.5.1.2 "><p id="evs_04_2095_p33839865162825"><a name="evs_04_2095_p33839865162825"></a><a name="evs_04_2095_p33839865162825"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.580000000000002%" headers="mcps1.1.5.1.3 "><p id="evs_04_2095_p56674535162825"><a name="evs_04_2095_p56674535162825"></a><a name="evs_04_2095_p56674535162825"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.220000000000006%" headers="mcps1.1.5.1.4 "><p id="evs_04_2095_p27234626162825"><a name="evs_04_2095_p27234626162825"></a><a name="evs_04_2095_p27234626162825"></a>Specifies also the snapshot description. You can specify either parameter <strong id="evs_04_2095_b842352706151715"><a name="evs_04_2095_b842352706151715"></a><a name="evs_04_2095_b842352706151715"></a>description</strong> or <strong id="evs_04_2095_b842352706151722"><a name="evs_04_2095_b842352706151722"></a><a name="evs_04_2095_b842352706151722"></a>display_description</strong>. <span id="evs_04_2095_text32804801201832"><a name="evs_04_2095_text32804801201832"></a><a name="evs_04_2095_text32804801201832"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "snapshot": {
            "name": "snap-001", 
            "description": "Daily backup"
        }
    }
    ```


## Response<a name="section5147449911340"></a>

-   Parameter description

    <a name="evs_04_2095_table5724531817"></a>
    <table><thead align="left"><tr id="evs_04_2095_row473553186"><th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.1"><p id="evs_04_2095_p1373105313817"><a name="evs_04_2095_p1373105313817"></a><a name="evs_04_2095_p1373105313817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.2"><p id="evs_04_2095_p11731053784"><a name="evs_04_2095_p11731053784"></a><a name="evs_04_2095_p11731053784"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.24467553244675%" id="mcps1.1.4.1.3"><p id="evs_04_2095_p4736536811"><a name="evs_04_2095_p4736536811"></a><a name="evs_04_2095_p4736536811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2095_row197316531287"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p18731553886"><a name="evs_04_2095_p18731553886"></a><a name="evs_04_2095_p18731553886"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p14731953385"><a name="evs_04_2095_p14731953385"></a><a name="evs_04_2095_p14731953385"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p3731053387"><a name="evs_04_2095_p3731053387"></a><a name="evs_04_2095_p3731053387"></a>Specifies the snapshot information. For details, see <a href="#evs_04_2095_li8366143102514">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row9804140716"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p129522216412"><a name="evs_04_2095_p129522216412"></a><a name="evs_04_2095_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p1595262111415"><a name="evs_04_2095_p1595262111415"></a><a name="evs_04_2095_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p109527215417"><a name="evs_04_2095_p109527215417"></a><a name="evs_04_2095_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2095_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="evs_04_2095_li8366143102514"></a>Parameters in the  **snapshot**  field

    <a name="evs_04_2095_table251963102518"></a>
    <table><thead align="left"><tr id="evs_04_2095_row18517183132513"><th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.1"><p id="evs_04_2095_p17515931252"><a name="evs_04_2095_p17515931252"></a><a name="evs_04_2095_p17515931252"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.377662233776622%" id="mcps1.1.4.1.2"><p id="evs_04_2095_p7515173192517"><a name="evs_04_2095_p7515173192517"></a><a name="evs_04_2095_p7515173192517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.24467553244675%" id="mcps1.1.4.1.3"><p id="evs_04_2095_p05179317252"><a name="evs_04_2095_p05179317252"></a><a name="evs_04_2095_p05179317252"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2095_row351716312517"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p8517838253"><a name="evs_04_2095_p8517838253"></a><a name="evs_04_2095_p8517838253"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p125173352512"><a name="evs_04_2095_p125173352512"></a><a name="evs_04_2095_p125173352512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p1251783102517"><a name="evs_04_2095_p1251783102517"></a><a name="evs_04_2095_p1251783102517"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row451813317253"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1451818312254"><a name="evs_04_2095_p1451818312254"></a><a name="evs_04_2095_p1451818312254"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p115184372510"><a name="evs_04_2095_p115184372510"></a><a name="evs_04_2095_p115184372510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p151812362515"><a name="evs_04_2095_p151812362515"></a><a name="evs_04_2095_p151812362515"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row16518132257"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1051853182512"><a name="evs_04_2095_p1051853182512"></a><a name="evs_04_2095_p1051853182512"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p205185362515"><a name="evs_04_2095_p205185362515"></a><a name="evs_04_2095_p205185362515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p1651863172513"><a name="evs_04_2095_p1651863172513"></a><a name="evs_04_2095_p1651863172513"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row5518163152514"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1751813313259"><a name="evs_04_2095_p1751813313259"></a><a name="evs_04_2095_p1751813313259"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p155189382519"><a name="evs_04_2095_p155189382519"></a><a name="evs_04_2095_p155189382519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p165181362512"><a name="evs_04_2095_p165181362512"></a><a name="evs_04_2095_p165181362512"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row5518137256"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p125182382518"><a name="evs_04_2095_p125182382518"></a><a name="evs_04_2095_p125182382518"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p951813311252"><a name="evs_04_2095_p951813311252"></a><a name="evs_04_2095_p951813311252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p115181317254"><a name="evs_04_2095_p115181317254"></a><a name="evs_04_2095_p115181317254"></a>Specifies the time when the snapshot was created.</p>
    <p id="evs_04_2095_p10500514493"><a name="evs_04_2095_p10500514493"></a><a name="evs_04_2095_p10500514493"></a><span id="evs_04_2095_text859662881020"><a name="evs_04_2095_text859662881020"></a><a name="evs_04_2095_text859662881020"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2095_row10519133253"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1951843112514"><a name="evs_04_2095_p1951843112514"></a><a name="evs_04_2095_p1951843112514"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p13519163112515"><a name="evs_04_2095_p13519163112515"></a><a name="evs_04_2095_p13519163112515"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p251915313258"><a name="evs_04_2095_p251915313258"></a><a name="evs_04_2095_p251915313258"></a>Specifies the snapshot metadata.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row165197362511"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1451913102511"><a name="evs_04_2095_p1451913102511"></a><a name="evs_04_2095_p1451913102511"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p1351963112514"><a name="evs_04_2095_p1351963112514"></a><a name="evs_04_2095_p1351963112514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p551913316258"><a name="evs_04_2095_p551913316258"></a><a name="evs_04_2095_p551913316258"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row10519163192515"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1351923142514"><a name="evs_04_2095_p1351923142514"></a><a name="evs_04_2095_p1351923142514"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p65190317252"><a name="evs_04_2095_p65190317252"></a><a name="evs_04_2095_p65190317252"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p1451963122512"><a name="evs_04_2095_p1451963122512"></a><a name="evs_04_2095_p1451963122512"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_row25191735255"><td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_p1951903192520"><a name="evs_04_2095_p1951903192520"></a><a name="evs_04_2095_p1951903192520"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.377662233776622%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_p165198313255"><a name="evs_04_2095_p165198313255"></a><a name="evs_04_2095_p165198313255"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.24467553244675%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_p95191639256"><a name="evs_04_2095_p95191639256"></a><a name="evs_04_2095_p95191639256"></a>Specifies the time when the snapshot was updated.</p>
    <p id="evs_04_2095_p972113371011"><a name="evs_04_2095_p972113371011"></a><a name="evs_04_2095_p972113371011"></a><span id="evs_04_2095_text140163851010"><a name="evs_04_2095_text140163851010"></a><a name="evs_04_2095_text140163851010"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2095_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2095_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2095_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2095_evs_04_2013_p19541716103019"><a name="evs_04_2095_evs_04_2013_p19541716103019"></a><a name="evs_04_2095_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2095_evs_04_2013_p39375186103019"><a name="evs_04_2095_evs_04_2013_p39375186103019"></a><a name="evs_04_2095_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2095_evs_04_2013_p38578950103019"><a name="evs_04_2095_evs_04_2013_p38578950103019"></a><a name="evs_04_2095_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2095_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_evs_04_2013_p46815658103019"><a name="evs_04_2095_evs_04_2013_p46815658103019"></a><a name="evs_04_2095_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_evs_04_2013_p33971979103019"><a name="evs_04_2095_evs_04_2013_p33971979103019"></a><a name="evs_04_2095_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_evs_04_2013_p21623243103019"><a name="evs_04_2095_evs_04_2013_p21623243103019"></a><a name="evs_04_2095_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2095_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2095_evs_04_2013_p59870541103019"><a name="evs_04_2095_evs_04_2013_p59870541103019"></a><a name="evs_04_2095_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2095_evs_04_2013_p17675690103019"><a name="evs_04_2095_evs_04_2013_p17675690103019"></a><a name="evs_04_2095_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2095_evs_04_2013_p6087468103019"><a name="evs_04_2095_evs_04_2013_p6087468103019"></a><a name="evs_04_2095_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2095_evs_04_2013_p54787218103019"><a name="evs_04_2095_evs_04_2013_p54787218103019"></a><a name="evs_04_2095_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "snapshot": {
            "status": "available", 
            "description": "Daily backup", 
            "created_at": "2013-02-25T03:56:53.081642", 
            "metadata": { }, 
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635", 
            "size": 1, 
            "id": "f9faf7df-fdc1-4093-9ef3-5cba06eef995", 
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


## Status Codes<a name="section1751558211340"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

