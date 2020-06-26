# Deleting a Parameter Template<a name="rds_09_0308"></a>

## Function<a name="section17637184617382"></a>

This API is used to delete a specified parameter template.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section4905513413"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

-   Default parameter templates cannot be deleted.

## URI<a name="section16637104613386"></a>

-   URI format

    DELETE https://\{_Endpoint_\}/v3/\{project\_id\}/configurations/\{config\_id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations/463b4b58-d0e8-4e2b-9560-5dea4552fde9

-   Parameter description

    **Table  1**  Parameter description

    <a name="table863711466384"></a>
    <table><thead align="left"><tr id="row1677824653812"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p1777824623819"><a name="p1777824623819"></a><a name="p1777824623819"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.11%" id="mcps1.2.4.1.2"><p id="p7778144611382"><a name="p7778144611382"></a><a name="p7778144611382"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.68000000000001%" id="mcps1.2.4.1.3"><p id="p97787467381"><a name="p97787467381"></a><a name="p97787467381"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1877814464381"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p17778184616386"><a name="p17778184616386"></a><a name="p17778184616386"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.11%" headers="mcps1.2.4.1.2 "><p id="p11778204623816"><a name="p11778204623816"></a><a name="p11778204623816"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p12778154663811"><a name="p12778154663811"></a><a name="p12778154663811"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p929912353618"><a name="p929912353618"></a><a name="p929912353618"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row10778104610388"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1477815462383"><a name="p1477815462383"></a><a name="p1477815462383"></a>config_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.11%" headers="mcps1.2.4.1.2 "><p id="p18778346193815"><a name="p18778346193815"></a><a name="p18778346193815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.68000000000001%" headers="mcps1.2.4.1.3 "><p id="p107781046163816"><a name="p107781046163816"></a><a name="p107781046163816"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36841646163811"></a>

None

## Response<a name="section106841046153811"></a>

-   Normal response

    None

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

