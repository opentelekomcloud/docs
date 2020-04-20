# Resetting Parameters to Their Default Values<a name="en-us_topic_0034973639"></a>

## Function<a name="section4850156117316"></a>

This API is used to reset parameters of a specified DB instance to their default values.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{nodeId\}/parameters/default

    Method: PUT

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4657088"></a>
    <table><thead align="left"><tr id="row60083059"><th class="cellrowborder" valign="top" width="20.36%" id="mcps1.2.4.1.1"><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.2%" id="mcps1.2.4.1.2"><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57385070"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="p17679057"><a name="p17679057"></a><a name="p17679057"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p22717550"><a name="p22717550"></a><a name="p22717550"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p53254067163252"><a name="p53254067163252"></a><a name="p53254067163252"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row2864326155157"><td class="cellrowborder" valign="top" width="20.36%" headers="mcps1.2.4.1.1 "><p id="p41557789155220"><a name="p41557789155220"></a><a name="p41557789155220"></a>nodeId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2%" headers="mcps1.2.4.1.2 "><p id="p10737742155220"><a name="p10737742155220"></a><a name="p10737742155220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Restrictions
    -   If a parameter of the primary DB instance is reset to the default value, the corresponding parameter of the standby DB instance is reset to the default setting simultaneously. You cannot reset the parameters of the standby DB instance to their default values. You can reset the parameters of read replicas to their default values.


## Request<a name="section3074340117316"></a>

\{\}

Note: Curly brackets \{\} indicate that the API does not obtain the data in the request body.

## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table37703499173158"></a>
    <table><thead align="left"><tr id="row66334950173158"><th class="cellrowborder" valign="top" width="27.500000000000004%" id="mcps1.2.4.1.1"><p id="p4421832173158"><a name="p4421832173158"></a><a name="p4421832173158"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p22624127173158"><a name="p22624127173158"></a><a name="p22624127173158"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.25%" id="mcps1.2.4.1.3"><p id="p20615027173158"><a name="p20615027173158"></a><a name="p20615027173158"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59204491173158"><td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.4.1.1 "><p id="p30834480173158"><a name="p30834480173158"></a><a name="p30834480173158"></a>shouldRestart</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p14564937173158"><a name="p14564937173158"></a><a name="p14564937173158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.25%" headers="mcps1.2.4.1.3 "><p id="p13250943137"><a name="p13250943137"></a><a name="p13250943137"></a>Indicates whether the parameter needs to be restarted for the modifications to take effect.</p>
    <a name="ul342717448317"></a><a name="ul342717448317"></a><ul id="ul342717448317"><li>The value <strong id="b1757161015273"><a name="b1757161015273"></a><a name="b1757161015273"></a>1</strong> indicates that the parameter needs to be restarted for the modifications to take effect.</li><li>The value <strong id="b14865131312276"><a name="b14865131312276"></a><a name="b14865131312276"></a>0</strong> indicates that the parameter does not need to be restarted for the modifications to take effect</li></ul>
    </td>
    </tr>
    <tr id="row14638904173158"><td class="cellrowborder" valign="top" width="27.500000000000004%" headers="mcps1.2.4.1.1 "><p id="p44900547173158"><a name="p44900547173158"></a><a name="p44900547173158"></a>setParameteResult</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p13065695173158"><a name="p13065695173158"></a><a name="p13065695173158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.25%" headers="mcps1.2.4.1.3 "><p id="p193406491335"><a name="p193406491335"></a><a name="p193406491335"></a>Indicates the parameter modification result.</p>
    <a name="ul16867105018312"></a><a name="ul16867105018312"></a><ul id="ul16867105018312"><li>The value <strong id="b18739171512711"><a name="b18739171512711"></a><a name="b18739171512711"></a>1</strong> indicates that the modifications are successful on the primary DB instance but failed on the standby DB instance.</li><li><strong id="b17571161618271"><a name="b17571161618271"></a><a name="b17571161618271"></a>0</strong> indicates that the modifications are successful on every DB instance.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    { 
         "shouldRestart": "1",
         "setParameteResult": "0"
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

