# Querying Failed Tasks<a name="sdrs_05_0901"></a>

## Function<a name="section778722103515"></a>

This API is used to query failed tasks of all protection groups or failed tasks in a specified protection group.

## Constraints and Limitations<a name="section578752118358"></a>

None

## URI<a name="section1478822113513"></a>

-   URI format

    GET /v1/\{project\_id\}/task-center/failure-jobs

-   Parameter description

    <a name="table979182173511"></a>
    <table><thead align="left"><tr id="row148131622173515"><th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.1.5.1.1"><p id="p2813132253518"><a name="p2813132253518"></a><a name="p2813132253518"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.1.5.1.2"><p id="p281362215352"><a name="p281362215352"></a><a name="p281362215352"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.428557144285573%" id="mcps1.1.5.1.3"><p id="p1081332263518"><a name="p1081332263518"></a><a name="p1081332263518"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51494850514948%" id="mcps1.1.5.1.4"><p id="p19813142220351"><a name="p19813142220351"></a><a name="p19813142220351"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row581312226353"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.1.5.1.1 "><p id="p1813172263520"><a name="p1813172263520"></a><a name="p1813172263520"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.1.5.1.2 "><p id="p78131822193520"><a name="p78131822193520"></a><a name="p78131822193520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.428557144285573%" headers="mcps1.1.5.1.3 "><p id="p38131122183510"><a name="p38131122183510"></a><a name="p38131122183510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51494850514948%" headers="mcps1.1.5.1.4 "><p id="p081332213352"><a name="p081332213352"></a><a name="p081332213352"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  field description

    <a name="table136481148235"></a>
    <table><thead align="left"><tr id="row1964611148237"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p16646161412313"><a name="p16646161412313"></a><a name="p16646161412313"></a><strong id="b84235270615443_1"><a name="b84235270615443_1"></a><a name="b84235270615443_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p1164610141234"><a name="p1164610141234"></a><a name="p1164610141234"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p86461214202317"><a name="p86461214202317"></a><a name="p86461214202317"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p3646111412237"><a name="p3646111412237"></a><a name="p3646111412237"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7646111462318"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p8551101016103"><a name="p8551101016103"></a><a name="p8551101016103"></a>failure_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p6646131411233"><a name="p6646131411233"></a><a name="p6646131411233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p96462014202314"><a name="p96462014202314"></a><a name="p96462014202314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p346194021018"><a name="p346194021018"></a><a name="p346194021018"></a>Query the task failure status.</p>
    <a name="ul3102418482"></a><a name="ul3102418482"></a><ul id="ul3102418482"><li><strong id="b1867214571280"><a name="b1867214571280"></a><a name="b1867214571280"></a>createFail</strong>: indicates a creation failure.</li><li><strong id="b1374118586433"><a name="b1374118586433"></a><a name="b1374118586433"></a>deleteFail</strong>: indicates a deletion failure.</li><li><strong id="b1090518479108"><a name="b1090518479108"></a><a name="b1090518479108"></a>attachFail</strong>: indicates an attachment failure.</li><li><strong id="b154111810151112"><a name="b154111810151112"></a><a name="b154111810151112"></a>detachFail</strong>: indicates a detachment failure.</li><li><strong id="b53861423128"><a name="b53861423128"></a><a name="b53861423128"></a>expandFail</strong>: indicates an expansion failure.</li><li><strong id="b12838194813120"><a name="b12838194813120"></a><a name="b12838194813120"></a>resizeFail</strong>: indicates a specification change failure.</li><li><strong id="b1764072612137"><a name="b1764072612137"></a><a name="b1764072612137"></a>startFail</strong>: indicates a protection enabling failure. </li><li><strong id="b6745134112133"><a name="b6745134112133"></a><a name="b6745134112133"></a>stopFail</strong>: indicates a protection disabling failure. </li><li><strong id="b1112013817149"><a name="b1112013817149"></a><a name="b1112013817149"></a>reverseFail</strong>: indicates a planned failover failure.</li><li><strong id="b161043593141"><a name="b161043593141"></a><a name="b161043593141"></a>failoverFail</strong>: indicates a failover failure.</li><li><strong id="b10447722181520"><a name="b10447722181520"></a><a name="b10447722181520"></a>reprotectFail</strong>: indicates a re-protection enabling failure. </li></ul>
    </td>
    </tr>
    <tr id="row14647181422313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p145517105104"><a name="p145517105104"></a><a name="p145517105104"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p20646141482315"><a name="p20646141482315"></a><a name="p20646141482315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p96469140238"><a name="p96469140238"></a><a name="p96469140238"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p34614020101"><a name="p34614020101"></a><a name="p34614020101"></a>Specifies the resource name of a protection group.</p>
    </td>
    </tr>
    <tr id="row964781412317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p05511710131010"><a name="p05511710131010"></a><a name="p05511710131010"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p4647114182312"><a name="p4647114182312"></a><a name="p4647114182312"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p18647141442317"><a name="p18647141442317"></a><a name="p18647141442317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p17248167145112"><a name="p17248167145112"></a><a name="p17248167145112"></a>Specifies the ID of a protection group.</p>
    <p id="p16481833123718"><a name="p16481833123718"></a><a name="p16481833123718"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row26471314102313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p17551010141015"><a name="p17551010141015"></a><a name="p17551010141015"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p164717144233"><a name="p164717144233"></a><a name="p164717144233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p66476149235"><a name="p66476149235"></a><a name="p66476149235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p13462040111018"><a name="p13462040111018"></a><a name="p13462040111018"></a>Specifies the resource type.</p>
    <a name="ul10445051171612"></a><a name="ul10445051171612"></a><ul id="ul10445051171612"><li><strong id="b448864013166"><a name="b448864013166"></a><a name="b448864013166"></a>server_groups</strong>: indicates a protection group.</li><li><strong id="b6278123117182"><a name="b6278123117182"></a><a name="b6278123117182"></a>protected_instances</strong>: indicates a protected instance.</li><li><strong id="b1066174461817"><a name="b1066174461817"></a><a name="b1066174461817"></a>replications</strong>: indicates a replication pair.</li><li><strong id="b9129114151919"><a name="b9129114151919"></a><a name="b9129114151919"></a>disaster_recovery_drills</strong>: indicates a DR drill.</li></ul>
    </td>
    </tr>
    <tr id="row8647314102313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p26471814122310"><a name="p26471814122310"></a><a name="p26471814122310"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p964761452315"><a name="p964761452315"></a><a name="p964761452315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1864761442310"><a name="p1864761442310"></a><a name="p1864761442310"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p171211213522"><a name="p171211213522"></a><a name="p171211213522"></a>Specifies the maximum number of results returned each time.</p>
    <p id="p168455995811"><a name="p168455995811"></a><a name="p168455995811"></a>The value is a positive integer ranging from <strong id="b6013100620539"><a name="b6013100620539"></a><a name="b6013100620539"></a>0</strong> to <strong id="b25293232205313"><a name="b25293232205313"></a><a name="b25293232205313"></a>1000</strong>, and is <strong id="b6520879205318"><a name="b6520879205318"></a><a name="b6520879205318"></a>1000</strong> by default.</p>
    </td>
    </tr>
    <tr id="row564818148231"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p36471414122314"><a name="p36471414122314"></a><a name="p36471414122314"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p1664771482310"><a name="p1664771482310"></a><a name="p1664771482310"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1648171472319"><a name="p1648171472319"></a><a name="p1648171472319"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p412313111528"><a name="p412313111528"></a><a name="p412313111528"></a>Specifies the offset of each request. The default value is <strong id="b74201644142916"><a name="b74201644142916"></a><a name="b74201644142916"></a>0</strong>.</p>
    <p id="p2648201462319"><a name="p2648201462319"></a><a name="p2648201462319"></a>The value must be a number and cannot be negative.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3134948112412"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/task-center/failure-jobs

    GET https://\{Endpoint\}/v1/\{project\_id\}/task-center/failure-jobs?server\_group\_id=XXXXX

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If you do not specify  **filter**  in the request, the system displays failed tasks of the protection group level, such as failed protection group creation or deletion tasks.  
    >-   To query failed tasks in a protection group, specify  **server\_group\_id**  in  **filter**.  


## Response<a name="section11837142115358"></a>

-   Parameter description

    <a name="table12856421203510"></a>
    <table><thead align="left"><tr id="row3815172218357"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1381517225355"><a name="p1381517225355"></a><a name="p1381517225355"></a><strong id="b18830155822219"><a name="b18830155822219"></a><a name="b18830155822219"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p8815132253512"><a name="p8815132253512"></a><a name="p8815132253512"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p781532243513"><a name="p781532243513"></a><a name="p781532243513"></a><strong id="b181761827231"><a name="b181761827231"></a><a name="b181761827231"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18815322123513"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p85771357151815"><a name="p85771357151815"></a><a name="p85771357151815"></a>failure_jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p10815132233511"><a name="p10815132233511"></a><a name="p10815132233511"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p881562243512"><a name="p881562243512"></a><a name="p881562243512"></a>Specifies the list of the failed tasks.</p>
    <p id="p52914521264"><a name="p52914521264"></a><a name="p52914521264"></a>For details, see <a href="#table687013217358">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row08151122193517"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p17577105711818"><a name="p17577105711818"></a><a name="p17577105711818"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p18815322113517"><a name="p18815322113517"></a><a name="p18815322113517"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p18815142219355"><a name="p18815142219355"></a><a name="p18815142219355"></a>Specifies the number of failed tasks in the list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **failure\_jobs**  field description

    <a name="table687013217358"></a>
    <table><thead align="left"><tr id="row58152224359"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p381542263514"><a name="p381542263514"></a><a name="p381542263514"></a><strong id="b2034817382255"><a name="b2034817382255"></a><a name="b2034817382255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p781519229359"><a name="p781519229359"></a><a name="p781519229359"></a><strong id="b95021340162511"><a name="b95021340162511"></a><a name="b95021340162511"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p881532219350"><a name="p881532219350"></a><a name="p881532219350"></a><strong id="b160654116258"><a name="b160654116258"></a><a name="b160654116258"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1281692214358"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p47451737102718"><a name="p47451737102718"></a><a name="p47451737102718"></a>job_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p081622212355"><a name="p081622212355"></a><a name="p081622212355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1118515312812"><a name="p1118515312812"></a><a name="p1118515312812"></a>Specifies the task status.</p>
    <p id="p178168220357"><a name="p178168220357"></a><a name="p178168220357"></a>The value can be <strong id="b839715422511"><a name="b839715422511"></a><a name="b839715422511"></a>FAIL</strong> only in current version.</p>
    <a name="ul85837493015"></a><a name="ul85837493015"></a><ul id="ul85837493015"><li><strong id="b16764963262"><a name="b16764963262"></a><a name="b16764963262"></a>FAIL</strong>: The task failed. </li></ul>
    </td>
    </tr>
    <tr id="row538933343717"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1474519372278"><a name="p1474519372278"></a><a name="p1474519372278"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p12475516274"><a name="p12475516274"></a><a name="p12475516274"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p178160225352"><a name="p178160225352"></a><a name="p178160225352"></a>Specifies the resource ID.</p>
    </td>
    </tr>
    <tr id="row12173164763716"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p474543732713"><a name="p474543732713"></a><a name="p474543732713"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p202502552710"><a name="p202502552710"></a><a name="p202502552710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p28164224351"><a name="p28164224351"></a><a name="p28164224351"></a>Specifies the resource name.</p>
    </td>
    </tr>
    <tr id="row9691159384"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1774503716276"><a name="p1774503716276"></a><a name="p1774503716276"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p3531046102712"><a name="p3531046102712"></a><a name="p3531046102712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p16211535172710"><a name="p16211535172710"></a><a name="p16211535172710"></a>Specifies the resource type.</p>
    <a name="ul4327624142514"></a><a name="ul4327624142514"></a><ul id="ul4327624142514"><li><strong id="b448864013166_1"><a name="b448864013166_1"></a><a name="b448864013166_1"></a>server_groups</strong>: indicates a protection group.</li><li><strong id="b6278123117182_1"><a name="b6278123117182_1"></a><a name="b6278123117182_1"></a>protected_instances</strong>: indicates a protected instance.</li><li><strong id="b1066174461817_1"><a name="b1066174461817_1"></a><a name="b1066174461817_1"></a>replications</strong>: indicates a replication pair.</li><li><strong id="b9129114151919_1"><a name="b9129114151919_1"></a><a name="b9129114151919_1"></a>disaster_recovery_drills</strong>: indicates a DR drill.</li></ul>
    </td>
    </tr>
    <tr id="row51683226381"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1274533772719"><a name="p1274533772719"></a><a name="p1274533772719"></a>failure_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p4541123182720"><a name="p4541123182720"></a><a name="p4541123182720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p981662283512"><a name="p981662283512"></a><a name="p981662283512"></a>Specifies the failed task status.</p>
    <a name="ul11996531259"></a><a name="ul11996531259"></a><ul id="ul11996531259"><li><strong id="b1867214571280_1"><a name="b1867214571280_1"></a><a name="b1867214571280_1"></a>createFail</strong>: indicates a creation failure.</li><li><strong id="b1374118586433_1"><a name="b1374118586433_1"></a><a name="b1374118586433_1"></a>deleteFail</strong>: indicates a deletion failure.</li><li><strong id="b1090518479108_1"><a name="b1090518479108_1"></a><a name="b1090518479108_1"></a>attachFail</strong>: indicates an attachment failure.</li><li><strong id="b154111810151112_1"><a name="b154111810151112_1"></a><a name="b154111810151112_1"></a>detachFail</strong>: indicates a detachment failure.</li><li><strong id="b53861423128_1"><a name="b53861423128_1"></a><a name="b53861423128_1"></a>expandFail</strong>: indicates an expansion failure.</li><li><strong id="b12838194813120_1"><a name="b12838194813120_1"></a><a name="b12838194813120_1"></a>resizeFail</strong>: indicates a specification change failure.</li><li><strong id="b1764072612137_1"><a name="b1764072612137_1"></a><a name="b1764072612137_1"></a>startFail</strong>: indicates a protection enabling failure. </li><li><strong id="b6745134112133_1"><a name="b6745134112133_1"></a><a name="b6745134112133_1"></a>stopFail</strong>: indicates a protection disabling failure. </li><li><strong id="b1112013817149_1"><a name="b1112013817149_1"></a><a name="b1112013817149_1"></a>reverseFail</strong>: indicates a planned failover failure.</li><li><strong id="b161043593141_1"><a name="b161043593141_1"></a><a name="b161043593141_1"></a>failoverFail</strong>: indicates a failover failure.</li><li><strong id="b10447722181520_1"><a name="b10447722181520_1"></a><a name="b10447722181520_1"></a>reprotectFail</strong>: indicates a re-protection enabling failure. </li></ul>
    </td>
    </tr>
    <tr id="row281617220355"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p374510376273"><a name="p374510376273"></a><a name="p374510376273"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p68166224355"><a name="p68166224355"></a><a name="p68166224355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p881620224359"><a name="p881620224359"></a><a name="p881620224359"></a>Specifies the task ID.</p>
    <p id="p3716113214520"><a name="p3716113214520"></a><a name="p3716113214520"></a>This is a returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    <tr id="row662314915372"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p16745153720274"><a name="p16745153720274"></a><a name="p16745153720274"></a>job_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17816172218355"><a name="p17816172218355"></a><a name="p17816172218355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p381611221355"><a name="p381611221355"></a><a name="p381611221355"></a>Specifies the task name.</p>
    </td>
    </tr>
    <tr id="row1081622283516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1374553722718"><a name="p1374553722718"></a><a name="p1374553722718"></a>begin_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1281652283516"><a name="p1281652283516"></a><a name="p1281652283516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p9816182233510"><a name="p9816182233510"></a><a name="p9816182233510"></a>Specifies the task operation time.</p>
    <p id="p64991126142213"><a name="p64991126142213"></a><a name="p64991126142213"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSZ", for example, <strong id="b16889113243016"><a name="b16889113243016"></a><a name="b16889113243016"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row381617220359"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p57456374277"><a name="p57456374277"></a><a name="p57456374277"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p12597515277"><a name="p12597515277"></a><a name="p12597515277"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p19816172220358"><a name="p19816172220358"></a><a name="p19816172220358"></a>Specifies the error code for a failed task.</p>
    </td>
    </tr>
    <tr id="row1740150132615"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p3745537172714"><a name="p3745537172714"></a><a name="p3745537172714"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p626318552714"><a name="p626318552714"></a><a name="p626318552714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1542850192612"><a name="p1542850192612"></a><a name="p1542850192612"></a>Specifies the task failure cause.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "count": 2,
        "failure_jobs": [
            {
                "job_status": "FAIL",
                "resource_id": "17984002-ad8a-438b-8ba6-b850224634c5",
                "resource_name": "Protected-Instance-ab14",
                "resource_type": "protectedInstance",
                "failure_status": "createFail",
                "job_id": "ff808082686f229a0168707beaab014e",
                "job_type": "createProtectedInstance",
                "begin_time": "2019-01-21T12:56:35.754Z",
                "error_code": "EVS.2024",
                "fail_reason": "SdrsGenerateNativeServerParamsTask-fail:volume is error!"
            },
            {
                "job_status": "FAIL",
                "resource_id": "897f57b2-6e94-4179-b414-9532726c59f2",
                "resource_name": "Protected-Instance-5e2e",
                "resource_type": "protectedInstance",
                "failure_status": "createFail",
                "job_id": "ff808082686f229a0168707b9be9013e",
                "job_type": "createProtectedInstance",
                "begin_time": "2019-01-21T12:56:15.591Z",
                "error_code": "EVS.2024",
                "fail_reason": "SdrsGenerateNativeServerParamsTask-fail:volume is error!"
            }
        ]
    }
    ```

    Or

    ```
    {  
          "error": {  
              "message": "XXXX",   
              "code": "XXX"  
          }  
      }
    ```

    In this example,  **error**  represents a general error, including  **badrequest**  \(shown below\) and  **itemNotFound**.

    ```
    {  
          "badrequest": {  
              "message": "XXXX",   
              "code": "XXX"  
          }  
      }
    ```


## **Returned Value**<a name="section897722112352"></a>

-   Normal

    <a name="table398016219357"></a>
    <table><thead align="left"><tr id="row1481842213516"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p2081822243510"><a name="p2081822243510"></a><a name="p2081822243510"></a><strong id="b9310104915293"><a name="b9310104915293"></a><a name="b9310104915293"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p118187225354"><a name="p118187225354"></a><a name="p118187225354"></a><strong id="b1211785016294"><a name="b1211785016294"></a><a name="b1211785016294"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6818112243517"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12824172203511"><a name="p12824172203511"></a><a name="p12824172203511"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1782472243510"><a name="p1782472243510"></a><a name="p1782472243510"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


