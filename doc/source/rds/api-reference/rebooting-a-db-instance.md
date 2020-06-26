# Rebooting a DB Instance<a name="en-us_topic_0034943368"></a>

## Function<a name="section4850156117316"></a>

This API is used to reboot a DB instance.

>![](/images/icon-notice.gif) **NOTICE:**   
>The RDS DB instance will be unavailable during the reboot process. Exercise caution when performing this operation.  

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST


-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.86%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.2%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.86%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.2%" headers="mcps1.2.4.1.3 "><p id="p28182251"><a name="p28182251"></a><a name="p28182251"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.86%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.2%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions

    The DB instance cannot reboot when it is being created, scaled, backed up, restored, or its instance class is being changed.


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="23.14%" id="mcps1.2.5.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.86%" id="mcps1.2.5.1.2"><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="23.14%" headers="mcps1.2.5.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>restart</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.86%" headers="mcps1.2.5.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>None</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p49586916144357"><a name="p49586916144357"></a><a name="p49586916144357"></a>This parameter is left blank.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
          "restart": {}
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table11854613"></a>
    <table><thead align="left"><tr id="row48728718"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p54712068"><a name="p54712068"></a><a name="p54712068"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p570775"><a name="p570775"></a><a name="p570775"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46232835"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p53872188"><a name="p53872188"></a><a name="p53872188"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p1571113"><a name="p1571113"></a><a name="p1571113"></a>Dictionary data structure. For details, see <a href="#table52869820">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4491214"><a name="p4491214"></a><a name="p4491214"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  extendparam field data structure description

    <a name="table52869820"></a>
    <table><thead align="left"><tr id="row50931783"><th class="cellrowborder" valign="top" width="23.932393239323936%" id="mcps1.2.4.1.1"><p id="p31833731"><a name="p31833731"></a><a name="p31833731"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.734273427342735%" id="mcps1.2.4.1.2"><p id="p28395444"><a name="p28395444"></a><a name="p28395444"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18329666"><a name="p18329666"></a><a name="p18329666"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8307988"><td class="cellrowborder" valign="top" width="23.932393239323936%" headers="mcps1.2.4.1.1 "><p id="p1858451"><a name="p1858451"></a><a name="p1858451"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.734273427342735%" headers="mcps1.2.4.1.2 "><p id="p16316838"><a name="p16316838"></a><a name="p16316838"></a>List data structure. For details, see <a href="#table32267243">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16706408"><a name="p16706408"></a><a name="p16706408"></a>Indicates the returned <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  jobs field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.980000000000004%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>String</p>
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

