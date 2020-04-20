# Changing DB Instance Volume<a name="en-us_topic_0034943367"></a>

## Function<a name="section4850156117316"></a>

This API is used to change the DB instance volume.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.490000000000002%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.88%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p28714935163555"><a name="p28714935163555"></a><a name="p28714935163555"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions
    1.  The adjusted volume size must be greater than the original one and the desired volume size must be a multiple of 10.
    2.  The sizes of the primary and standby DB instances are the same. When you scale the primary DB instance, its standby DB instance is also scaled.
    3.  The DB instances can be scaled when they are in the  **Available**  state.


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table3678226816954"></a>
    <table><thead align="left"><tr id="row1340482316954"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p1204887716954"><a name="p1204887716954"></a><a name="p1204887716954"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p3643495116954"><a name="p3643495116954"></a><a name="p3643495116954"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6554990116954"><a name="p6554990116954"></a><a name="p6554990116954"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row794180116954"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p3930611216954"><a name="p3930611216954"></a><a name="p3930611216954"></a>resize</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p2967852416954"><a name="p2967852416954"></a><a name="p2967852416954"></a>Dictionary data structure. For details, see <a href="#table634280816954">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3798745816954"><a name="p3798745816954"></a><a name="p3798745816954"></a>Specifies the information about the request parameter <strong id="b842352706113940_1"><a name="b842352706113940_1"></a><a name="b842352706113940_1"></a>volume</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  resize field data structure description

    <a name="table634280816954"></a>
    <table><thead align="left"><tr id="row2197661216954"><th class="cellrowborder" valign="top" width="23.932393239323936%" id="mcps1.2.4.1.1"><p id="p3527513616954"><a name="p3527513616954"></a><a name="p3527513616954"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.734273427342735%" id="mcps1.2.4.1.2"><p id="p3871372816954"><a name="p3871372816954"></a><a name="p3871372816954"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p4880423616954"><a name="p4880423616954"></a><a name="p4880423616954"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6082906916954"><td class="cellrowborder" valign="top" width="23.932393239323936%" headers="mcps1.2.4.1.1 "><p id="p2820759516954"><a name="p2820759516954"></a><a name="p2820759516954"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.734273427342735%" headers="mcps1.2.4.1.2 "><p id="p311386916954"><a name="p311386916954"></a><a name="p311386916954"></a>Dictionary data structure. For details, see <a href="#table5971833216954">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2900499116954"><a name="p2900499116954"></a><a name="p2900499116954"></a>Specifies the information about the request parameter <strong id="b842352706113940_3"><a name="b842352706113940_3"></a><a name="b842352706113940_3"></a>size</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  volume field data structure description

    <a name="table5971833216954"></a>
    <table><thead align="left"><tr id="row3797548116954"><th class="cellrowborder" valign="top" width="23.932393239323936%" id="mcps1.2.4.1.1"><p id="p5611509816954"><a name="p5611509816954"></a><a name="p5611509816954"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.734273427342735%" id="mcps1.2.4.1.2"><p id="p4902912116954"><a name="p4902912116954"></a><a name="p4902912116954"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1193582716954"><a name="p1193582716954"></a><a name="p1193582716954"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2727794616954"><td class="cellrowborder" valign="top" width="23.932393239323936%" headers="mcps1.2.4.1.1 "><p id="p23854016161336"><a name="p23854016161336"></a><a name="p23854016161336"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.734273427342735%" headers="mcps1.2.4.1.2 "><p id="p5837783016954"><a name="p5837783016954"></a><a name="p5837783016954"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p50035813161416"><a name="p50035813161416"></a><a name="p50035813161416"></a>Specifies the volume size after scaling up. The value must a multiple of 10.</p>
    <p id="p168012412563"><a name="p168012412563"></a><a name="p168012412563"></a>Its value range is from 50 GB to 4000 GB.</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    <div class="notice" id="note18772920133413"><a name="note18772920133413"></a><a name="note18772920133413"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p3772920183420"><a name="p3772920183420"></a><a name="p3772920183420"></a>The adjusted volume size of must be greater than or equal to that of the original volume size.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {    
    "resize": {
            "volume": {
                "size": 400 
            }
        }
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  5**  Parameter description

    <a name="table11854613"></a>
    <table><thead align="left"><tr id="row48728718"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p54712068"><a name="p54712068"></a><a name="p54712068"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p570775"><a name="p570775"></a><a name="p570775"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46232835"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p1571113"><a name="p1571113"></a><a name="p1571113"></a>Dictionary data structure. For details, see <a href="#table52869820">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4491214"><a name="p4491214"></a><a name="p4491214"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  extendparam field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="23.932393239323936%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.734273427342735%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8307988"><td class="cellrowborder" valign="top" width="23.932393239323936%" headers="mcps1.2.4.1.1 "><p id="p1858451"><a name="p1858451"></a><a name="p1858451"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.734273427342735%" headers="mcps1.2.4.1.2 "><p id="p16316838"><a name="p16316838"></a><a name="p16316838"></a>List data structure. For details, see <a href="#table32267243">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16706408"><a name="p16706408"></a><a name="p16706408"></a>Indicates the returned <strong id="b5323105162339"><a name="b5323105162339"></a><a name="b5323105162339"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  jobs field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="23.75%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.92%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="23.75%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.92%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p48259009"><a name="p48259009"></a><a name="p48259009"></a>Indicates the task ID.</p>
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
                    "id": "2b414788-a600-4883-a023-90e2eb0ea227"
                }
            ]
        }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

