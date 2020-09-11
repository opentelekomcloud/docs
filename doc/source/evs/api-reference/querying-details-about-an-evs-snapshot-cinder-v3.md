# Querying Details About an EVS Snapshot<a name="evs_04_3061"></a>

## Function<a name="section30030484111731"></a>

This API is used to query details about an EVS snapshot.

## URI<a name="section14733765111731"></a>

-   URI format

    GET /v3/\{project\_id\}/snapshots/\{snapshot\_id\}

-   Parameter description

    <a name="table66271751111731"></a>
    <table><thead align="left"><tr id="row56106054111731"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p48296540111731"><a name="p48296540111731"></a><a name="p48296540111731"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p19705674111731"><a name="p19705674111731"></a><a name="p19705674111731"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p52655801111731"><a name="p52655801111731"></a><a name="p52655801111731"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37261521111731"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p65393209111731"><a name="p65393209111731"></a><a name="p65393209111731"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p62358553111731"><a name="p62358553111731"></a><a name="p62358553111731"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p17878042111731"><a name="p17878042111731"></a><a name="p17878042111731"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row26684654111731"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p13973379111731"><a name="p13973379111731"></a><a name="p13973379111731"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p58101900111731"><a name="p58101900111731"></a><a name="p58101900111731"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p8633458111731"><a name="p8633458111731"></a><a name="p8633458111731"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section28221468111731"></a>

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/snapshots/f9faf7df-fdc1-4093-9ef3-5cba06eef995
    ```


## Response<a name="section63055193111836"></a>

-   Parameter description

    <a name="table12730134172713"></a>
    <table><thead align="left"><tr id="row473014182718"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p7730941122712"><a name="p7730941122712"></a><a name="p7730941122712"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p7731104122719"><a name="p7731104122719"></a><a name="p7731104122719"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p4731184118271"><a name="p4731184118271"></a><a name="p4731184118271"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2073111417271"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p6732134115272"><a name="p6732134115272"></a><a name="p6732134115272"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p17732141102714"><a name="p17732141102714"></a><a name="p17732141102714"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p11732194114271"><a name="p11732194114271"></a><a name="p11732194114271"></a>Specifies the snapshot information. For details, see <a href="#en-us_topic_0051408628_li64773086111836">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    <tr id="row1273219418275"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="en-us_topic_0051408628_li64773086111836"></a>Parameters in the  **snapshot**  field

    <a name="en-us_topic_0051408628_table46086870111836"></a>
    <table><thead align="left"><tr id="en-us_topic_0051408628_row56202297111836"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="en-us_topic_0051408628_p56092213111836"><a name="en-us_topic_0051408628_p56092213111836"></a><a name="en-us_topic_0051408628_p56092213111836"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="en-us_topic_0051408628_p47175401111836"><a name="en-us_topic_0051408628_p47175401111836"></a><a name="en-us_topic_0051408628_p47175401111836"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="en-us_topic_0051408628_p11730844111836"><a name="en-us_topic_0051408628_p11730844111836"></a><a name="en-us_topic_0051408628_p11730844111836"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0051408628_row15559516111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p52361272111836"><a name="en-us_topic_0051408628_p52361272111836"></a><a name="en-us_topic_0051408628_p52361272111836"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p13404600111836"><a name="en-us_topic_0051408628_p13404600111836"></a><a name="en-us_topic_0051408628_p13404600111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p34969797111836"><a name="en-us_topic_0051408628_p34969797111836"></a><a name="en-us_topic_0051408628_p34969797111836"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row46292725111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p58723264111836"><a name="en-us_topic_0051408628_p58723264111836"></a><a name="en-us_topic_0051408628_p58723264111836"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p58963956111836"><a name="en-us_topic_0051408628_p58963956111836"></a><a name="en-us_topic_0051408628_p58963956111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p47023540111836"><a name="en-us_topic_0051408628_p47023540111836"></a><a name="en-us_topic_0051408628_p47023540111836"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row20558679111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p54640283111836"><a name="en-us_topic_0051408628_p54640283111836"></a><a name="en-us_topic_0051408628_p54640283111836"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p63786796111836"><a name="en-us_topic_0051408628_p63786796111836"></a><a name="en-us_topic_0051408628_p63786796111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p14293074111836"><a name="en-us_topic_0051408628_p14293074111836"></a><a name="en-us_topic_0051408628_p14293074111836"></a>Specifies the snapshot name.</p>
    <p id="p5124959164711"><a name="p5124959164711"></a><a name="p5124959164711"></a>Snapshots whose names started with prefix <strong id="b322031418439"><a name="b322031418439"></a><a name="b322031418439"></a>autobk_snapshot_</strong> are automatically created by the system during backup creations. Do not delete these snapshots or use them to roll back the disk data.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row61528809111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p17777665111836"><a name="en-us_topic_0051408628_p17777665111836"></a><a name="en-us_topic_0051408628_p17777665111836"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p30704745111836"><a name="en-us_topic_0051408628_p30704745111836"></a><a name="en-us_topic_0051408628_p30704745111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p60132426111836"><a name="en-us_topic_0051408628_p60132426111836"></a><a name="en-us_topic_0051408628_p60132426111836"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row4320926111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p14450739111836"><a name="en-us_topic_0051408628_p14450739111836"></a><a name="en-us_topic_0051408628_p14450739111836"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p29659196111836"><a name="en-us_topic_0051408628_p29659196111836"></a><a name="en-us_topic_0051408628_p29659196111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p45391308111836"><a name="en-us_topic_0051408628_p45391308111836"></a><a name="en-us_topic_0051408628_p45391308111836"></a>Specifies the time when the snapshot was created.</p>
    <p id="p96931622122813"><a name="p96931622122813"></a><a name="p96931622122813"></a><span id="text20291102912819"><a name="text20291102912819"></a><a name="text20291102912819"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row3737236411149"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p80695711149"><a name="en-us_topic_0051408628_p80695711149"></a><a name="en-us_topic_0051408628_p80695711149"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p6536351711149"><a name="en-us_topic_0051408628_p6536351711149"></a><a name="en-us_topic_0051408628_p6536351711149"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p2439511411149"><a name="en-us_topic_0051408628_p2439511411149"></a><a name="en-us_topic_0051408628_p2439511411149"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p1827253412288"><a name="p1827253412288"></a><a name="p1827253412288"></a><span id="text1059311346285"><a name="text1059311346285"></a><a name="text1059311346285"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row5868590111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p5593786111836"><a name="en-us_topic_0051408628_p5593786111836"></a><a name="en-us_topic_0051408628_p5593786111836"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p50443518111836"><a name="en-us_topic_0051408628_p50443518111836"></a><a name="en-us_topic_0051408628_p50443518111836"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p46118865111836"><a name="en-us_topic_0051408628_p46118865111836"></a><a name="en-us_topic_0051408628_p46118865111836"></a>Specifies the snapshot metadata.</p>
    <p id="p1678772717473"><a name="p1678772717473"></a><a name="p1678772717473"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row12416602111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p66220711111836"><a name="en-us_topic_0051408628_p66220711111836"></a><a name="en-us_topic_0051408628_p66220711111836"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p62277393111836"><a name="en-us_topic_0051408628_p62277393111836"></a><a name="en-us_topic_0051408628_p62277393111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p43213914111836"><a name="en-us_topic_0051408628_p43213914111836"></a><a name="en-us_topic_0051408628_p43213914111836"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row53380907111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p28886228111836"><a name="en-us_topic_0051408628_p28886228111836"></a><a name="en-us_topic_0051408628_p28886228111836"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p58083101111836"><a name="en-us_topic_0051408628_p58083101111836"></a><a name="en-us_topic_0051408628_p58083101111836"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p39095984111836"><a name="en-us_topic_0051408628_p39095984111836"></a><a name="en-us_topic_0051408628_p39095984111836"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row16319538111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p46814240111836"><a name="en-us_topic_0051408628_p46814240111836"></a><a name="en-us_topic_0051408628_p46814240111836"></a>os-extended-snapshot-attributes:project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p33857106111836"><a name="en-us_topic_0051408628_p33857106111836"></a><a name="en-us_topic_0051408628_p33857106111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p6137764111836"><a name="en-us_topic_0051408628_p6137764111836"></a><a name="en-us_topic_0051408628_p6137764111836"></a>Specifies the tenant ID. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408628_row55239881111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408628_p45245366111836"><a name="en-us_topic_0051408628_p45245366111836"></a><a name="en-us_topic_0051408628_p45245366111836"></a>os-extended-snapshot-attributes:progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408628_p40996011111836"><a name="en-us_topic_0051408628_p40996011111836"></a><a name="en-us_topic_0051408628_p40996011111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408628_p18028606145913"><a name="en-us_topic_0051408628_p18028606145913"></a><a name="en-us_topic_0051408628_p18028606145913"></a><span id="text4730642777"><a name="text4730642777"></a><a name="text4730642777"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row1598314715534"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p1316171114535"><a name="p1316171114535"></a><a name="p1316171114535"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p8316101125312"><a name="p8316101125312"></a><a name="p8316101125312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p20348100143311"><a name="p20348100143311"></a><a name="p20348100143311"></a>Reserved field</p>
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
            "status": "available", 
            "os-extended-snapshot-attributes:progress": "100%", 
            "description": "daily backup", 
            "created_at": "2013-02-25t04:13:17.000000", 
            "metadata": { }, 
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635", 
            "os-extended-snapshot-attributes:project_id": "0c2eba2c5af04d3f9e9d0d410b371fde", 
            "size": 1, 
            "user_id": "48d70679b8644035846b2cb53633c256", 
            "id": "2bb856e1-b3d8-4432-a858-09e4ce939389", 
            "name": "snap-001", 
            "updated_at": null
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


## Status Codes<a name="section38811440112026"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

