# Deleting a Subnet Tag<a name="subnet_tag_0003"></a>

## Function<a name="section1585417593211"></a>

This API is used to delete a subnet tag.

## URI<a name="section158544595218"></a>

DELETE /v2.0/\{project\_id\}/subnets/\{subnet\_id\}/tags/\{key\}

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b18516256653"><a name="b18516256653"></a><a name="b18516256653"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b145413570519"><a name="b145413570519"></a><a name="b145413570519"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b1248015585516"><a name="b1248015585516"></a><a name="b1248015585516"></a>Description</strong></p>
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
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
</td>
</tr>
<tr id="row13201559193110"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8234174425110"><a name="p8234174425110"></a><a name="p8234174425110"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11234114455116"><a name="p11234114455116"></a><a name="p11234114455116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3234194414511"><a name="p3234194414511"></a><a name="p3234194414511"></a>Specifies the tag key.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section16861259192119"></a>

Request parameter

None

Example request

```
DELETE https://{Endpoint}/v2.0/{project_id}/subnets/{subnet_id}/tags/{key}
```

## Response Message<a name="section12861195972114"></a>

Response parameter

None

Example response

None

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

