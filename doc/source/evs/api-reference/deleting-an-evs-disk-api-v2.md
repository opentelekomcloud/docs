# Deleting an EVS Disk<a name="evs_04_2008"></a>

## Function<a name="section10932885"></a>

This API is used to delete an EVS disk. 

## URI<a name="section31287108"></a>

-   URI format

    DELETE /v2/\{project\_id\}/cloudvolumes/\{volume\_id\}

-   Parameter description

    <a name="table44522499"></a>
    <table><thead align="left"><tr id="row39474480"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p43316293"><a name="p43316293"></a><a name="p43316293"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.1.4.1.2"><p id="p18958859"><a name="p18958859"></a><a name="p18958859"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.1.4.1.3"><p id="p59272617"><a name="p59272617"></a><a name="p59272617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36352712"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p58888592"><a name="p58888592"></a><a name="p58888592"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.4.1.2 "><p id="p5246632"><a name="p5246632"></a><a name="p5246632"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.1.4.1.3 "><p id="p22324024"><a name="p22324024"></a><a name="p22324024"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row66698493"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p33868853"><a name="p33868853"></a><a name="p33868853"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.4.1.2 "><p id="p59022586"><a name="p59022586"></a><a name="p59022586"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.1.4.1.3 "><p id="p16100147"><a name="p16100147"></a><a name="p16100147"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13148517"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v2/{project_id}/cloudvolumes/b104b8db-170d-441b-897a-3c8ba9c5a214
    ```


## Response<a name="section51227795"></a>

-   Parameter description

    <a name="en-us_topic_0044524833_table735313581437"></a>
    <table><thead align="left"><tr id="en-us_topic_0044524833_row153536585313"><th class="cellrowborder" valign="top" width="21.157884211578843%" id="mcps1.1.4.1.1"><p id="en-us_topic_0044524833_p123541158732"><a name="en-us_topic_0044524833_p123541158732"></a><a name="en-us_topic_0044524833_p123541158732"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.197880211978802%" id="mcps1.1.4.1.2"><p id="en-us_topic_0044524833_p1435411581320"><a name="en-us_topic_0044524833_p1435411581320"></a><a name="en-us_topic_0044524833_p1435411581320"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="en-us_topic_0044524833_p13541058036"><a name="en-us_topic_0044524833_p13541058036"></a><a name="en-us_topic_0044524833_p13541058036"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044524833_row1135495819312"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0044524833_p33545583319"><a name="en-us_topic_0044524833_p33545583319"></a><a name="en-us_topic_0044524833_p33545583319"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0044524833_p19354165810317"><a name="en-us_topic_0044524833_p19354165810317"></a><a name="en-us_topic_0044524833_p19354165810317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0044524833_p435416581936"><a name="en-us_topic_0044524833_p435416581936"></a><a name="en-us_topic_0044524833_p435416581936"></a>Specifies the task ID.</p>
    <div class="note" id="en-us_topic_0044524833_note335410589314"><a name="en-us_topic_0044524833_note335410589314"></a><a name="en-us_topic_0044524833_note335410589314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0044524833_p1435514588312"><a name="en-us_topic_0044524833_p1435514588312"></a><a name="en-us_topic_0044524833_p1435514588312"></a>For details about how to query the task status, see <a href="querying-task-status.md">Querying Task Status</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0044524833_row195162113414"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0044524833_p129522216412"><a name="en-us_topic_0044524833_p129522216412"></a><a name="en-us_topic_0044524833_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0044524833_p1595262111415"><a name="en-us_topic_0044524833_p1595262111415"></a><a name="en-us_topic_0044524833_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0044524833_p109527215417"><a name="en-us_topic_0044524833_p109527215417"></a><a name="en-us_topic_0044524833_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
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


## Status Codes<a name="section58396974"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

