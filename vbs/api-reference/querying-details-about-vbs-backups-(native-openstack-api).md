# Querying Details About VBS Backups \(Native OpenStack API\)<a name="EN-US_TOPIC_0020237259"></a>

## Function<a name="section38423121"></a>

This interface is used to query the details about VBS backups.

## URI<a name="section10263773"></a>

-   URI format

    GET /v2/\{project\_id\}/backups/detail

-   Parameter description

    <a name="table32325424"></a>
    <table><thead align="left"><tr id="row59286834"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p37504268"><a name="p37504268"></a><a name="p37504268"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p17946858"><a name="p17946858"></a><a name="p17946858"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p44409397"><a name="p44409397"></a><a name="p44409397"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40391380"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p50476336"><a name="p50476336"></a><a name="p50476336"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p62051376"><a name="p62051376"></a><a name="p62051376"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Request filter**  parameter description

    <a name="table37332024155045"></a>
    <table><thead align="left"><tr id="row20772680155045"><th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.34%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.209999999999994%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56787744155045"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p36404558155045"><a name="p36404558155045"></a><a name="p36404558155045"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p63088125155045"><a name="p63088125155045"></a><a name="p63088125155045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p9864533155045"><a name="p9864533155045"></a><a name="p9864533155045"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p60829693155045"><a name="p60829693155045"></a><a name="p60829693155045"></a>Name of the backup to be queried. This parameter is used to query the backups whose names are specified character strings.</p>
    </td>
    </tr>
    <tr id="row10596326155045"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p52996106155045"><a name="p52996106155045"></a><a name="p52996106155045"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p64826194155045"><a name="p64826194155045"></a><a name="p64826194155045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p16430375155045"><a name="p16430375155045"></a><a name="p16430375155045"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p55791984155045"><a name="p55791984155045"></a><a name="p55791984155045"></a>Status of the backup to be queried. This parameter is used to query the backups in a specified state. The value can be <span class="parmvalue" id="parmvalue24916195101729"><a name="parmvalue24916195101729"></a><a name="parmvalue24916195101729"></a><b>available</b></span>, <span class="parmvalue" id="parmvalue22919169101729"><a name="parmvalue22919169101729"></a><a name="parmvalue22919169101729"></a><b>error</b></span>, <span class="parmvalue" id="parmvalue4945935101729"><a name="parmvalue4945935101729"></a><a name="parmvalue4945935101729"></a><b>restoring</b></span>, <span class="parmvalue" id="parmvalue44513423101729"><a name="parmvalue44513423101729"></a><a name="parmvalue44513423101729"></a><b>creating</b></span>, <span class="parmvalue" id="parmvalue65076488101729"><a name="parmvalue65076488101729"></a><a name="parmvalue65076488101729"></a><b>deleting</b></span>, or <span class="parmvalue" id="parmvalue48817485101729"><a name="parmvalue48817485101729"></a><a name="parmvalue48817485101729"></a><b>error_deleting</b></span>.</p>
    </td>
    </tr>
    <tr id="row098791912487"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p1098715193486"><a name="p1098715193486"></a><a name="p1098715193486"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p1198841974818"><a name="p1198841974818"></a><a name="p1198841974818"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p186705308494"><a name="p186705308494"></a><a name="p186705308494"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p119882199481"><a name="p119882199481"></a><a name="p119882199481"></a>Sorts by attribute. Possible values are <strong id="b6825152514612"><a name="b6825152514612"></a><a name="b6825152514612"></a>name</strong>, <strong id="b103497281868"><a name="b103497281868"></a><a name="b103497281868"></a>status</strong>, <strong id="b145897321769"><a name="b145897321769"></a><a name="b145897321769"></a>container_format</strong>, <strong id="b147751234263"><a name="b147751234263"></a><a name="b147751234263"></a>disk_format</strong>, <strong id="b18773391565"><a name="b18773391565"></a><a name="b18773391565"></a>size</strong>, <strong id="b13396141465"><a name="b13396141465"></a><a name="b13396141465"></a>id</strong>, <strong id="b11185194511619"><a name="b11185194511619"></a><a name="b11185194511619"></a>created_at</strong>, and <strong id="b46031448663"><a name="b46031448663"></a><a name="b46031448663"></a>updated_at</strong>. The default value is <strong id="b155782582062"><a name="b155782582062"></a><a name="b155782582062"></a>created_at</strong>. This API uses the natural sort direction of the <strong id="b28682579717"><a name="b28682579717"></a><a name="b28682579717"></a>sort_key</strong> attribute.</p>
    </td>
    </tr>
    <tr id="row132476231482"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p653220411497"><a name="p653220411497"></a><a name="p653220411497"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p424710236484"><a name="p424710236484"></a><a name="p424710236484"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p11193931204919"><a name="p11193931204919"></a><a name="p11193931204919"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p324716231485"><a name="p324716231485"></a><a name="p324716231485"></a>Sorts by a set of one or more sort direction and attribute (<strong id="b13143112111459"><a name="b13143112111459"></a><a name="b13143112111459"></a>sort_key</strong>) combinations. If you omit the sort direction in a set, the value defaults to <strong id="b2237181281216"><a name="b2237181281216"></a><a name="b2237181281216"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="row32365812155045"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p4385095155045"><a name="p4385095155045"></a><a name="p4385095155045"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p19648386155045"><a name="p19648386155045"></a><a name="p19648386155045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p48015438155045"><a name="p48015438155045"></a><a name="p48015438155045"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p64045266155045"><a name="p64045266155045"></a><a name="p64045266155045"></a>Offset of the queried information</p>
    </td>
    </tr>
    <tr id="row39536489155045"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p48339061155045"><a name="p48339061155045"></a><a name="p48339061155045"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p23149902155045"><a name="p23149902155045"></a><a name="p23149902155045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p63202779155045"><a name="p63202779155045"></a><a name="p63202779155045"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p19151493155045"><a name="p19151493155045"></a><a name="p19151493155045"></a>Maximum number of query results that can be returned</p>
    </td>
    </tr>
    <tr id="row5614570164116"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p4498303164118"><a name="p4498303164118"></a><a name="p4498303164118"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p28818245164118"><a name="p28818245164118"></a><a name="p28818245164118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p52576545164118"><a name="p52576545164118"></a><a name="p52576545164118"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p30841720164118"><a name="p30841720164118"></a><a name="p30841720164118"></a>Disk ID of the backup to be queried. It is used to query the backups for specific disks.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET /v2/{project_id}/backups/detail?name=backup&status=error&limit=10&volume_id=7d7c6fbe-d7ee-4b4d-8bae-bdd08b5604bb
    ```


## Request<a name="section25265097"></a>

None

## Response<a name="section26059286"></a>

-   Parameter description

    <a name="table48234446202619"></a>
    <table><thead align="left"><tr id="row55367383202619"><th class="cellrowborder" valign="top" width="28.74%" id="mcps1.1.4.1.1"><p id="p9816113115130"><a name="p9816113115130"></a><a name="p9816113115130"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.39%" id="mcps1.1.4.1.2"><p id="p148161731141319"><a name="p148161731141319"></a><a name="p148161731141319"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.87%" id="mcps1.1.4.1.3"><p id="p138168311139"><a name="p138168311139"></a><a name="p138168311139"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5405314117637"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p1622830017637"><a name="p1622830017637"></a><a name="p1622830017637"></a>backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p388999251771"><a name="p388999251771"></a><a name="p388999251771"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p638861871771"><a name="p638861871771"></a><a name="p638861871771"></a>List of queried backups</p>
    </td>
    </tr>
    <tr id="row63899507202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p8477569202619"><a name="p8477569202619"></a><a name="p8477569202619"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p3812946216349"><a name="p3812946216349"></a><a name="p3812946216349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p55194315202619"><a name="p55194315202619"></a><a name="p55194315202619"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row26986790202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p38446351202619"><a name="p38446351202619"></a><a name="p38446351202619"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p147871316349"><a name="p147871316349"></a><a name="p147871316349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p51398114202619"><a name="p51398114202619"></a><a name="p51398114202619"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row59929844202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p22479234202619"><a name="p22479234202619"></a><a name="p22479234202619"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p5266693716349"><a name="p5266693716349"></a><a name="p5266693716349"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p48084179202619"><a name="p48084179202619"></a><a name="p48084179202619"></a>Backup URL</p>
    </td>
    </tr>
    <tr id="row30104430202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p22539803202619"><a name="p22539803202619"></a><a name="p22539803202619"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p3816348516349"><a name="p3816348516349"></a><a name="p3816348516349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p42822461202619"><a name="p42822461202619"></a><a name="p42822461202619"></a>AZ where the backup resides</p>
    </td>
    </tr>
    <tr id="row49857835202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p11952800202619"><a name="p11952800202619"></a><a name="p11952800202619"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p3926917816420"><a name="p3926917816420"></a><a name="p3926917816420"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p39169096202619"><a name="p39169096202619"></a><a name="p39169096202619"></a>Source disk ID of the backup</p>
    </td>
    </tr>
    <tr id="row16977544202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p33003808202619"><a name="p33003808202619"></a><a name="p33003808202619"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p1551126516414"><a name="p1551126516414"></a><a name="p1551126516414"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p44790369202619"><a name="p44790369202619"></a><a name="p44790369202619"></a>Cause of the backup failure</p>
    </td>
    </tr>
    <tr id="row460141202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p37271474202619"><a name="p37271474202619"></a><a name="p37271474202619"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p6707960416349"><a name="p6707960416349"></a><a name="p6707960416349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p60551425202619"><a name="p60551425202619"></a><a name="p60551425202619"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row8091914202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p51465269202619"><a name="p51465269202619"></a><a name="p51465269202619"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p6473887516349"><a name="p6473887516349"></a><a name="p6473887516349"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p38938725202619"><a name="p38938725202619"></a><a name="p38938725202619"></a>Backup size</p>
    </td>
    </tr>
    <tr id="row14904212202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p66390544202619"><a name="p66390544202619"></a><a name="p66390544202619"></a>object_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p935748516349"><a name="p935748516349"></a><a name="p935748516349"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p51837782202619"><a name="p51837782202619"></a><a name="p51837782202619"></a>Number of objects on Object Storage Service (OBS) for the disk data</p>
    </td>
    </tr>
    <tr id="row63886860202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p7453171202619"><a name="p7453171202619"></a><a name="p7453171202619"></a>container</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p1975883616349"><a name="p1975883616349"></a><a name="p1975883616349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p45004514202619"><a name="p45004514202619"></a><a name="p45004514202619"></a>Container of the backup</p>
    </td>
    </tr>
    <tr id="row2387448202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p59165588202619"><a name="p59165588202619"></a><a name="p59165588202619"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p5696191216349"><a name="p5696191216349"></a><a name="p5696191216349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p27753504202619"><a name="p27753504202619"></a><a name="p27753504202619"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row48454951202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p32536945202619"><a name="p32536945202619"></a><a name="p32536945202619"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p5051216016349"><a name="p5051216016349"></a><a name="p5051216016349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p1604592202619"><a name="p1604592202619"></a><a name="p1604592202619"></a>Backup creation time</p>
    </td>
    </tr>
    <tr id="row436163494914"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p148191537181410"><a name="p148191537181410"></a><a name="p148191537181410"></a>os-bak-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p7972235194916"><a name="p7972235194916"></a><a name="p7972235194916"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p12972133513498"><a name="p12972133513498"></a><a name="p12972133513498"></a>ID of the project that owns the VBS backup</p>
    </td>
    </tr>
    <tr id="row14441328202619"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p28896915202619"><a name="p28896915202619"></a><a name="p28896915202619"></a>service_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p6495317316349"><a name="p6495317316349"></a><a name="p6495317316349"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p10122423202619"><a name="p10122423202619"></a><a name="p10122423202619"></a>Backup metadata</p>
    </td>
    </tr>
    <tr id="row4023893017450"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p1675189817462"><a name="p1675189817462"></a><a name="p1675189817462"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p5199816317462"><a name="p5199816317462"></a><a name="p5199816317462"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p5110169017462"><a name="p5110169017462"></a><a name="p5110169017462"></a>Time when the backup was updated</p>
    </td>
    </tr>
    <tr id="row587809217458"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p51017140174631"><a name="p51017140174631"></a><a name="p51017140174631"></a>data_timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p51551297174631"><a name="p51551297174631"></a><a name="p51551297174631"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p14905520174631"><a name="p14905520174631"></a><a name="p14905520174631"></a>Current time</p>
    </td>
    </tr>
    <tr id="row5551782717455"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p47171598175250"><a name="p47171598175250"></a><a name="p47171598175250"></a>has_dependent_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p53882996175250"><a name="p53882996175250"></a><a name="p53882996175250"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p2446587175250"><a name="p2446587175250"></a><a name="p2446587175250"></a>Whether a dependent backup exists. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row2950474175228"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p38731483175250"><a name="p38731483175250"></a><a name="p38731483175250"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p43102204175250"><a name="p43102204175250"></a><a name="p43102204175250"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p1617637175250"><a name="p1617637175250"></a><a name="p1617637175250"></a>ID of the snapshot associated with the backup</p>
    </td>
    </tr>
    <tr id="row46058702175233"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p38407358175250"><a name="p38407358175250"></a><a name="p38407358175250"></a>is_incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p64003470175250"><a name="p64003470175250"></a><a name="p64003470175250"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p16898564175250"><a name="p16898564175250"></a><a name="p16898564175250"></a>Whether the backup is an incremental backup. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row4426806101854"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p1422124714456"><a name="p1422124714456"></a><a name="p1422124714456"></a>backups_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p2428687314456"><a name="p2428687314456"></a><a name="p2428687314456"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p2107967814456"><a name="p2107967814456"></a><a name="p2107967814456"></a>Specifies that only part of a tenant's backup information is queried, such as query by page with the limit table specified and when the number of backups exceeds 1000.</p>
    </td>
    </tr>
    <tr id="row554657171454"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p6626476114456"><a name="p6626476114456"></a><a name="p6626476114456"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p604027431454"><a name="p604027431454"></a><a name="p604027431454"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p607840521454"><a name="p607840521454"></a><a name="p607840521454"></a>Specifies that the URL of the last backup is queried.</p>
    </td>
    </tr>
    <tr id="row1549701514553"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p4729870714553"><a name="p4729870714553"></a><a name="p4729870714553"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p1543247614553"><a name="p1543247614553"></a><a name="p1543247614553"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p4207106614553"><a name="p4207106614553"></a><a name="p4207106614553"></a>Relationship between the query result and <strong id="b842352706202944"><a name="b842352706202944"></a><a name="b842352706202944"></a>href.</strong> The value <strong id="b1636101139174441"><a name="b1636101139174441"></a><a name="b1636101139174441"></a>next</strong> indicates that some backups are not obtained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **service\_metadata**  parameter description

    <a name="table1037654820140"></a>
    <table><thead align="left"><tr id="row738274810147"><th class="cellrowborder" valign="top" width="26.090000000000003%" id="mcps1.1.4.1.1"><p id="p1038584831413"><a name="p1038584831413"></a><a name="p1038584831413"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.4.1.2"><p id="p5388174816141"><a name="p5388174816141"></a><a name="p5388174816141"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.43%" id="mcps1.1.4.1.3"><p id="p0392144819146"><a name="p0392144819146"></a><a name="p0392144819146"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9394548131410"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p5396184818142"><a name="p5396184818142"></a><a name="p5396184818142"></a>DL</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p15399164817145"><a name="p15399164817145"></a><a name="p15399164817145"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1540134821414"><a name="p1540134821414"></a><a name="p1540134821414"></a><strong id="b1883017264192"><a name="b1883017264192"></a><a name="b1883017264192"></a>0</strong>: non-deduplication and non-compression; <strong id="b142166218198"><a name="b142166218198"></a><a name="b142166218198"></a>1</strong>: deduplication and non-compression; <strong id="b15128132531917"><a name="b15128132531917"></a><a name="b15128132531917"></a>2</strong>: non-deduplication and compression; <strong id="b14302192919191"><a name="b14302192919191"></a><a name="b14302192919191"></a>3</strong>: deduplication and compression If this key is not specified, the value is 0 (non-deduplication and non-compression).</p>
    </td>
    </tr>
    <tr id="row94031648131410"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p1040514821415"><a name="p1040514821415"></a><a name="p1040514821415"></a>VK</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p2408448151415"><a name="p2408448151415"></a><a name="p2408448151415"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p7949104222620"><a name="p7949104222620"></a><a name="p7949104222620"></a>Specifies the encryption VK of an encrypted volume. The value is a string of 64 characters.</p>
    </td>
    </tr>
    <tr id="row64111148161411"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p114136486148"><a name="p114136486148"></a><a name="p114136486148"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p144151748181415"><a name="p144151748181415"></a><a name="p144151748181415"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p104187485142"><a name="p104187485142"></a><a name="p104187485142"></a>Specifies whether the disk is the boot disk.</p>
    </td>
    </tr>
    <tr id="row541984861411"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p19420174812149"><a name="p19420174812149"></a><a name="p19420174812149"></a>backupurl</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p1676418182174"><a name="p1676418182174"></a><a name="p1676418182174"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p4424114851411"><a name="p4424114851411"></a><a name="p4424114851411"></a>Specifies the backup image ID on the backup system.</p>
    </td>
    </tr>
    <tr id="row03821658101519"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p13851858181514"><a name="p13851858181514"></a><a name="p13851858181514"></a>SP</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p113852587150"><a name="p113852587150"></a><a name="p113852587150"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1158282184118"><a name="p1158282184118"></a><a name="p1158282184118"></a>Specifies the path name of the backup image in the storage unit.</p>
    </td>
    </tr>
    <tr id="row116119111162"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p61614115165"><a name="p61614115165"></a><a name="p61614115165"></a>VMID</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p016111119169"><a name="p016111119169"></a><a name="p016111119169"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p816218117162"><a name="p816218117162"></a><a name="p816218117162"></a>Specifies the ID of the VM to which the backup image belongs.</p>
    </td>
    </tr>
    <tr id="row179902621610"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p1065015891711"><a name="p1065015891711"></a><a name="p1065015891711"></a>ST</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p89901621617"><a name="p89901621617"></a><a name="p89901621617"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p10990661166"><a name="p10990661166"></a><a name="p10990661166"></a>Specifies the backup service type. <strong id="b131529101718"><a name="b131529101718"></a><a name="b131529101718"></a>0</strong>: disk backup; <strong id="b712412322176"><a name="b712412322176"></a><a name="b712412322176"></a>1</strong>: VM backup; <strong id="b119811533121716"><a name="b119811533121716"></a><a name="b119811533121716"></a>4</strong>: disk backup copy, <strong id="b19271836151710"><a name="b19271836151710"></a><a name="b19271836151710"></a>5</strong>: VM backup copy. If this tag does not exist, disk backup is specified.</p>
    </td>
    </tr>
    <tr id="row1990763169"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p8990566167"><a name="p8990566167"></a><a name="p8990566167"></a>BT</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p49901666161"><a name="p49901666161"></a><a name="p49901666161"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1899017601613"><a name="p1899017601613"></a><a name="p1899017601613"></a>Specifies the backup storage type.</p>
    </td>
    </tr>
    <tr id="row137111118161"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p13791120169"><a name="p13791120169"></a><a name="p13791120169"></a>SS</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p537611141610"><a name="p537611141610"></a><a name="p537611141610"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p93711113169"><a name="p93711113169"></a><a name="p93711113169"></a>Specifies the space saving rate.</p>
    </td>
    </tr>
    <tr id="row737911191619"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p937121151618"><a name="p937121151618"></a><a name="p937121151618"></a>BP</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p43771117167"><a name="p43771117167"></a><a name="p43771117167"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p74481998308"><a name="p74481998308"></a><a name="p74481998308"></a>Specifies the storage unit path.</p>
    </td>
    </tr>
    <tr id="row23761171615"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p203711161610"><a name="p203711161610"></a><a name="p203711161610"></a>CMKID</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p037101113163"><a name="p037101113163"></a><a name="p037101113163"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p937101121615"><a name="p937101121615"></a><a name="p937101121615"></a>Specifies the CMKID of an encrypted volume. The content is UUID and contains 36 characters.</p>
    </td>
    </tr>
    <tr id="row33731112164"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p113741119161"><a name="p113741119161"></a><a name="p113741119161"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p133713114166"><a name="p133713114166"></a><a name="p133713114166"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p11371118164"><a name="p11371118164"></a><a name="p11371118164"></a>Specifies the backup progress.</p>
    </td>
    </tr>
    <tr id="row19786843181812"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p6786154341819"><a name="p6786154341819"></a><a name="p6786154341819"></a>CS</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p17786143141812"><a name="p17786143141812"></a><a name="p17786143141812"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1578624314182"><a name="p1578624314182"></a><a name="p1578624314182"></a>Specifies the total backup data of the chain where the backup is located. The unit is MB.</p>
    </td>
    </tr>
    <tr id="row117869430183"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p578684314188"><a name="p578684314188"></a><a name="p578684314188"></a>VT</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p197869431189"><a name="p197869431189"></a><a name="p197869431189"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1878618438185"><a name="p1878618438185"></a><a name="p1878618438185"></a>Specifies the production storage disk type.</p>
    </td>
    </tr>
    <tr id="row178694318186"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p197861443131814"><a name="p197861443131814"></a><a name="p197861443131814"></a>OMID</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p37861143191816"><a name="p37861143191816"></a><a name="p37861143191816"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p5786124315184"><a name="p5786124315184"></a><a name="p5786124315184"></a>Specifies the host ID of the job execution node.</p>
    </td>
    </tr>
    <tr id="row1578634301813"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p127861243151811"><a name="p127861243151811"></a><a name="p127861243151811"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p10786194320185"><a name="p10786194320185"></a><a name="p10786194320185"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p12786164315186"><a name="p12786164315186"></a><a name="p12786164315186"></a>Specifies the backup type. <strong id="b15716111274919"><a name="b15716111274919"></a><a name="b15716111274919"></a>1</strong>: full backup; <strong id="b15725912114916"><a name="b15725912114916"></a><a name="b15725912114916"></a>0</strong>: incremental backup</p>
    </td>
    </tr>
    <tr id="row6786743181818"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p27877438187"><a name="p27877438187"></a><a name="p27877438187"></a>ebk_T_I</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p19787164310183"><a name="p19787164310183"></a><a name="p19787164310183"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p1019923311356"><a name="p1019923311356"></a><a name="p1019923311356"></a>Specifies the job ID of the backup system.</p>
    </td>
    </tr>
    <tr id="row57871543201820"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p27878437188"><a name="p27878437188"></a><a name="p27878437188"></a>AT</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p1478718431186"><a name="p1478718431186"></a><a name="p1478718431186"></a>float</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p378794361812"><a name="p378794361812"></a><a name="p378794361812"></a>Specifies the average rate (Average Throughput). The unit is MB/s. One digit is reserved after the decimal point.</p>
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
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p7501163716354"><a name="p7501163716354"></a><a name="p7501163716354"></a>Describes the backup.</p>
    </td>
    </tr>
    <tr id="row16500123383518"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p174991237103512"><a name="p174991237103512"></a><a name="p174991237103512"></a>INC</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p949823716356"><a name="p949823716356"></a><a name="p949823716356"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p149653783520"><a name="p149653783520"></a><a name="p149653783520"></a>Specifies whether the backup is an incremental backup. <strong id="b22041344141714"><a name="b22041344141714"></a><a name="b22041344141714"></a>1</strong>: incremental backup; <strong id="b381849141718"><a name="b381849141718"></a><a name="b381849141718"></a>0</strong>: full backup</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "backups": [
    {
    "status": "error",
    "description": null,
    "links": [
    {
    "href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "rel": "self"
    },
    {
    "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "rel": "bookmark"
    }
    ],
    "availability_zone": null,
    "volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024",
    "fail_reason": "Connection to swift failed: [Errno 111] ECONNREFUSED",
    "id": "1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "size": 1,
    "object_count": null,
    "container": "volumebackups",
    "name": null,
    "created_at": "2013-06-27T08:48:03.000000",
    "os-bak-tenant-attr:tenant_id": "b23b579f08c84228b9b4673c46f0c442",
    "service_metadata": " {\"bootable\": false, \"backupurl\": \"58d94782-6509-45ad-9442-970d2a005050\", \"BackupSize\": 0, \"progress\": \"0\", \"snap_id\": \"665e411f5d87431ca98c199fbd4a64fd\", \"Type\": 0} "
    },
    {
    "status": "error",
    "description": null,
    "links": [
    {
    "href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/80e17946-6e56-46e0-9547-e9ba4f1619bd",
    "rel": "self"
    },
    {
    "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/80e17946-6e56-46e0-9547-e9ba4f1619bd",
    "rel": "bookmark"
    }
    ],
    "availability_zone": null,
    "volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024",
    "fail_reason": "Connection to swift failed: [Errno 111] ECONNREFUSED",
    "id": "80e17946-6e56-46e0-9547-e9ba4f1619bd",
    "size": 1,
    "object_count": null,
    "container": "volumebackups",
    "name": null,
    "created_at": "2013-06-27T08:56:58.000000"
    },
    {
    "status": "error",
    "description": null,
    "links": [
    {
    "href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/b3cf7a16-decc-4beb-8077-682737d94a58",
    "rel": "self"
    },
    {
    "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/b3cf7a16-decc-4beb-8077-682737d94a58",
    "rel": "bookmark"
    }
    ],
    "availability_zone": null,
    "volume_id": "2748f2f2-4394-4e6e-af8d-8dd34496c024",
    "fail_reason": "Connection to swift failed: [Errno 111] ECONNREFUSED",
    "id": "b3cf7a16-decc-4beb-8077-682737d94a58",
    "size": 1,
    "object_count": null,
    "container": "volumebackups",
    "name": null,
    "created_at": "2013-06-27T08:46:31.000000"
    }
    ],
    "backups_links": [
        {
          "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups?limit=1&offset=1&marker=b3cf7a16-decc-4beb-8077-682737d94a58",
          "rel": "next"
        }
      ]
    }
    ```


## Status Codes<a name="section33206990"></a>

-   Normal

    200

-   Abnormal

    <a name="table24890860203310"></a>
    <table><thead align="left"><tr id="row29188547203310"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15462140203310"><a name="p15462140203310"></a><a name="p15462140203310"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p44473833203310"><a name="p44473833203310"></a><a name="p44473833203310"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45610739203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3482369203310"><a name="p3482369203310"></a><a name="p3482369203310"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p13636476203310"><a name="p13636476203310"></a><a name="p13636476203310"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row55619421203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8879270203310"><a name="p8879270203310"></a><a name="p8879270203310"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p48132239203310"><a name="p48132239203310"></a><a name="p48132239203310"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row30536967203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57575235203310"><a name="p57575235203310"></a><a name="p57575235203310"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p33082484203310"><a name="p33082484203310"></a><a name="p33082484203310"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row29306908203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25049367203310"><a name="p25049367203310"></a><a name="p25049367203310"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p15732859203310"><a name="p15732859203310"></a><a name="p15732859203310"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7378003203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p60747366203310"><a name="p60747366203310"></a><a name="p60747366203310"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p21589622203310"><a name="p21589622203310"></a><a name="p21589622203310"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60088872203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p35360445203310"><a name="p35360445203310"></a><a name="p35360445203310"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p45623811203310"><a name="p45623811203310"></a><a name="p45623811203310"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row7961120203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40870961203310"><a name="p40870961203310"></a><a name="p40870961203310"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p22213576203310"><a name="p22213576203310"></a><a name="p22213576203310"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row65704456203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p20460704203310"><a name="p20460704203310"></a><a name="p20460704203310"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p46704304203310"><a name="p46704304203310"></a><a name="p46704304203310"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row17685557203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23244013203310"><a name="p23244013203310"></a><a name="p23244013203310"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3716914203310"><a name="p3716914203310"></a><a name="p3716914203310"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row33452228203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p25275975203310"><a name="p25275975203310"></a><a name="p25275975203310"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p34088074203310"><a name="p34088074203310"></a><a name="p34088074203310"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row38357211203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p19926369203310"><a name="p19926369203310"></a><a name="p19926369203310"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3423229203310"><a name="p3423229203310"></a><a name="p3423229203310"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row30809061203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p12506042203310"><a name="p12506042203310"></a><a name="p12506042203310"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p6356504203310"><a name="p6356504203310"></a><a name="p6356504203310"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row57208537203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3379926203310"><a name="p3379926203310"></a><a name="p3379926203310"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5338608203310"><a name="p5338608203310"></a><a name="p5338608203310"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row48047475203310"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p66640258203310"><a name="p66640258203310"></a><a name="p66640258203310"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p29151842203310"><a name="p29151842203310"></a><a name="p29151842203310"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

