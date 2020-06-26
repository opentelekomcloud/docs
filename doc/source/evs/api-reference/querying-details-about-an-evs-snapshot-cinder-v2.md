# Querying Details About an EVS Snapshot<a name="evs_04_2098"></a>

## Function<a name="section30030484111731"></a>

This API is used to query details about an EVS snapshot.

## URI<a name="section14733765111731"></a>

-   URI format

    GET /v2/\{project\_id\}/snapshots/\{snapshot\_id\}

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
    GET https://{endpoint}/v2/{project_id}/snapshots/f9faf7df-fdc1-4093-9ef3-5cba06eef995
    ```


## Response<a name="section63055193111836"></a>

-   Parameter description

    <a name="table12298112761311"></a>
    <table><thead align="left"><tr id="row3298122761310"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p1129817277138"><a name="p1129817277138"></a><a name="p1129817277138"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p102981727131315"><a name="p102981727131315"></a><a name="p102981727131315"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p1829872710136"><a name="p1829872710136"></a><a name="p1829872710136"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1029817278135"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p72986273130"><a name="p72986273130"></a><a name="p72986273130"></a>snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p3299527151313"><a name="p3299527151313"></a><a name="p3299527151313"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p102991727171313"><a name="p102991727171313"></a><a name="p102991727171313"></a>Specifies the snapshot information. For details, see <a href="#li64773086111836">Parameters in the snapshot field</a>.</p>
    </td>
    </tr>
    <tr id="row1148619118454"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li64773086111836"></a>Parameters in the  **snapshot**  field

    <a name="table46086870111836"></a>
    <table><thead align="left"><tr id="row56202297111836"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p56092213111836"><a name="p56092213111836"></a><a name="p56092213111836"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p47175401111836"><a name="p47175401111836"></a><a name="p47175401111836"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p11730844111836"><a name="p11730844111836"></a><a name="p11730844111836"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15559516111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p52361272111836"><a name="p52361272111836"></a><a name="p52361272111836"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p13404600111836"><a name="p13404600111836"></a><a name="p13404600111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p34969797111836"><a name="p34969797111836"></a><a name="p34969797111836"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row46292725111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p58723264111836"><a name="p58723264111836"></a><a name="p58723264111836"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p58963956111836"><a name="p58963956111836"></a><a name="p58963956111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p47023540111836"><a name="p47023540111836"></a><a name="p47023540111836"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row20558679111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p54640283111836"><a name="p54640283111836"></a><a name="p54640283111836"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p63786796111836"><a name="p63786796111836"></a><a name="p63786796111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p14293074111836"><a name="p14293074111836"></a><a name="p14293074111836"></a>Specifies the snapshot name.</p>
    <p id="p1338613133449"><a name="p1338613133449"></a><a name="p1338613133449"></a>Snapshots whose names started with prefix <strong id="b8266932154912"><a name="b8266932154912"></a><a name="b8266932154912"></a>autobk_snapshot_</strong> are automatically created by the system during backup creations. Do not delete these snapshots or use them to roll back the disk data.</p>
    </td>
    </tr>
    <tr id="row61528809111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p17777665111836"><a name="p17777665111836"></a><a name="p17777665111836"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p30704745111836"><a name="p30704745111836"></a><a name="p30704745111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p60132426111836"><a name="p60132426111836"></a><a name="p60132426111836"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="row4320926111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p14450739111836"><a name="p14450739111836"></a><a name="p14450739111836"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p29659196111836"><a name="p29659196111836"></a><a name="p29659196111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p45391308111836"><a name="p45391308111836"></a><a name="p45391308111836"></a>Specifies the time when the snapshot was created.</p>
    <p id="p1559945216131"><a name="p1559945216131"></a><a name="p1559945216131"></a><span id="text462016291416"><a name="text462016291416"></a><a name="text462016291416"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row3737236411149"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p80695711149"><a name="p80695711149"></a><a name="p80695711149"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p6536351711149"><a name="p6536351711149"></a><a name="p6536351711149"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p2439511411149"><a name="p2439511411149"></a><a name="p2439511411149"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p4282185140"><a name="p4282185140"></a><a name="p4282185140"></a><span id="text106095811141"><a name="text106095811141"></a><a name="text106095811141"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row5868590111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p5593786111836"><a name="p5593786111836"></a><a name="p5593786111836"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p50443518111836"><a name="p50443518111836"></a><a name="p50443518111836"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p46118865111836"><a name="p46118865111836"></a><a name="p46118865111836"></a>Specifies the snapshot metadata.</p>
    <p id="p771812911458"><a name="p771812911458"></a><a name="p771812911458"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="row12416602111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p66220711111836"><a name="p66220711111836"></a><a name="p66220711111836"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p62277393111836"><a name="p62277393111836"></a><a name="p62277393111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p43213914111836"><a name="p43213914111836"></a><a name="p43213914111836"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row53380907111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p28886228111836"><a name="p28886228111836"></a><a name="p28886228111836"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p58083101111836"><a name="p58083101111836"></a><a name="p58083101111836"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p39095984111836"><a name="p39095984111836"></a><a name="p39095984111836"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="row16319538111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p46814240111836"><a name="p46814240111836"></a><a name="p46814240111836"></a>os-extended-snapshot-attributes:project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p33857106111836"><a name="p33857106111836"></a><a name="p33857106111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p6137764111836"><a name="p6137764111836"></a><a name="p6137764111836"></a>Specifies the tenant ID. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row55239881111836"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p45245366111836"><a name="p45245366111836"></a><a name="p45245366111836"></a>os-extended-snapshot-attributes:progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p40996011111836"><a name="p40996011111836"></a><a name="p40996011111836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0123550104_p170219911618"><a name="en-us_topic_0123550104_p170219911618"></a><a name="en-us_topic_0123550104_p170219911618"></a><span id="text4730642777"><a name="text4730642777"></a><a name="text4730642777"></a>Reserved field</span></p>
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
            "metadata": {},
            "volume_id": "5aa119a8-d25b-45a7-8d1b-88e127885635",
            "os-extended-snapshot-attributes:project_id": "0c2eba2c5af04d3f9e9d0d410b371fde",
            "size": 1,
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

