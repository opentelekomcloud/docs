# Restoring Data to the Original DB Instance<a name="en-us_topic_0037147508"></a>

## Function<a name="section4850156117316"></a>

This API is used to restore data to the original DB instance.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.67%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.260000000000005%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.67%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions

    The DB engine Microsoft SQL Server is not supported.


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table3678226816954"></a>
    <table><thead align="left"><tr id="row1340482316954"><th class="cellrowborder" valign="top" width="18.04819518048195%" id="mcps1.2.5.1.1"><p id="p1204887716954"><a name="p1204887716954"></a><a name="p1204887716954"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.06729327067293%" id="mcps1.2.5.1.2"><p id="p5641325215138"><a name="p5641325215138"></a><a name="p5641325215138"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.918008199180083%" id="mcps1.2.5.1.3"><p id="p3077560415137"><a name="p3077560415137"></a><a name="p3077560415137"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.96650334966503%" id="mcps1.2.5.1.4"><p id="p6554990116954"><a name="p6554990116954"></a><a name="p6554990116954"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row794180116954"><td class="cellrowborder" valign="top" width="18.04819518048195%" headers="mcps1.2.5.1.1 "><p id="p3930611216954"><a name="p3930611216954"></a><a name="p3930611216954"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.06729327067293%" headers="mcps1.2.5.1.2 "><p id="p2196665315138"><a name="p2196665315138"></a><a name="p2196665315138"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p41480320151354"><a name="p41480320151354"></a><a name="p41480320151354"></a>Dictionary data structure. For details, see <a href="#table634280816954">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.96650334966503%" headers="mcps1.2.5.1.4 "><p id="p3798745816954"><a name="p3798745816954"></a><a name="p3798745816954"></a>Specifies the restore information, including <strong id="b842352706164349"><a name="b842352706164349"></a><a name="b842352706164349"></a>backupRef</strong> and <strong id="b842352706164353"><a name="b842352706164353"></a><a name="b842352706164353"></a>restoreTime</strong>. At least one of them must be specified. If both of them are specified, only <strong id="b31486606164525"><a name="b31486606164525"></a><a name="b31486606164525"></a>backupRef</strong> takes effect.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  restore field data structure description

    <a name="table634280816954"></a>
    <table><thead align="left"><tr id="row2197661216954"><th class="cellrowborder" valign="top" width="18.8%" id="mcps1.2.5.1.1"><p id="p3527513616954"><a name="p3527513616954"></a><a name="p3527513616954"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.31%" id="mcps1.2.5.1.2"><p id="p40764322151251"><a name="p40764322151251"></a><a name="p40764322151251"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.17%" id="mcps1.2.5.1.3"><p id="p25282334151257"><a name="p25282334151257"></a><a name="p25282334151257"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.72%" id="mcps1.2.5.1.4"><p id="p4880423616954"><a name="p4880423616954"></a><a name="p4880423616954"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6082906916954"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p2820759516954"><a name="p2820759516954"></a><a name="p2820759516954"></a>backupRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.31%" headers="mcps1.2.5.1.2 "><p id="p25894537151251"><a name="p25894537151251"></a><a name="p25894537151251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.5.1.3 "><p id="p51393005151257"><a name="p51393005151257"></a><a name="p51393005151257"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.72%" headers="mcps1.2.5.1.4 "><p id="p2900499116954"><a name="p2900499116954"></a><a name="p2900499116954"></a>Specifies the full backup file ID.</p>
    <div class="notice" id="note16651710113411"><a name="note16651710113411"></a><a name="note16651710113411"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1754195923415"><a name="p1754195923415"></a><a name="p1754195923415"></a>If <span class="parmname" id="parmname10508360356"><a name="parmname10508360356"></a><a name="parmname10508360356"></a><b>backupRef</b></span> is empty, <span class="parmname" id="parmname1672544516344"><a name="parmname1672544516344"></a><a name="parmname1672544516344"></a><b>restoreTime</b></span> is mandatory. Otherwise, an error is reported.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row14634957211441"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p44580875211441"><a name="p44580875211441"></a><a name="p44580875211441"></a>restoreTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.31%" headers="mcps1.2.5.1.2 "><p id="p19527020151251"><a name="p19527020151251"></a><a name="p19527020151251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.17%" headers="mcps1.2.5.1.3 "><p id="p18755047151257"><a name="p18755047151257"></a><a name="p18755047151257"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.72%" headers="mcps1.2.5.1.4 "><p id="p34698034211441"><a name="p34698034211441"></a><a name="p34698034211441"></a>Specifies the time point to which the DB instance is restored.</p>
    <div class="notice" id="note133671919350"><a name="note133671919350"></a><a name="note133671919350"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p138101919355"><a name="p138101919355"></a><a name="p138101919355"></a>If <strong id="b52371656103514"><a name="b52371656103514"></a><a name="b52371656103514"></a>restoreTime</strong> is empty, <span class="parmname" id="parmname03841913359"><a name="parmname03841913359"></a><a name="parmname03841913359"></a><b>backupRef</b></span> is mandatory. Otherwise, an error is reported.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {    
    "restore": {
            "backupRef":"a9832168-7541-4536-b8d9-a8a9b79cf1b4"
        }
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  4**  Parameter description

    <a name="table11854613"></a>
    <table><thead align="left"><tr id="row48728718"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p54712068"><a name="p54712068"></a><a name="p54712068"></a><strong id="b842352706102328_9"><a name="b842352706102328_9"></a><a name="b842352706102328_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p570775"><a name="p570775"></a><a name="p570775"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46232835"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p1571113"><a name="p1571113"></a><a name="p1571113"></a>Dictionary data structure. For details, see <a href="#table52869820">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4491214"><a name="p4491214"></a><a name="p4491214"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  extendparam field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="23.932393239323936%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b842352706102328_11"><a name="b842352706102328_11"></a><a name="b842352706102328_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.734273427342735%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8307988"><td class="cellrowborder" valign="top" width="23.932393239323936%" headers="mcps1.2.4.1.1 "><p id="p1858451"><a name="p1858451"></a><a name="p1858451"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.734273427342735%" headers="mcps1.2.4.1.2 "><p id="p16316838"><a name="p16316838"></a><a name="p16316838"></a>List data structure. For details, see <a href="#table32267243">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16706408"><a name="p16706408"></a><a name="p16706408"></a>Indicates the returned <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  jobs field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b842352706102328_13"><a name="b842352706102328_13"></a><a name="b842352706102328_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48259009"><a name="p48259009"></a><a name="p48259009"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "extendparam": {
            "jobs": [
                {
                    "id": "ff80808156fa51c50156fa7c20210bc9"
                }
            ]
        }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

