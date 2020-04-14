# Deleting an EIP Tag<a name="eip_apitag_0003"></a>

## Function<a name="en-us_topic_0201534220_section13639163252413"></a>

This API is used to delete an EIP tag.

## URI<a name="en-us_topic_0201534220_section264093272413"></a>

DELETE /v2.0/\{project\_id\}/publicips/\{publicip\_id\}/tags/\{key\}

[Table 1](#en-us_topic_0201534220_table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534220_table27380479"></a>
<table><thead align="left"><tr id="en-us_topic_0201534220_row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534220_p47174532"><a name="en-us_topic_0201534220_p47174532"></a><a name="en-us_topic_0201534220_p47174532"></a><strong id="en-us_topic_0201534220_b1359610281278"><a name="en-us_topic_0201534220_b1359610281278"></a><a name="en-us_topic_0201534220_b1359610281278"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534220_p63040734"><a name="en-us_topic_0201534220_p63040734"></a><a name="en-us_topic_0201534220_p63040734"></a><strong id="en-us_topic_0201534220_b1675704317278"><a name="en-us_topic_0201534220_b1675704317278"></a><a name="en-us_topic_0201534220_b1675704317278"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534220_p6025849"><a name="en-us_topic_0201534220_p6025849"></a><a name="en-us_topic_0201534220_p6025849"></a><strong id="en-us_topic_0201534220_b12791114492711"><a name="en-us_topic_0201534220_b12791114492711"></a><a name="en-us_topic_0201534220_b12791114492711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534220_row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534220_p8478608"><a name="en-us_topic_0201534220_p8478608"></a><a name="en-us_topic_0201534220_p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534220_p15678685"><a name="en-us_topic_0201534220_p15678685"></a><a name="en-us_topic_0201534220_p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534220_p10487112"><a name="en-us_topic_0201534220_p10487112"></a><a name="en-us_topic_0201534220_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534220_row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534220_p43913021"><a name="en-us_topic_0201534220_p43913021"></a><a name="en-us_topic_0201534220_p43913021"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534220_p184914"><a name="en-us_topic_0201534220_p184914"></a><a name="en-us_topic_0201534220_p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534220_p14978051"><a name="en-us_topic_0201534220_p14978051"></a><a name="en-us_topic_0201534220_p14978051"></a>Specifies the unique identifier of an EIP.</p>
</td>
</tr>
<tr id="en-us_topic_0201534220_row172919431459"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534220_p8234174425110"><a name="en-us_topic_0201534220_p8234174425110"></a><a name="en-us_topic_0201534220_p8234174425110"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534220_p11234114455116"><a name="en-us_topic_0201534220_p11234114455116"></a><a name="en-us_topic_0201534220_p11234114455116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534220_p3234194414511"><a name="en-us_topic_0201534220_p3234194414511"></a><a name="en-us_topic_0201534220_p3234194414511"></a>Specifies the tag key.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534220_section6649132102410"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/{project_id}/publicips/{publicip_id}/tags/{key}
    ```


## Response Message<a name="en-us_topic_0201534220_section76491632142420"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="en-us_topic_0201534220_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534220_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

