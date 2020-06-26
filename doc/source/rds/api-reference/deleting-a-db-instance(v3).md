# Deleting a DB Instance<a name="rds_01_0003"></a>

## Function<a name="section4284989"></a>

This API is used to delete a DB instance.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section38564907"></a>

-   URI format

    DELETE https://\{_Endpoint_\}/v3/\{project\_id\}/instances/\{instance\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/instances/dsfae23fsfdsae3435in01

-   Parameter description

    **Table  1**  Parameter description

    <a name="table65777232"></a>
    <table><thead align="left"><tr id="row46529701"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10809459"><a name="p10809459"></a><a name="p10809459"></a><strong id="b9296112613193"><a name="b9296112613193"></a><a name="b9296112613193"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3150961"><a name="p3150961"></a><a name="p3150961"></a><strong id="b0858729171912"><a name="b0858729171912"></a><a name="b0858729171912"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p53901255"><a name="p53901255"></a><a name="p53901255"></a><strong id="b14869123081916"><a name="b14869123081916"></a><a name="b14869123081916"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3925534"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49532829"><a name="p49532829"></a><a name="p49532829"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52736237"><a name="p52736237"></a><a name="p52736237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p178064411566"><a name="p178064411566"></a><a name="p178064411566"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row19402550154517"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1046217474614"><a name="p1046217474614"></a><a name="p1046217474614"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p246284104619"><a name="p246284104619"></a><a name="p246284104619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18462124174611"><a name="p18462124174611"></a><a name="p18462124174611"></a>Specifies the DB instance ID compliant with the UUID format.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1390010340492"></a>

None

## Response<a name="section36749739"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table17474517"></a>
    <table><thead align="left"><tr id="row16146366"><th class="cellrowborder" valign="top" width="26.38%" id="mcps1.2.4.1.1"><p id="p32787233"><a name="p32787233"></a><a name="p32787233"></a><strong id="b1095164516326"><a name="b1095164516326"></a><a name="b1095164516326"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.29%" id="mcps1.2.4.1.2"><p id="p38520254"><a name="p38520254"></a><a name="p38520254"></a><strong id="b231334618324"><a name="b231334618324"></a><a name="b231334618324"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p33132859"><a name="p33132859"></a><a name="p33132859"></a><strong id="b11276447183217"><a name="b11276447183217"></a><a name="b11276447183217"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1625804435012"><td class="cellrowborder" valign="top" width="26.38%" headers="mcps1.2.4.1.1 "><p id="p1165525810503"><a name="p1165525810503"></a><a name="p1165525810503"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.29%" headers="mcps1.2.4.1.2 "><p id="p116551958135013"><a name="p116551958135013"></a><a name="p116551958135013"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p16655115865012"><a name="p16655115865012"></a><a name="p16655115865012"></a>Indicates the ID of the instance deletion task.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    ```
    {
    	"job_id": "dff1d289-4d03-4942-8b9f-463ea07c000d"
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

