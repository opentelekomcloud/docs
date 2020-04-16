# Deleting a DB Instance<a name="en-us_topic_0056890052"></a>

## Function<a name="section36524518102048"></a>

This API is used to delete a DB instance.

## URI<a name="section51263775102048"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/instances/\{instanceId\}

    Method: DELETE

-   Parameter description

    **Table  1**  Parameter description

    <a name="table10271366102048"></a>
    <table><thead align="left"><tr id="row47701174102048"><th class="cellrowborder" valign="top" width="26.240000000000002%" id="mcps1.2.4.1.1"><p id="p4909390317443"><a name="p4909390317443"></a><a name="p4909390317443"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.77%" id="mcps1.2.4.1.2"><p id="p2043144817443"><a name="p2043144817443"></a><a name="p2043144817443"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.99%" id="mcps1.2.4.1.3"><p id="p6346699117443"><a name="p6346699117443"></a><a name="p6346699117443"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row105028141826"><td class="cellrowborder" valign="top" width="26.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p40108143174242"><a name="p40108143174242"></a><a name="p40108143174242"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.77%" headers="mcps1.2.4.1.2 "><p id="p27534111174242"><a name="p27534111174242"></a><a name="p27534111174242"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.99%" headers="mcps1.2.4.1.3 "><p id="p15670491174242"><a name="p15670491174242"></a><a name="p15670491174242"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row65712913102048"><td class="cellrowborder" valign="top" width="26.240000000000002%" headers="mcps1.2.4.1.1 "><p id="p57964633112316"><a name="p57964633112316"></a><a name="p57964633112316"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.77%" headers="mcps1.2.4.1.2 "><p id="p64623711112316"><a name="p64623711112316"></a><a name="p64623711112316"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.99%" headers="mcps1.2.4.1.3 "><p id="p3975356017443"><a name="p3975356017443"></a><a name="p3975356017443"></a>Specifies the ID of the DB instance to be deleted.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    -   The standby DB instance cannot be deleted.
    -   All automated backups will be deleted and all manual backups will be retained.
    -   Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section11352400112951"></a>

None

## Normal Response<a name="section13572792102048"></a>

None

## Abnormal Response<a name="section64738761102048"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

