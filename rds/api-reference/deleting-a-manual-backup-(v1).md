# Deleting a Manual Backup<a name="en-us_topic_0037139103"></a>

## Function<a name="section4850156117316"></a>

This API is used to delete a manual backup.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/backups/\{backupId\}

    Method: DELETE

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.01%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.88%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p6304653416317"><a name="p6304653416317"></a><a name="p6304653416317"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row17239382154651"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p20936710154651"><a name="p20936710154651"></a><a name="p20936710154651"></a>backupId</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.2.4.1.2 "><p id="p18151956154651"><a name="p18151956154651"></a><a name="p18151956154651"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p61022371154651"><a name="p61022371154651"></a><a name="p61022371154651"></a>Specifies the backup file ID compliant with the UUID format.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Normal Response<a name="section28521534113742"></a>

\{\}

## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

