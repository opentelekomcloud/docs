# Creating a VBS Backup<a name="EN-US_TOPIC_0020237255"></a>

## Function<a name="section63962185"></a>

This interface is used to create a VBS backup.

If the API is successfully called, the backup task is successfully delivered. You can query the backup status by using the API for  [Querying Details About a VBS Backup \(Native OpenStack API\)](querying-details-about-a-vbs-backup-(native-openstack-api).md).

## URI<a name="section38788755"></a>

-   URI format

    POST /v2/\{project\_id\}/cloudbackups

-   Parameter description

    <a name="table60344938"></a>
    <table><thead align="left"><tr id="row59011071"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p15167431"><a name="p15167431"></a><a name="p15167431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p20602375"><a name="p20602375"></a><a name="p20602375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p58179688"><a name="p58179688"></a><a name="p58179688"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14934289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1717931"><a name="p1717931"></a><a name="p1717931"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4934750"><a name="p4934750"></a><a name="p4934750"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

-   Parameter description

    <a name="table48412952"></a>
    <table><thead align="left"><tr id="row28932175"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.83%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row187031441791"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.1 "><p id="p385596811791"><a name="p385596811791"></a><a name="p385596811791"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.1.5.1.2 "><p id="p363264551791"><a name="p363264551791"></a><a name="p363264551791"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.83%" headers="mcps1.1.5.1.3 "><p id="p567617131791"><a name="p567617131791"></a><a name="p567617131791"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.1.5.1.4 "><p id="p342960231791"><a name="p342960231791"></a><a name="p342960231791"></a>Backup to be created. For details, see the <strong id="b2167716175313"><a name="b2167716175313"></a><a name="b2167716175313"></a>backup</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **backup**  field description

    <a name="table1864132719178"></a>
    <table><thead align="left"><tr id="row064112751715"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.1"><p id="p186452718171"><a name="p186452718171"></a><a name="p186452718171"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="p36416279175"><a name="p36416279175"></a><a name="p36416279175"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.3"><p id="p1664182720171"><a name="p1664182720171"></a><a name="p1664182720171"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.5.1.4"><p id="p12641427181712"><a name="p12641427181712"></a><a name="p12641427181712"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row364182741711"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p13641327201716"><a name="p13641327201716"></a><a name="p13641327201716"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p864102791710"><a name="p864102791710"></a><a name="p864102791710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p56410276174"><a name="p56410276174"></a><a name="p56410276174"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p166412273173"><a name="p166412273173"></a><a name="p166412273173"></a>ID of the disk to be backed up</p>
    </td>
    </tr>
    <tr id="row156492761714"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p464192711171"><a name="p464192711171"></a><a name="p464192711171"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p464927201718"><a name="p464927201718"></a><a name="p464927201718"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p146422710172"><a name="p146422710172"></a><a name="p146422710172"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p19659276174"><a name="p19659276174"></a><a name="p19659276174"></a>Snapshot ID of the disk to be backed up</p>
    </td>
    </tr>
    <tr id="row1365112718173"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p17654276175"><a name="p17654276175"></a><a name="p17654276175"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p11651327121713"><a name="p11651327121713"></a><a name="p11651327121713"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p196512275174"><a name="p196512275174"></a><a name="p196512275174"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p1651427111710"><a name="p1651427111710"></a><a name="p1651427111710"></a>Backup name. The value is a string of 1 to 64 characters that can contain digits, letters, underscores (_), and hyphens (-), not starting with <strong id="b05913432120"><a name="b05913432120"></a><a name="b05913432120"></a>auto</strong>.</p>
    </td>
    </tr>
    <tr id="row19651927121715"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p106552710177"><a name="p106552710177"></a><a name="p106552710177"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p665152718171"><a name="p665152718171"></a><a name="p665152718171"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p56519275179"><a name="p56519275179"></a><a name="p56519275179"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p2659277173"><a name="p2659277173"></a><a name="p2659277173"></a>Backup description. The value is a string of 1 to 64 characters and cannot contain the less-than sign (&lt;) or greater-than sign (&gt;).</p>
    </td>
    </tr>
    <tr id="row12651727171714"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p126512721714"><a name="p126512721714"></a><a name="p126512721714"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p865172715178"><a name="p865172715178"></a><a name="p865172715178"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p1465427191714"><a name="p1465427191714"></a><a name="p1465427191714"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p12651927111710"><a name="p12651927111710"></a><a name="p12651927111710"></a>List of tags to be configured for the backup resources For details, see the <strong id="b054110261608"><a name="b054110261608"></a><a name="b054110261608"></a>tag</strong> field description.</p>
    </td>
    </tr>
    <tr id="row76522791711"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p156516277178"><a name="p156516277178"></a><a name="p156516277178"></a>extend_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p665192710176"><a name="p665192710176"></a><a name="p665192710176"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p165027181718"><a name="p165027181718"></a><a name="p165027181718"></a>map&lt;string,string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p206582713177"><a name="p206582713177"></a><a name="p206582713177"></a>Additional information for creating the VBS backup. The <strong id="b84235270620309"><a name="b84235270620309"></a><a name="b84235270620309"></a>FullBackup</strong> field is supported. If <strong id="b1251862158203035"><a name="b1251862158203035"></a><a name="b1251862158203035"></a>FullBackup</strong> is set to <strong id="b842352706203125"><a name="b842352706203125"></a><a name="b842352706203125"></a>true</strong>, full backup will be adopted this time. If <strong id="b1030062150203055"><a name="b1030062150203055"></a><a name="b1030062150203055"></a>FullBackup</strong> is set to <strong id="b842352706203121"><a name="b842352706203121"></a><a name="b842352706203121"></a>false</strong> or the parameter is left blank, incremental backup will be adopted.</p>
    </td>
    </tr>
    </tbody>
    </table>

    -   **tag**  field description

        <a name="table2316162182113"></a>
        <table><thead align="left"><tr id="row3316122118215"><th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.1"><p id="p631702117212"><a name="p631702117212"></a><a name="p631702117212"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="p143171921192110"><a name="p143171921192110"></a><a name="p143171921192110"></a>Mandatory</p>
        </th>
        <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.3"><p id="p133171321172114"><a name="p133171321172114"></a><a name="p133171321172114"></a>Type</p>
        </th>
        <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.5.1.4"><p id="p43174219217"><a name="p43174219217"></a><a name="p43174219217"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row5317162119217"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p12317162118211"><a name="p12317162118211"></a><a name="p12317162118211"></a>key</p>
        </td>
        <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p33172212219"><a name="p33172212219"></a><a name="p33172212219"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p1331711212217"><a name="p1331711212217"></a><a name="p1331711212217"></a>string</p>
        </td>
        <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p431772116215"><a name="p431772116215"></a><a name="p431772116215"></a>Tag key. A tag key consists of up to 36 characters. A tag key cannot contain non-printable ASCII characters (0-31) and the following special characters: =*&lt;&gt;\,|/</p>
        </td>
        </tr>
        <tr id="row03179218217"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.1 "><p id="p13179214211"><a name="p13179214211"></a><a name="p13179214211"></a>value</p>
        </td>
        <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p103171121102120"><a name="p103171121102120"></a><a name="p103171121102120"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p73171121132118"><a name="p73171121132118"></a><a name="p73171121132118"></a>string</p>
        </td>
        <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.5.1.4 "><p id="p2317921172119"><a name="p2317921172119"></a><a name="p2317921172119"></a>Tag value. A tag value consists of 0 to 43 characters. A tag key cannot contain non-printable ASCII characters (0-31) and the following special characters: =*&lt;&gt;\,|/</p>
        </td>
        </tr>
        </tbody>
        </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >When you use Instant Restore for the first time and the to-be-restored disk has been backed up before the feature is enabled, you need to perform a full backup on the disk on the console or directly call the API for creating a full backup \(**POST /v2/\{tenant\_id\}/cloudbackups**\). After doing this, the disk backups generated through APIs will support this feature.  


-   Example request

    ```
    {
        "backup": {
            "volume_id": "c68ae7fb-0aa5-4a97-ab01-ed02c5b7e768",
            "snapshot_id": null,
            "name": "backup1",
            "description": "Backup_Demo",
            "tags":[{
                "key":"key",
                "value":"value"
             }],
            "extend_param": {"FullBackup": "true"}
        }
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="15.428457154284573%" id="mcps1.1.4.1.1"><p id="p1352611598468"><a name="p1352611598468"></a><a name="p1352611598468"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.088391160883912%" id="mcps1.1.4.1.2"><p id="p85261859124613"><a name="p85261859124613"></a><a name="p85261859124613"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.48315168483151%" id="mcps1.1.4.1.3"><p id="p10526959124618"><a name="p10526959124618"></a><a name="p10526959124618"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p5325228320254"><a name="p5325228320254"></a><a name="p5325228320254"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
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


## Status Codes<a name="section24171358"></a>

-   Normal

    200

-   Abnormal

    <a name="table51230787"></a>
    <table><thead align="left"><tr id="row60503138"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1807185"><a name="p1807185"></a><a name="p1807185"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p12164329"><a name="p12164329"></a><a name="p12164329"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45786577"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17725233"><a name="p17725233"></a><a name="p17725233"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26457778"><a name="p26457778"></a><a name="p26457778"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row36793414"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row31979016"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4499052116376"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2035357816376"><a name="p2035357816376"></a><a name="p2035357816376"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3802708716376"><a name="p3802708716376"></a><a name="p3802708716376"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8462523163725"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14375766163725"><a name="p14375766163725"></a><a name="p14375766163725"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p23586373163725"><a name="p23586373163725"></a><a name="p23586373163725"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60343628163758"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55995701163758"><a name="p55995701163758"></a><a name="p55995701163758"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p39357967163758"><a name="p39357967163758"></a><a name="p39357967163758"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row32079544163754"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p48306260163754"><a name="p48306260163754"></a><a name="p48306260163754"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20492948163754"><a name="p20492948163754"></a><a name="p20492948163754"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28680770163738"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p41441040163738"><a name="p41441040163738"></a><a name="p41441040163738"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1281119163738"><a name="p1281119163738"></a><a name="p1281119163738"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row65552906164354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8185203164354"><a name="p8185203164354"></a><a name="p8185203164354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59021712164354"><a name="p59021712164354"></a><a name="p59021712164354"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row19714506"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p53371190"><a name="p53371190"></a><a name="p53371190"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28099101"><a name="p28099101"></a><a name="p28099101"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row32688750164938"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30543097164938"><a name="p30543097164938"></a><a name="p30543097164938"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p58071768164938"><a name="p58071768164938"></a><a name="p58071768164938"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row11809518164943"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17046908164943"><a name="p17046908164943"></a><a name="p17046908164943"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38622347164943"><a name="p38622347164943"></a><a name="p38622347164943"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row38399341164956"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23338889164956"><a name="p23338889164956"></a><a name="p23338889164956"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11401882164956"><a name="p11401882164956"></a><a name="p11401882164956"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row51565323"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16041657"><a name="p16041657"></a><a name="p16041657"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section51311416428"></a>

For details, see  [Error Codes](error-codes.md).

