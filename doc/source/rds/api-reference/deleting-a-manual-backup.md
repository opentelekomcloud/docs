# Deleting a Manual Backup<a name="rds_09_0007"></a>

## Function<a name="section117711820496"></a>

This API is used to delete a manual backup.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section12081471012"></a>

-   URI format

    DELETE https://\{_Endpoint_\}/v3/\{project\_id\}/backups/\{backup\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/backups/2f4ddb93-b901-4b08-93d8-1d2e472f30fe

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p14969328081"><a name="p14969328081"></a><a name="p14969328081"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row98887351976"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10889153513710"><a name="p10889153513710"></a><a name="p10889153513710"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p208892356711"><a name="p208892356711"></a><a name="p208892356711"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38891335874"><a name="p38891335874"></a><a name="p38891335874"></a>Specifies the ID of the manual backup.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section420839121019"></a>

None

## Response<a name="section1229512143106"></a>

-   Normal response

    None

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

