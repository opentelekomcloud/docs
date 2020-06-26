# Deleting a Private IP Address<a name="vpc_privateip_0004"></a>

## Function<a name="section1933992"></a>

This API is used to delete a private IP address.

## URI<a name="section17405935"></a>

DELETE /v1/\{project\_id\}/privateips/\{privateip\_id\}

[Table 1](#table24633528)  describes the parameters.

**Table  1**  Parameter description

<a name="table24633528"></a>
<table><thead align="left"><tr id="row5608311"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p51620080"><a name="p51620080"></a><a name="p51620080"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p20476957"><a name="p20476957"></a><a name="p20476957"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p48020839"><a name="p48020839"></a><a name="p48020839"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64482741"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p55719536"><a name="p55719536"></a><a name="p55719536"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16988543"><a name="p16988543"></a><a name="p16988543"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row36617123"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13196948"><a name="p13196948"></a><a name="p13196948"></a>privateip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62319862"><a name="p62319862"></a><a name="p62319862"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14744048"><a name="p14744048"></a><a name="p14744048"></a>Specifies the ID of the private IP address, which uniquely identifies the private IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section22435692"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1/{project_id}/privateips/4779ab1c-7c1a-44b1-a02e-93dfc361b32d
    ```


## Response Message<a name="section594640"></a>

-   Request parameter

    None

-   Example response

    ```
    None
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

