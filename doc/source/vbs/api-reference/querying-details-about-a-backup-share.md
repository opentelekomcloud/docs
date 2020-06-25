# Querying Details About a Backup Share<a name="EN-US_TOPIC_0078214155"></a>

## Function<a name="section112161181110"></a>

This interface is used to query details about a backup share.

## URI<a name="section202261121119"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-backup-sharing/\{id\}

-   Parameter description

    <a name="table525111161111"></a>
    <table><thead align="left"><tr id="row184241914117"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1625418168917"><a name="p1625418168917"></a><a name="p1625418168917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p9254916897"><a name="p9254916897"></a><a name="p9254916897"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1254191615916"><a name="p1254191615916"></a><a name="p1254191615916"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row194243121118"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1025419164915"><a name="p1025419164915"></a><a name="p1025419164915"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3254171615911"><a name="p3254171615911"></a><a name="p3254171615911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row194249110119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p164249171118"><a name="p164249171118"></a><a name="p164249171118"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1742414191111"><a name="p1742414191111"></a><a name="p1742414191111"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p17424016119"><a name="p17424016119"></a><a name="p17424016119"></a>Backup share ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11311114116"></a>

None

## Response<a name="section332171191116"></a>

-   Parameter description

    <a name="table94014121114"></a>
    <table><thead align="left"><tr id="row24251516110"><th class="cellrowborder" valign="top" width="24.39%" id="mcps1.1.4.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.509999999999998%" id="mcps1.1.4.1.2"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.10000000000001%" id="mcps1.1.4.1.3"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14255121115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p194259151113"><a name="p194259151113"></a><a name="p194259151113"></a>shared</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p19425121181111"><a name="p19425121181111"></a><a name="p19425121181111"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p186521181010"><a name="p186521181010"></a><a name="p186521181010"></a>Information about the backup share</p>
    </td>
    </tr>
    <tr id="row1542511116119"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p9425201191114"><a name="p9425201191114"></a><a name="p9425201191114"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1742521181115"><a name="p1742521181115"></a><a name="p1742521181115"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p4861214107"><a name="p4861214107"></a><a name="p4861214107"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row174254131112"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p742501151111"><a name="p742501151111"></a><a name="p742501151111"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1342611171119"><a name="p1342611171119"></a><a name="p1342611171119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p28652112106"><a name="p28652112106"></a><a name="p28652112106"></a>Creation time of the backup share</p>
    </td>
    </tr>
    <tr id="row942641171115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p194263161119"><a name="p194263161119"></a><a name="p194263161119"></a>from_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p44265120112"><a name="p44265120112"></a><a name="p44265120112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p186142117106"><a name="p186142117106"></a><a name="p186142117106"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row5426819111"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1342612117111"><a name="p1342612117111"></a><a name="p1342612117111"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1842601191119"><a name="p1842601191119"></a><a name="p1842601191119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p386821111013"><a name="p386821111013"></a><a name="p386821111013"></a>Backup share ID</p>
    </td>
    </tr>
    <tr id="row54261716112"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p12426141171114"><a name="p12426141171114"></a><a name="p12426141171114"></a>to_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p44267111114"><a name="p44267111114"></a><a name="p44267111114"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p1487421171010"><a name="p1487421171010"></a><a name="p1487421171010"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row7426018111"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p10426115114"><a name="p10426115114"></a><a name="p10426115114"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p742611161114"><a name="p742611161114"></a><a name="p742611161114"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p12871121121014"><a name="p12871121121014"></a><a name="p12871121121014"></a>Update time of the backup share</p>
    </td>
    </tr>
    <tr id="row14426416115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p24261612119"><a name="p24261612119"></a><a name="p24261612119"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p12427101151110"><a name="p12427101151110"></a><a name="p12427101151110"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p18717218107"><a name="p18717218107"></a><a name="p18717218107"></a>Details about the source backup</p>
    </td>
    </tr>
    <tr id="row17427812113"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p942751181115"><a name="p942751181115"></a><a name="p942751181115"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p14279114115"><a name="p14279114115"></a><a name="p14279114115"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p42822461202619"><a name="p42822461202619"></a><a name="p42822461202619"></a>AZ where the backup resides</p>
    </td>
    </tr>
    <tr id="row174289111116"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p19428131121110"><a name="p19428131121110"></a><a name="p19428131121110"></a>container</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p154287110111"><a name="p154287110111"></a><a name="p154287110111"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p45004514202619"><a name="p45004514202619"></a><a name="p45004514202619"></a>Container of the backup</p>
    </td>
    </tr>
    <tr id="row194280110119"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p54281112112"><a name="p54281112112"></a><a name="p54281112112"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1042811112114"><a name="p1042811112114"></a><a name="p1042811112114"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p1604592202619"><a name="p1604592202619"></a><a name="p1604592202619"></a>Backup creation time</p>
    </td>
    </tr>
    <tr id="row19428414112"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1142910114119"><a name="p1142910114119"></a><a name="p1142910114119"></a>data_timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p14299112112"><a name="p14299112112"></a><a name="p14299112112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p14905520174631"><a name="p14905520174631"></a><a name="p14905520174631"></a>Current time</p>
    </td>
    </tr>
    <tr id="row742916131119"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1142911121117"><a name="p1142911121117"></a><a name="p1142911121117"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p942961181117"><a name="p942961181117"></a><a name="p942961181117"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p51398114202619"><a name="p51398114202619"></a><a name="p51398114202619"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row142901151117"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1342941181117"><a name="p1342941181117"></a><a name="p1342941181117"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p742921121119"><a name="p742921121119"></a><a name="p742921121119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p44790369202619"><a name="p44790369202619"></a><a name="p44790369202619"></a>Cause of the backup failure</p>
    </td>
    </tr>
    <tr id="row1943091141115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p44301012118"><a name="p44301012118"></a><a name="p44301012118"></a>has_dependent_backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p443018121116"><a name="p443018121116"></a><a name="p443018121116"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p2446587175250"><a name="p2446587175250"></a><a name="p2446587175250"></a>Whether a dependent backup exists. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row1043019113114"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1143015181117"><a name="p1143015181117"></a><a name="p1143015181117"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p74335118119"><a name="p74335118119"></a><a name="p74335118119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p60551425202619"><a name="p60551425202619"></a><a name="p60551425202619"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row1943341151119"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p9433151201113"><a name="p9433151201113"></a><a name="p9433151201113"></a>is_incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p6433419113"><a name="p6433419113"></a><a name="p6433419113"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p16898564175250"><a name="p16898564175250"></a><a name="p16898564175250"></a>Whether the backup is an incremental backup. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row20433101111115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p443314115118"><a name="p443314115118"></a><a name="p443314115118"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1543301131120"><a name="p1543301131120"></a><a name="p1543301131120"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p27753504202619"><a name="p27753504202619"></a><a name="p27753504202619"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row11433171171114"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p1343311141115"><a name="p1343311141115"></a><a name="p1343311141115"></a>object_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p104331414111"><a name="p104331414111"></a><a name="p104331414111"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p51837782202619"><a name="p51837782202619"></a><a name="p51837782202619"></a>Number of objects on OBS for the disk data</p>
    </td>
    </tr>
    <tr id="row1043310131116"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p44339141112"><a name="p44339141112"></a><a name="p44339141112"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p943371131112"><a name="p943371131112"></a><a name="p943371131112"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p38938725202619"><a name="p38938725202619"></a><a name="p38938725202619"></a>Backup size</p>
    </td>
    </tr>
    <tr id="row443491131113"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p8434512115"><a name="p8434512115"></a><a name="p8434512115"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p94342017116"><a name="p94342017116"></a><a name="p94342017116"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p1617637175250"><a name="p1617637175250"></a><a name="p1617637175250"></a>ID of the snapshot associated with the backup</p>
    </td>
    </tr>
    <tr id="row7434121151120"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p124345171111"><a name="p124345171111"></a><a name="p124345171111"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1343451181116"><a name="p1343451181116"></a><a name="p1343451181116"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p55194315202619"><a name="p55194315202619"></a><a name="p55194315202619"></a>Backup status</p>
    </td>
    </tr>
    <tr id="row184341816110"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p13434515113"><a name="p13434515113"></a><a name="p13434515113"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p1343514111114"><a name="p1343514111114"></a><a name="p1343514111114"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p5110169017462"><a name="p5110169017462"></a><a name="p5110169017462"></a>Update time of the backup</p>
    </td>
    </tr>
    <tr id="row8435211115"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p743561181112"><a name="p743561181112"></a><a name="p743561181112"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p174355112112"><a name="p174355112112"></a><a name="p174355112112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p39169096202619"><a name="p39169096202619"></a><a name="p39169096202619"></a>Source disk ID of the backup</p>
    </td>
    </tr>
    <tr id="row14357115114"><td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.1.4.1.1 "><p id="p134354110114"><a name="p134354110114"></a><a name="p134354110114"></a>service_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p6435010119"><a name="p6435010119"></a><a name="p6435010119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.10000000000001%" headers="mcps1.1.4.1.3 "><p id="p10122423202619"><a name="p10122423202619"></a><a name="p10122423202619"></a>Backup metadata</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "shared": {
            "backup": {
                "availability_zone": "AZ1",
                "container": null,
                "created_at": "2017-08-08T04:03:27.000000",
                "data_timestamp": "2017-08-08T04:03:27.000000",
                "description": null,
                "fail_reason": "Invalid InitiatorConnector protocol specified DSWARE",
                "has_dependent_backups": null,
                "id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                "is_incremental": null,
                "name": "lbf",
                "object_count": 0,
                "size": 1,
                "snapshot_id": null,
                "status": "available",
                "updated_at": "2017-08-16T07:24:24.786297",
                "volume_id": "a7d7783f-02b7-4645-b0e3-61df63f0ba10",
                "service_metadata": null
            },
            "backup_id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
            "created_at": "2017-08-22T08:43:16.699374",
            "from_project_id": "c13f5220dc1949b0b741ea81a7cd5554",
            "id": "8332443e-9866-41d8-8a58-a898cf5db030",
            "to_project_id": "722513ed0a324dadaabe5b2d0fe848c9",
            "updated_at": null
        }
    }
    ```


## Status Codes<a name="section1512371161119"></a>

-   Normal

    200

-   Abnormal

    <a name="table59178184203255"></a>
    <table><thead align="left"><tr id="row54047877203255"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15801936203255"><a name="p15801936203255"></a><a name="p15801936203255"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p4888452203255"><a name="p4888452203255"></a><a name="p4888452203255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60420295203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p62205764203255"><a name="p62205764203255"></a><a name="p62205764203255"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5502113203255"><a name="p5502113203255"></a><a name="p5502113203255"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row49519019203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p51617596203255"><a name="p51617596203255"></a><a name="p51617596203255"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20275713203255"><a name="p20275713203255"></a><a name="p20275713203255"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48263690203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17044857203255"><a name="p17044857203255"></a><a name="p17044857203255"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38456209203255"><a name="p38456209203255"></a><a name="p38456209203255"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row10561563203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50180290203255"><a name="p50180290203255"></a><a name="p50180290203255"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38071718203255"><a name="p38071718203255"></a><a name="p38071718203255"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7101146203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38321955203255"><a name="p38321955203255"></a><a name="p38321955203255"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p17070685203255"><a name="p17070685203255"></a><a name="p17070685203255"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row19418444203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p29390130203255"><a name="p29390130203255"></a><a name="p29390130203255"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31790300203255"><a name="p31790300203255"></a><a name="p31790300203255"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row17677246203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22570826203255"><a name="p22570826203255"></a><a name="p22570826203255"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16297614203255"><a name="p16297614203255"></a><a name="p16297614203255"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row12460805203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2692305203255"><a name="p2692305203255"></a><a name="p2692305203255"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16750186203255"><a name="p16750186203255"></a><a name="p16750186203255"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row16533951203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64181621203255"><a name="p64181621203255"></a><a name="p64181621203255"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31328812203255"><a name="p31328812203255"></a><a name="p31328812203255"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row13523855203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p21690474203255"><a name="p21690474203255"></a><a name="p21690474203255"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12097945203255"><a name="p12097945203255"></a><a name="p12097945203255"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row41772644203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28140973203255"><a name="p28140973203255"></a><a name="p28140973203255"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p64826302203255"><a name="p64826302203255"></a><a name="p64826302203255"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46565809203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13734210203255"><a name="p13734210203255"></a><a name="p13734210203255"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38729264203255"><a name="p38729264203255"></a><a name="p38729264203255"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row13019061203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p47911033203255"><a name="p47911033203255"></a><a name="p47911033203255"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p55588428203255"><a name="p55588428203255"></a><a name="p55588428203255"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row30533812203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57319716203255"><a name="p57319716203255"></a><a name="p57319716203255"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12385400203255"><a name="p12385400203255"></a><a name="p12385400203255"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

