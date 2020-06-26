# Deleting a Network<a name="vpc_network_0005"></a>

## Function<a name="section43031324205035"></a>

This API is used to delete a network.

## URI<a name="section29996404205035"></a>

DELETE /v2.0/networks/\{network\_id\}

[Table 1](#table1710134691014)  describes the parameters.

**Table  1**  Parameter description

<a name="table1710134691014"></a>
<table><thead align="left"><tr id="vpc_network_0002_row1775694617109"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="vpc_network_0002_p775644621011"><a name="vpc_network_0002_p775644621011"></a><a name="vpc_network_0002_p775644621011"></a><strong id="vpc_network_0002_b78438591578"><a name="vpc_network_0002_b78438591578"></a><a name="vpc_network_0002_b78438591578"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="vpc_network_0002_p575674618101"><a name="vpc_network_0002_p575674618101"></a><a name="vpc_network_0002_p575674618101"></a><strong id="vpc_network_0002_b75895085819"><a name="vpc_network_0002_b75895085819"></a><a name="vpc_network_0002_b75895085819"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="vpc_network_0002_p17568468102"><a name="vpc_network_0002_p17568468102"></a><a name="vpc_network_0002_p17568468102"></a><strong id="vpc_network_0002_b154271011583"><a name="vpc_network_0002_b154271011583"></a><a name="vpc_network_0002_b154271011583"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_network_0002_row875634651011"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="vpc_network_0002_p8756154610104"><a name="vpc_network_0002_p8756154610104"></a><a name="vpc_network_0002_p8756154610104"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="vpc_network_0002_p37561846191013"><a name="vpc_network_0002_p37561846191013"></a><a name="vpc_network_0002_p37561846191013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="vpc_network_0002_p1375624661014"><a name="vpc_network_0002_p1375624661014"></a><a name="vpc_network_0002_p1375624661014"></a>Specifies the network ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section54655929205035"></a>

None

## Response Message<a name="section48616095205035"></a>

None

## Example:<a name="section7653394205035"></a>

Example request

```
DELETE https://{Endpoint}/v2.0/networks/60c809cb-6731-45d0-ace8-3bf5626421a9
```

Example response

None

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

