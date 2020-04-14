# Querying Details About VBS Backups \(Native OpenStack V3 API\)<a name="EN-US_TOPIC_0143705536"></a>

## Function<a name="section38423121"></a>

This interface is used to query the details about VBS backups.

## URI<a name="section10263773"></a>

-   URI format

    GET /v3/\{project\_id\}/native/backups/detail

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
    <tr id="row81593718492"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p815737124914"><a name="p815737124914"></a><a name="p815737124914"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p5654459499"><a name="p5654459499"></a><a name="p5654459499"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p17151437104914"><a name="p17151437104914"></a><a name="p17151437104914"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p1048013812508"><a name="p1048013812508"></a><a name="p1048013812508"></a>The query result contains the <strong id="b03011923942"><a name="b03011923942"></a><a name="b03011923942"></a>count</strong> field whose default value is <strong id="b53011223946"><a name="b53011223946"></a><a name="b53011223946"></a>False</strong>. This field is first available in the 3.45 version.</p>
    </td>
    </tr>
    <tr id="row02145319015"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p58374830151723"><a name="p58374830151723"></a><a name="p58374830151723"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p30740762151723"><a name="p30740762151723"></a><a name="p30740762151723"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p6973819151723"><a name="p6973819151723"></a><a name="p6973819151723"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p28008505151723"><a name="p28008505151723"></a><a name="p28008505151723"></a>Fuzzy query by backup name. This parameter is added in version 3.31.</p>
    </td>
    </tr>
    <tr id="row496314566012"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p36381618154250"><a name="p36381618154250"></a><a name="p36381618154250"></a>status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p61229932154250"><a name="p61229932154250"></a><a name="p61229932154250"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p60677479154250"><a name="p60677479154250"></a><a name="p60677479154250"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p15928779154250"><a name="p15928779154250"></a><a name="p15928779154250"></a>Fuzzy query by backup status. This parameter is added in version 3.31.</p>
    </td>
    </tr>
    <tr id="row14441101916"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p19469525163651"><a name="p19469525163651"></a><a name="p19469525163651"></a>volume_id~</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p33527697163651"><a name="p33527697163651"></a><a name="p33527697163651"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p31388933163651"><a name="p31388933163651"></a><a name="p31388933163651"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p59475674163651"><a name="p59475674163651"></a><a name="p59475674163651"></a>Fuzzy query by disk ID. This parameter is added in version 3.31.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the version features such as with\_count, name\~, status\~, and volume\_id\~ are used, add  **Openstack-Api-Version": volume 3.45**  \(3.45 is the version number\) to the header when requesting the URL.  

-   Example request

    ```
    GET /v3/{project_id}/backups/detail?name=backup&status=error&limit=10&volume_id=7d7c6fbe-d7ee-4b4d-8bae-bdd08b5604bb
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
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p5266693716349"><a name="p5266693716349"></a><a name="p5266693716349"></a>list&lt;link&gt;</p>
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
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p51837782202619"><a name="p51837782202619"></a><a name="p51837782202619"></a>Number of objects on OBS for the disk data</p>
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
    <tr id="row436163494914"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p129711035184910"><a name="p129711035184910"></a><a name="p129711035184910"></a>os-backup-project-attr:project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p7972235194916"><a name="p7972235194916"></a><a name="p7972235194916"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p12972133513498"><a name="p12972133513498"></a><a name="p12972133513498"></a>ID of the project that owns the VBS backup</p>
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
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p2446587175250"><a name="p2446587175250"></a><a name="p2446587175250"></a>Whether a dependent backup exists</p>
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
    <tr id="row19268125025113"><td class="cellrowborder" valign="top" width="28.74%" headers="mcps1.1.4.1.1 "><p id="p17268950155116"><a name="p17268950155116"></a><a name="p17268950155116"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.4.1.2 "><p id="p1026813505515"><a name="p1026813505515"></a><a name="p1026813505515"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.87%" headers="mcps1.1.4.1.3 "><p id="p418212513527"><a name="p418212513527"></a><a name="p418212513527"></a>Number of returned items. This parameter is first available in the 3.45 version.</p>
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
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p149653783520"><a name="p149653783520"></a><a name="p149653783520"></a>Specifies whether the backup is an incremental backup. <strong id="b104201640132016"><a name="b104201640132016"></a><a name="b104201640132016"></a>1</strong>: incremental backup; <strong id="b1542084082015"><a name="b1542084082015"></a><a name="b1542084082015"></a>0</strong>: full backup</p>
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
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p4598133313404"><a name="p4598133313404"></a><a name="p4598133313404"></a>Specifies that the URL of the last backup is queried.</p>
    </td>
    </tr>
    <tr id="row5502172319407"><td class="cellrowborder" valign="top" width="26.090000000000003%" headers="mcps1.1.4.1.1 "><p id="p559918335401"><a name="p559918335401"></a><a name="p559918335401"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p10599173319404"><a name="p10599173319404"></a><a name="p10599173319404"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.43%" headers="mcps1.1.4.1.3 "><p id="p165991533174010"><a name="p165991533174010"></a><a name="p165991533174010"></a>Relationship between the query result and <strong id="b842352706202944"><a name="b842352706202944"></a><a name="b842352706202944"></a>href</strong>. The value <strong id="b1636101139174441"><a name="b1636101139174441"></a><a name="b1636101139174441"></a>next</strong> indicates that some backups are not obtained.</p>
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
    "os-backup-project-attr:project_id": "b23b579f08c84228b9b4673c46f0c442",
    "snapshot_id": "66a574c0-4415-499e-b0b1-3f340d7f7932",
    "updated_at": "2019-03-27T12:36:17.596602",
    "data_timestamp": "2019-03-16T11:56:00.917245",
    "has_dependent_backups": false,
    "is_incremental": false
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
    "created_at": "2013-06-27T08:56:58.000000",
    "os-backup-project-attr:project_id": "b23b579f08c84228b9b4673c46f0c442",
    "snapshot_id": "66a574c0-4415-499e-b0b1-3f340d7f7932",
    "updated_at": "2019-03-27T12:36:17.596602",
    "data_timestamp": "2019-03-16T11:56:00.917245",
    "has_dependent_backups": false,
    "is_incremental": false
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
    "created_at": "2013-06-27T08:46:31.000000",
    "snapshot_id": "66a574c0-4415-499e-b0b1-3f340d7f7932",
    "updated_at": "2019-03-27T12:36:17.596602",
    "data_timestamp": "2019-03-16T11:56:00.917245",
    "has_dependent_backups": false,
    "is_incremental": false
    }
    ]
    }
    ```


## Status Codes<a name="section33206990"></a>

-   Normal

    200

-   Abnormal

    <a name="table24890860203310"></a>
    <table><thead align="left"><tr id="row29188547203310"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15462140203310"><a name="p15462140203310"></a><a name="p15462140203310"></a>Status Codes</p>
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


