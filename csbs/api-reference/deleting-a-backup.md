# Deleting a Backup<a name="EN-US_TOPIC_0059304232"></a>

## Function<a name="section24937164"></a>

This API is used to delete a backup.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The deletion operation is asynchronous. Tasks will be queued depending on the background task execution status. Therefore, the deletion will not be completed immediately. You need to query the task information continuously to obtain the deletion result. A maximum of 30 minutes is required.  
>For example, a user can execute a maximum of five backup deletion tasks concurrently. If the number exceeds five, the sixth and subsequent tasks are queued.  

## URI<a name="section23107889"></a>

-   URI format

    DELETE https://\{endpoint\}/v1/\{project\_id\}/providers/\{provider\_id\}/checkpoints/\{checkpoint\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table8558107"></a>
    <table><thead align="left"><tr id="row46491595"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10556491"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49769413"><a name="p49769413"></a><a name="p49769413"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p4790635"><a name="p4790635"></a><a name="p4790635"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p52497191"><a name="p52497191"></a><a name="p52497191"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row18399828"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13991122"><a name="p13991122"></a><a name="p13991122"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p59539072"><a name="p59539072"></a><a name="p59539072"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p57935494"><a name="p57935494"></a><a name="p57935494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p62263437"><a name="p62263437"></a><a name="p62263437"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b20451623192612"><a name="b20451623192612"></a><a name="b20451623192612"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row23500024"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24453795"><a name="p24453795"></a><a name="p24453795"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p34600354"><a name="p34600354"></a><a name="p34600354"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51165278"><a name="p51165278"></a><a name="p51165278"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p50746814"><a name="p50746814"></a><a name="p50746814"></a>Backup record ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section6644414"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table22773387"></a>
    <table><thead align="left"><tr id="row11530445"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p13881956816"><a name="p13881956816"></a><a name="p13881956816"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p178813517810"><a name="p178813517810"></a><a name="p178813517810"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p178811451187"><a name="p178811451187"></a><a name="p178811451187"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p4881855818"><a name="p4881855818"></a><a name="p4881855818"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21960560"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33974975"><a name="p33974975"></a><a name="p33974975"></a>checkpoint_items</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p509623"><a name="p509623"></a><a name="p509623"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p41279487"><a name="p41279487"></a><a name="p41279487"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p55304127"><a name="p55304127"></a><a name="p55304127"></a>Indicates the ID list of the backup records to be deleted. If this parameter is not set, all backup records of <strong id="b59079939"><a name="b59079939"></a><a name="b59079939"></a>checkpoint</strong> will be deleted.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description

    None


-   Example request

    ```
    Deleting all backups in the specified backup record:
    DELETE https://{endpoint}/v1/{project_id}/providers/{provider_id}/checkpoints/{checkpoint_id}
    Deleting a single backup in the specified backup record:
    DELETE https://{endpoint}/v1/{project_id}/providers/{provider_id}/checkpoints/{checkpoint_id}?checkpoint_items={checkpoint_items_id}
    ```


## Response<a name="section59799733"></a>

-   Parameter description

    None


-   Example response

    ```
    { 
    }
    ```


## Status Codes<a name="section1326685"></a>

-   Normal

    <a name="table25788020"></a>
    <table><thead align="left"><tr id="row56719680"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p30891373"><a name="p30891373"></a><a name="p30891373"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p19173303"><a name="p19173303"></a><a name="p19173303"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9533701"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p34032320"><a name="p34032320"></a><a name="p34032320"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p5154511"><a name="p5154511"></a><a name="p5154511"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table14862235"></a>
    <table><thead align="left"><tr id="row17500102"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p8222144"><a name="p8222144"></a><a name="p8222144"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p62013947"><a name="p62013947"></a><a name="p62013947"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57073823"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p59576914"><a name="p59576914"></a><a name="p59576914"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61000767"><a name="p61000767"></a><a name="p61000767"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row12135994"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p43491438"><a name="p43491438"></a><a name="p43491438"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p33145583"><a name="p33145583"></a><a name="p33145583"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row29874791"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3939013"><a name="p3939013"></a><a name="p3939013"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p50624676"><a name="p50624676"></a><a name="p50624676"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row52968908"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62623118"><a name="p62623118"></a><a name="p62623118"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p39307813"><a name="p39307813"></a><a name="p39307813"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row18226004"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p67020229"><a name="p67020229"></a><a name="p67020229"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59929470"><a name="p59929470"></a><a name="p59929470"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row2494326"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p713839"><a name="p713839"></a><a name="p713839"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p57820997"><a name="p57820997"></a><a name="p57820997"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

