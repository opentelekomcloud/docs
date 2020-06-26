# Obtaining Detailed Information of a Specified DB Instance<a name="en-us_topic_0032348281"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain detailed information of a specified DB instance.

## URI<a name="section5837609817316"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table3109429217316"></a>
    <table><thead align="left"><tr id="row2968870717316"><th class="cellrowborder" valign="top" width="21.83%" id="mcps1.2.4.1.1"><p id="p5597508117316"><a name="p5597508117316"></a><a name="p5597508117316"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.169999999999998%" id="mcps1.2.4.1.2"><p id="p3768771917316"><a name="p3768771917316"></a><a name="p3768771917316"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p3280643817316"><a name="p3280643817316"></a><a name="p3280643817316"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4007585417316"><td class="cellrowborder" valign="top" width="21.83%" headers="mcps1.2.4.1.1 "><p id="p2491872617316"><a name="p2491872617316"></a><a name="p2491872617316"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p515090217316"><a name="p515090217316"></a><a name="p515090217316"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p47611098163611"><a name="p47611098163611"></a><a name="p47611098163611"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row6402048317316"><td class="cellrowborder" valign="top" width="21.83%" headers="mcps1.2.4.1.1 "><p id="p1827664817316"><a name="p1827664817316"></a><a name="p1827664817316"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p401350517316"><a name="p401350517316"></a><a name="p401350517316"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Normal Response<a name="section6468780017316"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table2020428417316"></a>
    <table><thead align="left"><tr id="row3428628317316"><th class="cellrowborder" valign="top" width="21.98%" id="mcps1.2.4.1.1"><p id="p2572551517316"><a name="p2572551517316"></a><a name="p2572551517316"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.589999999999996%" id="mcps1.2.4.1.2"><p id="p339198017316"><a name="p339198017316"></a><a name="p339198017316"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.43%" id="mcps1.2.4.1.3"><p id="p631496517316"><a name="p631496517316"></a><a name="p631496517316"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4175019117316"><td class="cellrowborder" valign="top" width="21.98%" headers="mcps1.2.4.1.1 "><p id="p2632233817316"><a name="p2632233817316"></a><a name="p2632233817316"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p5173461317316"><a name="p5173461317316"></a><a name="p5173461317316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p71201322697"><a name="p71201322697"></a><a name="p71201322697"></a>Indicates the primary node ID of the DB instance.</p>
    <div class="note" id="note1412012221797"><a name="note1412012221797"></a><a name="note1412012221797"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p141206221195"><a name="p141206221195"></a><a name="p141206221195"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row254286717316"><td class="cellrowborder" valign="top" width="21.98%" headers="mcps1.2.4.1.1 "><p id="p464564917316"><a name="p464564917316"></a><a name="p464564917316"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p4075325517316"><a name="p4075325517316"></a><a name="p4075325517316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p1267935817316"><a name="p1267935817316"></a><a name="p1267935817316"></a>Indicates the DB instance status.</p>
    <div class="p" id="p620854315015"><a name="p620854315015"></a><a name="p620854315015"></a>Value:<a name="ul3066104695748"></a><a name="ul3066104695748"></a><ul id="ul3066104695748"><li>If the value is <strong id="b84235270616547_1"><a name="b84235270616547_1"></a><a name="b84235270616547_1"></a>BUILD</strong>, the instance is being created.</li><li>If the value is <strong id="b842352706165415"><a name="b842352706165415"></a><a name="b842352706165415"></a>ACTIVE</strong>, the instance is normal.</li><li>If the value is <strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>FAILED</strong>, the instance is abnormal.</li><li>If the value is <strong id="b84235270616547_3"><a name="b84235270616547_3"></a><a name="b84235270616547_3"></a>MODIFYING</strong>, the instance is being scaled up.</li><li>If the value is <strong id="b84235270616547_5"><a name="b84235270616547_5"></a><a name="b84235270616547_5"></a>REBOOTING</strong>, the instance is being rebooted.</li><li>If the value is <strong id="b84235270616547_7"><a name="b84235270616547_7"></a><a name="b84235270616547_7"></a>RESTORING</strong>, the instance is being restored.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row4700536117316"><td class="cellrowborder" valign="top" width="21.98%" headers="mcps1.2.4.1.1 "><p id="p4933790017316"><a name="p4933790017316"></a><a name="p4933790017316"></a>instanceName</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p3694693917316"><a name="p3694693917316"></a><a name="p3694693917316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p3991207117316"><a name="p3991207117316"></a><a name="p3991207117316"></a>Indicates the created DB instance name.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "instance": {
            "instanceId": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "instanceName": "rds-instance-test01"
        }
    }
    ```


## Abnormal Response<a name="section4885744117316"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

