# Deleting an FPGA Image<a name="EN-US_TOPIC_0065962599"></a>

## Function<a name="section19527005211725"></a>

This API is used to delete an FPGA image.

## URI<a name="section38661040211725"></a>

DELETE /v1/\{project\_id\}/cloudservers/fpga\_image/\{fpga\_image\_id\}

[Table 1](#table44329634211725)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table44329634211725"></a>
<table><thead align="left"><tr id="row41557603211725"><th class="cellrowborder" valign="top" width="19.53%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.599999999999998%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.870000000000005%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55081924211725"><td class="cellrowborder" valign="top" width="19.53%" headers="mcps1.2.4.1.1 "><p id="p50162201211725"><a name="p50162201211725"></a><a name="p50162201211725"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p27862189211725"><a name="p27862189211725"></a><a name="p27862189211725"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.870000000000005%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row30180665211725"><td class="cellrowborder" valign="top" width="19.53%" headers="mcps1.2.4.1.1 "><p id="p44186266211725"><a name="p44186266211725"></a><a name="p44186266211725"></a>fpga_image_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.2.4.1.2 "><p id="p17752625211725"><a name="p17752625211725"></a><a name="p17752625211725"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.870000000000005%" headers="mcps1.2.4.1.3 "><p id="p33122615211725"><a name="p33122615211725"></a><a name="p33122615211725"></a>Specifies the FPGA image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section49362668211725"></a>

None

## Response<a name="section34595306211725"></a>

None

## Example Request<a name="section20514490211725"></a>

```
DELETE https://{endpoint}/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}
```

## Example Response<a name="section142498762720"></a>

None

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

