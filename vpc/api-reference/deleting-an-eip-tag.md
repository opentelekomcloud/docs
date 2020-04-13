# Deleting an EIP Tag<a name="eip_tag_0003"></a>

## Function<a name="section13639163252413"></a>

This API is used to delete an EIP tag.

## URI<a name="section264093272413"></a>

DELETE /v2.0/\{project\_id\}/publicips/\{publicip\_id\}/tags/\{key\}

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b1359610281278"><a name="b1359610281278"></a><a name="b1359610281278"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b1675704317278"><a name="b1675704317278"></a><a name="b1675704317278"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b12791114492711"><a name="b12791114492711"></a><a name="b12791114492711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the unique identifier of an EIP.</p>
</td>
</tr>
<tr id="row172919431459"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8234174425110"><a name="p8234174425110"></a><a name="p8234174425110"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11234114455116"><a name="p11234114455116"></a><a name="p11234114455116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3234194414511"><a name="p3234194414511"></a><a name="p3234194414511"></a>Specifies the tag key.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section6649132102410"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/{project_id}/publicips/{publicip_id}/tags/{key}
    ```


## Response Message<a name="section76491632142420"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

