# Setting Configuration Parameters<a name="en-us_topic_0034973638"></a>

## Function<a name="section4850156117316"></a>

This API is used to set DB instance parameters.

>![](/images/icon-note.gif) **NOTE:**   
>A parameter template \(with same name as the DB instance\) will be created if needed.  

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{nodeId\}/parameters

    Method: PUT

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="21.490000000000002%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.27%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.239999999999995%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.27%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p59352878163330"><a name="p59352878163330"></a><a name="p59352878163330"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>nodeId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.27%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions
    -   The values of the edited parameters must be within the default value range of the specified database version. For details about the range of parameter values, see the "Modifying Parameters in a Parameter Template" section in the  _Relational Database Service User Guide_.
    -   If a parameter of the primary DB instance is modified, the corresponding parameter of the standby DB instance is modified simultaneously. You cannot modify the parameters of the standby DB instance. You can modify the parameters of read replicas.


## Request<a name="section3074340117316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table30427456"></a>
    <table><thead align="left"><tr id="row47542385"><th class="cellrowborder" valign="top" width="21.310000000000002%" id="mcps1.2.4.1.1"><p id="p25727981"><a name="p25727981"></a><a name="p25727981"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.63%" id="mcps1.2.4.1.2"><p id="p3591713"><a name="p3591713"></a><a name="p3591713"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.06%" id="mcps1.2.4.1.3"><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10023380"><td class="cellrowborder" valign="top" width="21.310000000000002%" headers="mcps1.2.4.1.1 "><p id="p6587426"><a name="p6587426"></a><a name="p6587426"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.2 "><p id="p63819464"><a name="p63819464"></a><a name="p63819464"></a>Dictionary data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.4.1.3 "><p id="p17946858"><a name="p17946858"></a><a name="p17946858"></a>Specifies the parameter value list.</p>
    <p id="p3479331719245"><a name="p3479331719245"></a><a name="p3479331719245"></a><strong id="b842352706143230"><a name="b842352706143230"></a><a name="b842352706143230"></a>key</strong> specifies the parameter name. <strong id="b842352706143238"><a name="b842352706143238"></a><a name="b842352706143238"></a>value</strong> specifies the parameter value.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
        "values": {
             "connect_timeout": 17,
             "sync_binlog": 1
        }
    }
    ```


## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table37703499173158"></a>
    <table><thead align="left"><tr id="row66334950173158"><th class="cellrowborder" valign="top" width="27.13%" id="mcps1.2.4.1.1"><p id="p4421832173158"><a name="p4421832173158"></a><a name="p4421832173158"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.2"><p id="p22624127173158"><a name="p22624127173158"></a><a name="p22624127173158"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.88%" id="mcps1.2.4.1.3"><p id="p20615027173158"><a name="p20615027173158"></a><a name="p20615027173158"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59204491173158"><td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.1 "><p id="p30834480173158"><a name="p30834480173158"></a><a name="p30834480173158"></a>shouldRestart</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p14564937173158"><a name="p14564937173158"></a><a name="p14564937173158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p1227762316311"><a name="p1227762316311"></a><a name="p1227762316311"></a>Indicates whether the parameter needs to be restarted for the modifications to take effect.</p>
    <a name="ul199728241833"></a><a name="ul199728241833"></a><ul id="ul199728241833"><li>The value <strong id="b938895142310"><a name="b938895142310"></a><a name="b938895142310"></a>1</strong> indicates that the parameter needs to be restarted for the modifications to take effect.</li><li>The value <strong id="b88721309259"><a name="b88721309259"></a><a name="b88721309259"></a>0</strong> indicates that the parameter does not need to be restarted for the modifications to take effect</li></ul>
    </td>
    </tr>
    <tr id="row14638904173158"><td class="cellrowborder" valign="top" width="27.13%" headers="mcps1.2.4.1.1 "><p id="p44900547173158"><a name="p44900547173158"></a><a name="p44900547173158"></a>setParameteResult</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p13065695173158"><a name="p13065695173158"></a><a name="p13065695173158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p56315328316"><a name="p56315328316"></a><a name="p56315328316"></a>Indicates the parameter modification result.</p>
    <a name="ul199986321133"></a><a name="ul199986321133"></a><ul id="ul199986321133"><li>The value <strong id="b84235270693855"><a name="b84235270693855"></a><a name="b84235270693855"></a>1</strong> indicates that the modifications are successful on the primary DB instance but failed on the standby DB instance.</li><li><strong id="b1836103413259"><a name="b1836103413259"></a><a name="b1836103413259"></a>0</strong> indicates that the modifications are successful on every DB instance.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    { 
         "shouldRestart": "0",
         "setParameteResult": "0" 
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

