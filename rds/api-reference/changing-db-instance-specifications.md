# Changing DB Instance Specifications<a name="en-us_topic_0037365603"></a>

## Function<a name="section4850156117316"></a>

This API is used to change DB instance specifications.

>![](/images/icon-notice.gif) **NOTICE:**   
>Services will be interrupted for 5 to 10 minutes when you change DB instance specifications. Exercise caution when performing this operation.  

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/action

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.08%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.62%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.62%" headers="mcps1.2.4.1.3 "><p id="p57877484163525"><a name="p57877484163525"></a><a name="p57877484163525"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.62%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions
    1.  The new specifications cannot be the same as the original specifications.
    2.  The instance class can be modified only for DB instances whose status is  **Available**.


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table3678226816954"></a>
    <table><thead align="left"><tr id="row1340482316954"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p1204887716954"><a name="p1204887716954"></a><a name="p1204887716954"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p3643495116954"><a name="p3643495116954"></a><a name="p3643495116954"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6554990116954"><a name="p6554990116954"></a><a name="p6554990116954"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row794180116954"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p3930611216954"><a name="p3930611216954"></a><a name="p3930611216954"></a>resize</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p2967852416954"><a name="p2967852416954"></a><a name="p2967852416954"></a>Dictionary data structure. For details, see <a href="#table5971833216954">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3798745816954"><a name="p3798745816954"></a><a name="p3798745816954"></a>Specifies the information about the returned parameter <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>flavorRef</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  resize field data structure description

    <a name="table5971833216954"></a>
    <table><thead align="left"><tr id="row3797548116954"><th class="cellrowborder" valign="top" width="24.5%" id="mcps1.2.4.1.1"><p id="p5611509816954"><a name="p5611509816954"></a><a name="p5611509816954"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.17%" id="mcps1.2.4.1.2"><p id="p4902912116954"><a name="p4902912116954"></a><a name="p4902912116954"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p1193582716954"><a name="p1193582716954"></a><a name="p1193582716954"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2727794616954"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p23854016161336"><a name="p23854016161336"></a><a name="p23854016161336"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.17%" headers="mcps1.2.4.1.2 "><p id="p5837783016954"><a name="p5837783016954"></a><a name="p5837783016954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p50035813161416"><a name="p50035813161416"></a><a name="p50035813161416"></a>Specifies the specification ID (<strong id="b84235270621110"><a name="b84235270621110"></a><a name="b84235270621110"></a>flavors.id</strong> in the response message in section <a href="obtaining-all-db-instance-specifications.md">Obtaining All DB Instance Specifications</a>).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
    "resize":{
    "flavorRef":"0d922098-553c-4123-80df-e627a1d41a0d"
    }
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  4**  Parameter description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p9439626"><a name="p9439626"></a><a name="p9439626"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p26412257"><a name="p26412257"></a><a name="p26412257"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p59018101"><a name="p59018101"></a><a name="p59018101"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p66727538"><a name="p66727538"></a><a name="p66727538"></a>jobId</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p36221483"><a name="p36221483"></a><a name="p36221483"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48259009"><a name="p48259009"></a><a name="p48259009"></a>Indicates the jobId information.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
    "jobId": [
    "ff8080815703e6de015703e98504001a"
    ]
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

