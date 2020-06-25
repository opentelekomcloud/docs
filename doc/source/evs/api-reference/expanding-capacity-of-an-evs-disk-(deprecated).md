# Expanding Capacity of an EVS Disk \(Deprecated\)<a name="evs_04_2014"></a>

## Function<a name="section4445458"></a>

This API is used to expand the capacity of an EVS disk. 

-   If the status of the to-be-expanded disk is  **available**, there are no restrictions.
-   If the status of the to-be-expanded disk is  **in-use**, the restrictions are as follows:
    -   A shared disk cannot be expanded, that is, the value of parameter  **multiattach**  must be  **false**.
    -   The status of the server to which the disk attached must be  **ACTIVE**,  **PAUSED**,  **SUSPENDED**, or  **SHUTOFF**.


>![](/images/icon-notice.gif) **NOTICE:**   
>This API call exists for compatibility reasons only and is not meant to be used.   

## URI<a name="section40009126"></a>

-   URI format

    POST /v2/\{project\_id\}/cloudvolumes/\{volume\_id\}/action

-   Parameter description

    <a name="table30668413"></a>
    <table><thead align="left"><tr id="row58200784"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p16643039"><a name="p16643039"></a><a name="p16643039"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p5908907"><a name="p5908907"></a><a name="p5908907"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p8859419"><a name="p8859419"></a><a name="p8859419"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46524311"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p10372872"><a name="p10372872"></a><a name="p10372872"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p34896342"><a name="p34896342"></a><a name="p34896342"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p8031464"><a name="p8031464"></a><a name="p8031464"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row5174319"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p16466658"><a name="p16466658"></a><a name="p16466658"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p58730959"><a name="p58730959"></a><a name="p58730959"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p59587228"><a name="p59587228"></a><a name="p59587228"></a>Specifies the ID of the disk.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section24537816"></a>

-   Parameter description

    <a name="table42671863"></a>
    <table><thead align="left"><tr id="row12592542"><th class="cellrowborder" valign="top" width="19.17%" id="mcps1.1.5.1.1"><p id="p13362997"><a name="p13362997"></a><a name="p13362997"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.5.1.2"><p id="p8661001"><a name="p8661001"></a><a name="p8661001"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.54%" id="mcps1.1.5.1.3"><p id="p30452481"><a name="p30452481"></a><a name="p30452481"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86%" id="mcps1.1.5.1.4"><p id="p50731910"><a name="p50731910"></a><a name="p50731910"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5187493615377"><td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.1.5.1.1 "><p id="p4112025815377"><a name="p4112025815377"></a><a name="p4112025815377"></a>os-extend</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.2 "><p id="p4240658415377"><a name="p4240658415377"></a><a name="p4240658415377"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.3 "><p id="p1238131615377"><a name="p1238131615377"></a><a name="p1238131615377"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p6336250715377"><a name="p6336250715377"></a><a name="p6336250715377"></a>Specifies the disk expansion marker. For details, see <a href="#li19185119124117">Parameter in the os-extend field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li19185119124117"></a>Parameter in the  **os-extend**  field

    <a name="table15186149194112"></a>
    <table><thead align="left"><tr id="row418613904115"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="p91861591418"><a name="p91861591418"></a><a name="p91861591418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="p218699134116"><a name="p218699134116"></a><a name="p218699134116"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.3"><p id="p141867974119"><a name="p141867974119"></a><a name="p141867974119"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48%" id="mcps1.1.5.1.4"><p id="p161874916417"><a name="p161874916417"></a><a name="p161874916417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row118711964115"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p101872944115"><a name="p101872944115"></a><a name="p101872944115"></a>new_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="p3187992411"><a name="p3187992411"></a><a name="p3187992411"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p118719914117"><a name="p118719914117"></a><a name="p118719914117"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.5.1.4 "><p id="p8187199204115"><a name="p8187199204115"></a><a name="p8187199204115"></a>Specifies the size of the disk after capacity expansion, in GB.</p>
    <p id="p1187179134115"><a name="p1187179134115"></a><a name="p1187179134115"></a>The new disk size ranges from the original disk size to the maximum size (<strong id="b842352706154149"><a name="b842352706154149"></a><a name="b842352706154149"></a>32768</strong> for a data disk and <strong id="b7981161735114"><a name="b7981161735114"></a><a name="b7981161735114"></a>1024</strong> for a system disk).</p>
    <div class="note" id="note518718914412"><a name="note518718914412"></a><a name="note518718914412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p5070492815911"><a name="evs_04_2013_p5070492815911"></a><a name="evs_04_2013_p5070492815911"></a>If the specified parameter value is a decimal, the integral part of the value is used by default when the request is sent.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "os-extend": {
            "new_size": 200
        }
    }
    ```


## Response<a name="section19513753"></a>

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


## Status Codes<a name="section41406050"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

