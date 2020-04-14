# Querying Details About a VBS Backup \(Native OpenStack V3 API\)<a name="EN-US_TOPIC_0143705537"></a>

## Function<a name="section43395070"></a>

This interface is used to query details about a VBS backup.

## URI<a name="section55011311"></a>

-   URI format

    GET /v3/\{project\_id\}/native/backups/\{backup\_id\}

-   Parameter description

    <a name="table40072161"></a>
    <table><thead align="left"><tr id="row65282360"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p53379839"><a name="p53379839"></a><a name="p53379839"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p28799665"><a name="p28799665"></a><a name="p28799665"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p51071544"><a name="p51071544"></a><a name="p51071544"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43154428"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p5847780"><a name="p5847780"></a><a name="p5847780"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3908185"><a name="p3908185"></a><a name="p3908185"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row30494806"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p54160201"><a name="p54160201"></a><a name="p54160201"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p24900132"><a name="p24900132"></a><a name="p24900132"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3644816"><a name="p3644816"></a><a name="p3644816"></a>Backup ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25339754"></a>

None

## Response<a name="section26731201"></a>

-   Parameter description

    <a name="table37188714202639"></a>
    <table><thead align="left"><tr id="row47408137202639"><th class="cellrowborder" valign="top" width="26.090000000000003%" id="mcps1.1.4.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.4.1.2"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.43%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6386244717728"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p547572317728"><a name="p547572317728"></a><a name="p547572317728"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2919188817731"><a name="p2919188817731"></a><a name="p2919188817731"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1573275017731"><a name="p1573275017731"></a><a name="p1573275017731"></a>List of queried backups</p>
    </td>
    </tr>
    <tr id="row34898119202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p8175394202639"><a name="p8175394202639"></a><a name="p8175394202639"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p4498910316552"><a name="p4498910316552"></a><a name="p4498910316552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p18778941202639"><a name="p18778941202639"></a><a name="p18778941202639"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row34792741202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p66748598202639"><a name="p66748598202639"></a><a name="p66748598202639"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2023868816552"><a name="p2023868816552"></a><a name="p2023868816552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p52216658202639"><a name="p52216658202639"></a><a name="p52216658202639"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row187880202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p15218330202639"><a name="p15218330202639"></a><a name="p15218330202639"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2872102616552"><a name="p2872102616552"></a><a name="p2872102616552"></a>list&lt;link&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p56587500202639"><a name="p56587500202639"></a><a name="p56587500202639"></a>Backup URL</p>
    </td>
    </tr>
    <tr id="row39525457202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p47445438202639"><a name="p47445438202639"></a><a name="p47445438202639"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p4470175616552"><a name="p4470175616552"></a><a name="p4470175616552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p38609241202639"><a name="p38609241202639"></a><a name="p38609241202639"></a>AZ where the backup resides</p>
    </td>
    </tr>
    <tr id="row11938854202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p27523095202639"><a name="p27523095202639"></a><a name="p27523095202639"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p6407250316552"><a name="p6407250316552"></a><a name="p6407250316552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p56187888202639"><a name="p56187888202639"></a><a name="p56187888202639"></a>Source disk ID of the backup</p>
    </td>
    </tr>
    <tr id="row35928950202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p24563814202639"><a name="p24563814202639"></a><a name="p24563814202639"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2249026716552"><a name="p2249026716552"></a><a name="p2249026716552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p34805200202639"><a name="p34805200202639"></a><a name="p34805200202639"></a>Cause of the backup failure</p>
    </td>
    </tr>
    <tr id="row44811352202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p5840881202639"><a name="p5840881202639"></a><a name="p5840881202639"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p977230216552"><a name="p977230216552"></a><a name="p977230216552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p2861985202639"><a name="p2861985202639"></a><a name="p2861985202639"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row25757867202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p6012487202639"><a name="p6012487202639"></a><a name="p6012487202639"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p5335903516552"><a name="p5335903516552"></a><a name="p5335903516552"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p55027024202639"><a name="p55027024202639"></a><a name="p55027024202639"></a>Backup size</p>
    </td>
    </tr>
    <tr id="row25481174202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p50709247202639"><a name="p50709247202639"></a><a name="p50709247202639"></a>object_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2711456816552"><a name="p2711456816552"></a><a name="p2711456816552"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p44734422202639"><a name="p44734422202639"></a><a name="p44734422202639"></a>Number of objects on OBS for the disk data</p>
    </td>
    </tr>
    <tr id="row67065481202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p63594872202639"><a name="p63594872202639"></a><a name="p63594872202639"></a>container</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p4879638116552"><a name="p4879638116552"></a><a name="p4879638116552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p30152945202639"><a name="p30152945202639"></a><a name="p30152945202639"></a>Container of the backup</p>
    </td>
    </tr>
    <tr id="row2941050202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p36898458202639"><a name="p36898458202639"></a><a name="p36898458202639"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p6019280316552"><a name="p6019280316552"></a><a name="p6019280316552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p29111527202639"><a name="p29111527202639"></a><a name="p29111527202639"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row60677159202639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p15902866202639"><a name="p15902866202639"></a><a name="p15902866202639"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p4377888116552"><a name="p4377888116552"></a><a name="p4377888116552"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p51533385202639"><a name="p51533385202639"></a><a name="p51533385202639"></a>Backup creation time</p>
    </td>
    </tr>
    <tr id="row154691563498"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p9167854191913"><a name="p9167854191913"></a><a name="p9167854191913"></a>os-backup-project-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p194701566492"><a name="p194701566492"></a><a name="p194701566492"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1470166164917"><a name="p1470166164917"></a><a name="p1470166164917"></a>ID of the project that owns the VBS backup</p>
    </td>
    </tr>
    <tr id="row3290306118630"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p1654496218646"><a name="p1654496218646"></a><a name="p1654496218646"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p3646434918646"><a name="p3646434918646"></a><a name="p3646434918646"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p82229918646"><a name="p82229918646"></a><a name="p82229918646"></a>Update time of the backup</p>
    </td>
    </tr>
    <tr id="row1506423518633"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p6258577818646"><a name="p6258577818646"></a><a name="p6258577818646"></a>data_timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p5325972318646"><a name="p5325972318646"></a><a name="p5325972318646"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1907033518646"><a name="p1907033518646"></a><a name="p1907033518646"></a>Current time</p>
    </td>
    </tr>
    <tr id="row1051881618636"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p1073973218646"><a name="p1073973218646"></a><a name="p1073973218646"></a>has_dependent_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p6618937718646"><a name="p6618937718646"></a><a name="p6618937718646"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p5973930018646"><a name="p5973930018646"></a><a name="p5973930018646"></a>Whether a dependent backup exists</p>
    </td>
    </tr>
    <tr id="row6544466318639"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p6340593118646"><a name="p6340593118646"></a><a name="p6340593118646"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p6558038218646"><a name="p6558038218646"></a><a name="p6558038218646"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1041074618646"><a name="p1041074618646"></a><a name="p1041074618646"></a>ID of the snapshot associated with the backup</p>
    </td>
    </tr>
    <tr id="row2126056418643"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p613286418646"><a name="p613286418646"></a><a name="p613286418646"></a>is_incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p3951169318646"><a name="p3951169318646"></a><a name="p3951169318646"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p4633055618646"><a name="p4633055618646"></a><a name="p4633055618646"></a>Whether the backup is an incremental backup</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **description**  parameter description

    <a name="table10930121323510"></a>
    <table><thead align="left"><tr id="row59421013153511"><th class="cellrowborder" valign="top" width="26.090000000000003%" id="mcps1.1.4.1.1"><p id="p9947413163511"><a name="p9947413163511"></a><a name="p9947413163511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.4.1.2"><p id="p495361316355"><a name="p495361316355"></a><a name="p495361316355"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.43%" id="mcps1.1.4.1.3"><p id="p29555136354"><a name="p29555136354"></a><a name="p29555136354"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59596134354"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p115025378354"><a name="p115025378354"></a><a name="p115025378354"></a>DESC</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p8502133733515"><a name="p8502133733515"></a><a name="p8502133733515"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p7501163716354"><a name="p7501163716354"></a><a name="p7501163716354"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row16500123383518"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p174991237103512"><a name="p174991237103512"></a><a name="p174991237103512"></a>INC</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p949823716356"><a name="p949823716356"></a><a name="p949823716356"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p149653783520"><a name="p149653783520"></a><a name="p149653783520"></a>Specifies whether the backup is an incremental backup. <strong id="b11548122111319"><a name="b11548122111319"></a><a name="b11548122111319"></a>1</strong>: incremental backup; <strong id="b1554852118319"><a name="b1554852118319"></a><a name="b1554852118319"></a>0</strong>: full backup</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **link**  parameter description

    <a name="table1250162313409"></a>
    <table><thead align="left"><tr id="row14501623194017"><th class="cellrowborder" valign="top" width="26.090000000000003%" id="mcps1.1.4.1.1"><p id="p14501523144012"><a name="p14501523144012"></a><a name="p14501523144012"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.4.1.2"><p id="p155013237408"><a name="p155013237408"></a><a name="p155013237408"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.43%" id="mcps1.1.4.1.3"><p id="p10501202364011"><a name="p10501202364011"></a><a name="p10501202364011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1750115239406"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p7598203354019"><a name="p7598203354019"></a><a name="p7598203354019"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p9598633104015"><a name="p9598633104015"></a><a name="p9598633104015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p4598133313404"><a name="p4598133313404"></a><a name="p4598133313404"></a>Specifies that the URL of the last backup queried.</p>
    </td>
    </tr>
    <tr id="row5502172319407"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p559918335401"><a name="p559918335401"></a><a name="p559918335401"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p10599173319404"><a name="p10599173319404"></a><a name="p10599173319404"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p165991533174010"><a name="p165991533174010"></a><a name="p165991533174010"></a>Relationship between the query result and <strong id="b143271029123112"><a name="b143271029123112"></a><a name="b143271029123112"></a>href</strong>. The value <strong id="b133271929163112"><a name="b133271929163112"></a><a name="b133271929163112"></a>next</strong> indicates that some backups are not obtained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    	"backup": {
    		"status": "error",
    		"description": null,
    		"links": [{
    			"href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    			"rel": "self"
    		},
    		{
    			"href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    			"rel": "bookmark"
    		}],
    		"availability_zone": null,
    		"volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024",
    		"fail_reason": "Connection to swift failed: [Errno 111] ECONNREFUSED",
    		"id": "1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    		"size": 1,
    		"object_count": null,
    		"container": "volumebackups",
    		"name": null,
    		"created_at": "2013-06-27T08:48:03.000000",
    		"os-backup-project-attr:project_id": "b23b579f08c84228b9b4673c46f0c442",
    		"snapshot_id": "66a574c0-4415-499e-b0b1-3f340d7f7932",
    		"updated_at": "2019-03-27T12:36:17.596602",
    		"data_timestamp": "2019-03-16T11:56:00.917245",
    		"has_dependent_backups": false,
    		"is_incremental": false
    	}
    }
    ```


## Status Codes<a name="section39254219"></a>

-   Normal

    200

-   Abnormal

    <a name="table5304616203321"></a>
    <table><thead align="left"><tr id="row35243530203321"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p36153654203321"><a name="p36153654203321"></a><a name="p36153654203321"></a>Status Codes</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p42764887203321"><a name="p42764887203321"></a><a name="p42764887203321"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41403861203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p65378455203321"><a name="p65378455203321"></a><a name="p65378455203321"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p61163526203321"><a name="p61163526203321"></a><a name="p61163526203321"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row13600825203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27925078203321"><a name="p27925078203321"></a><a name="p27925078203321"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p47338835203321"><a name="p47338835203321"></a><a name="p47338835203321"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row23396333203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16054814203321"><a name="p16054814203321"></a><a name="p16054814203321"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p25371523203321"><a name="p25371523203321"></a><a name="p25371523203321"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row27017116203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40902827203321"><a name="p40902827203321"></a><a name="p40902827203321"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p24794723203321"><a name="p24794723203321"></a><a name="p24794723203321"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row21825917203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23068868203321"><a name="p23068868203321"></a><a name="p23068868203321"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p56639048203321"><a name="p56639048203321"></a><a name="p56639048203321"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row39989388203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17914997203321"><a name="p17914997203321"></a><a name="p17914997203321"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p41828687203321"><a name="p41828687203321"></a><a name="p41828687203321"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row40913870203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25689172203321"><a name="p25689172203321"></a><a name="p25689172203321"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p448158203321"><a name="p448158203321"></a><a name="p448158203321"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row4033424203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p58271932203321"><a name="p58271932203321"></a><a name="p58271932203321"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p22406048203321"><a name="p22406048203321"></a><a name="p22406048203321"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row327847203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p26555667203321"><a name="p26555667203321"></a><a name="p26555667203321"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3525452203321"><a name="p3525452203321"></a><a name="p3525452203321"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row31729073203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19918087203321"><a name="p19918087203321"></a><a name="p19918087203321"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2752350203321"><a name="p2752350203321"></a><a name="p2752350203321"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row24771153203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p60306380203321"><a name="p60306380203321"></a><a name="p60306380203321"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p52978587203321"><a name="p52978587203321"></a><a name="p52978587203321"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row7045238203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p33793375203321"><a name="p33793375203321"></a><a name="p33793375203321"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p52908816203321"><a name="p52908816203321"></a><a name="p52908816203321"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row6417299203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50039236203321"><a name="p50039236203321"></a><a name="p50039236203321"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26646354203321"><a name="p26646354203321"></a><a name="p26646354203321"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row38490599203321"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30730827203321"><a name="p30730827203321"></a><a name="p30730827203321"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6169022203321"><a name="p6169022203321"></a><a name="p6169022203321"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

