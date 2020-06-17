# Deleting a Backup Policy<a name="EN-US_TOPIC_0059304224"></a>

## Function<a name="section21950305"></a>

This API is used to delete the backup policy of a specific ID.

## URI<a name="section63335023"></a>

-   URI format

    DELETE https://\{endpoint\}/v1/\{project\_id\}/policies/\{policy\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table43212483"></a>
    <table><thead align="left"><tr id="row6889384"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p21169251"><a name="p21169251"></a><a name="p21169251"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p36987783"><a name="p36987783"></a><a name="p36987783"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p43220410"><a name="p43220410"></a><a name="p43220410"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p11192359"><a name="p11192359"></a><a name="p11192359"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34165876"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p15972553"><a name="p15972553"></a><a name="p15972553"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18708431"><a name="p18708431"></a><a name="p18708431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p38987949"><a name="p38987949"></a><a name="p38987949"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row35166068"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29879222"><a name="p29879222"></a><a name="p29879222"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p4297933"><a name="p4297933"></a><a name="p4297933"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12588321"><a name="p12588321"></a><a name="p12588321"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p13021081"><a name="p13021081"></a><a name="p13021081"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33144303"></a>

-   Parameter description

None

-   Example request

    ```
    DELETE https://{endpoint}/v1/{project_id}/policies/{policy_id}
    ```


## Response<a name="section29863272"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="section333997"></a>

-   Normal

    <a name="table25961797"></a>
    <table><thead align="left"><tr id="row50404031"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p56194702"><a name="p56194702"></a><a name="p56194702"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p55477038"><a name="p55477038"></a><a name="p55477038"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64455111"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p53481472"><a name="p53481472"></a><a name="p53481472"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p37031937"><a name="p37031937"></a><a name="p37031937"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table46796915"></a>
    <table><thead align="left"><tr id="row36469261"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1220188"><a name="p1220188"></a><a name="p1220188"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p31726399"><a name="p31726399"></a><a name="p31726399"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19701535"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p52320483"><a name="p52320483"></a><a name="p52320483"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p10100724"><a name="p10100724"></a><a name="p10100724"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row23797652"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p48561666"><a name="p48561666"></a><a name="p48561666"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41180913"><a name="p41180913"></a><a name="p41180913"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row35083905"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p23224019"><a name="p23224019"></a><a name="p23224019"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2097402"><a name="p2097402"></a><a name="p2097402"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row18876625"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p52611666"><a name="p52611666"></a><a name="p52611666"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p33686555"><a name="p33686555"></a><a name="p33686555"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row34743547"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62763908"><a name="p62763908"></a><a name="p62763908"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p50711786"><a name="p50711786"></a><a name="p50711786"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row53752891"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p59016886"><a name="p59016886"></a><a name="p59016886"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15638466"><a name="p15638466"></a><a name="p15638466"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

