# Creating a Backup Share<a name="EN-US_TOPIC_0078214151"></a>

## Function<a name="section12991215691"></a>

This interface is used to create a backup share from a backup.

## URI<a name="section143041151095"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-backup-sharing

-   Parameter description

    <a name="table1331011512912"></a>
    <table><thead align="left"><tr id="row32541316392"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1625418168917"><a name="p1625418168917"></a><a name="p1625418168917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p9254916897"><a name="p9254916897"></a><a name="p9254916897"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1254191615916"><a name="p1254191615916"></a><a name="p1254191615916"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12254716991"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1025419164915"><a name="p1025419164915"></a><a name="p1025419164915"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3254171615911"><a name="p3254171615911"></a><a name="p3254171615911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section203249151917"></a>

-   Parameter description

    <a name="table10327101517913"></a>
    <table><thead align="left"><tr id="row2025515161398"><th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9255131617913"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.1 "><p id="p1925561617914"><a name="p1925561617914"></a><a name="p1925561617914"></a>shared</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p9255201610920"><a name="p9255201610920"></a><a name="p9255201610920"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.3 "><p id="p13255116691"><a name="p13255116691"></a><a name="p13255116691"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p11255191613913"><a name="p11255191613913"></a><a name="p11255191613913"></a>Information about the backup share</p>
    </td>
    </tr>
    <tr id="row1125531613913"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.1 "><p id="p1025551618919"><a name="p1025551618919"></a><a name="p1025551618919"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p125513161394"><a name="p125513161394"></a><a name="p125513161394"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.3 "><p id="p52562016296"><a name="p52562016296"></a><a name="p52562016296"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p11256181620912"><a name="p11256181620912"></a><a name="p11256181620912"></a>ID of the backup to be shared</p>
    </td>
    </tr>
    <tr id="row1625620161494"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.1 "><p id="p525620161894"><a name="p525620161894"></a><a name="p525620161894"></a>to_project_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p1256151620917"><a name="p1256151620917"></a><a name="p1256151620917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.3 "><p id="p1225613161696"><a name="p1225613161696"></a><a name="p1225613161696"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.1.5.1.4 "><p id="p42561616395"><a name="p42561616395"></a><a name="p42561616395"></a>IDs of projects with which the backup is shared</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "shared": {
            "to_project_ids": [
                "722513ed0a324dadaabe5b2d0fe848c9",
                "722513ed0a324dadaabe5b2d0fe84919"
            ],
            "backup_id": "066b1e37-9305-4057-97e5-2e99b21fc71d"
        }
    }
    ```


## Response<a name="section10341151511916"></a>

-   Parameter description

    <a name="table153449152913"></a>
    <table><thead align="left"><tr id="row125714163918"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.5.1.1"><p id="p11911851132015"><a name="p11911851132015"></a><a name="p11911851132015"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.1.5.1.2"><p id="p1310755112013"><a name="p1310755112013"></a><a name="p1310755112013"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.1.5.1.3"><p id="p191071951112015"><a name="p191071951112015"></a><a name="p191071951112015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.1.5.1.4"><p id="p210715118209"><a name="p210715118209"></a><a name="p210715118209"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1325713164913"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p925711161793"><a name="p925711161793"></a><a name="p925711161793"></a>shared</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p202571161192"><a name="p202571161192"></a><a name="p202571161192"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p9257216894"><a name="p9257216894"></a><a name="p9257216894"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p525751618910"><a name="p525751618910"></a><a name="p525751618910"></a>Information about the backup share</p>
    </td>
    </tr>
    <tr id="row1725701614917"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p42576166910"><a name="p42576166910"></a><a name="p42576166910"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p1125720161595"><a name="p1125720161595"></a><a name="p1125720161595"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p13257316494"><a name="p13257316494"></a><a name="p13257316494"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p82574167918"><a name="p82574167918"></a><a name="p82574167918"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row225761618918"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p1125714162914"><a name="p1125714162914"></a><a name="p1125714162914"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p525711166919"><a name="p525711166919"></a><a name="p525711166919"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p325712161396"><a name="p325712161396"></a><a name="p325712161396"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p1257116795"><a name="p1257116795"></a><a name="p1257116795"></a>Backup share ID</p>
    </td>
    </tr>
    <tr id="row1325814161497"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p12585161592"><a name="p12585161592"></a><a name="p12585161592"></a>to_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p325801610915"><a name="p325801610915"></a><a name="p325801610915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p0258101613919"><a name="p0258101613919"></a><a name="p0258101613919"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p125814161894"><a name="p125814161894"></a><a name="p125814161894"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row2025818162917"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p125817161790"><a name="p125817161790"></a><a name="p125817161790"></a>from_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p625818160911"><a name="p625818160911"></a><a name="p625818160911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p10258101611913"><a name="p10258101611913"></a><a name="p10258101611913"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p52582161096"><a name="p52582161096"></a><a name="p52582161096"></a>ID of the project that shares the backup</p>
    </td>
    </tr>
    <tr id="row1425814161916"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p325821619918"><a name="p325821619918"></a><a name="p325821619918"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p19258101620916"><a name="p19258101620916"></a><a name="p19258101620916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p162581216799"><a name="p162581216799"></a><a name="p162581216799"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p2025812167911"><a name="p2025812167911"></a><a name="p2025812167911"></a>Creation time of the backup share</p>
    </td>
    </tr>
    <tr id="row825831613910"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p1225814166915"><a name="p1225814166915"></a><a name="p1225814166915"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p32586163916"><a name="p32586163916"></a><a name="p32586163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p1225817164911"><a name="p1225817164911"></a><a name="p1225817164911"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p152584168918"><a name="p152584168918"></a><a name="p152584168918"></a>Update time of the backup share</p>
    </td>
    </tr>
    <tr id="row17258916492"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p1625891620919"><a name="p1625891620919"></a><a name="p1625891620919"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p14258916197"><a name="p14258916197"></a><a name="p14258916197"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p5258616496"><a name="p5258616496"></a><a name="p5258616496"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p132582161392"><a name="p132582161392"></a><a name="p132582161392"></a>Whether the backup has been deleted</p>
    </td>
    </tr>
    <tr id="row2258416292"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.5.1.1 "><p id="p9258516491"><a name="p9258516491"></a><a name="p9258516491"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.2 "><p id="p925918161911"><a name="p925918161911"></a><a name="p925918161911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.1.5.1.3 "><p id="p192592161291"><a name="p192592161291"></a><a name="p192592161291"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.1.5.1.4 "><p id="p125918161596"><a name="p125918161596"></a><a name="p125918161596"></a>Deletion time</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "shared": [
            {
                "backup_id": "066b1e37-9305-4057-97e5-2e99b21fc71d",
                "deleted": null,
                "created_at": null,
                "updated_at": null,
                "to_project_id": "722513ed0a324dadaabe5b2d0fe848c9",
                "from_project_id": "c13f5220dc1949b0b741ea81a7cd5554",
                "deleted_at": null,
                "id": "8332443e-9866-41d8-8a58-a898cf5db030"
            }
        ]
    }
    ```


## Status Codes<a name="section4372215591"></a>

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

