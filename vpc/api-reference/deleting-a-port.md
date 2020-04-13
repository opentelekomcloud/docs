# Deleting a Port<a name="vpc_port02_0005"></a>

## Function<a name="en-us_topic_0062207359_section45238241"></a>

This API is used to delete a port.

Restrictions

-   A port with  **device\_owner**  set to a value other than  **neutron:VIP\_PORT**  cannot be deleted.
-   A port with  **device\_id**  specified cannot be deleted.

## URI<a name="en-us_topic_0062207359_section4490990"></a>

DELETE /v2.0/ports/\{port\_id\}

[Table 1](#table1855162528)  describes the parameters.

**Table  1**  Parameter description

<a name="table1855162528"></a>
<table><thead align="left"><tr id="vpc_port02_0002_row1394617591304"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="vpc_port02_0002_p159467591307"><a name="vpc_port02_0002_p159467591307"></a><a name="vpc_port02_0002_p159467591307"></a><strong id="vpc_port02_0002_b5836335194617"><a name="vpc_port02_0002_b5836335194617"></a><a name="vpc_port02_0002_b5836335194617"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="vpc_port02_0002_p1094612597019"><a name="vpc_port02_0002_p1094612597019"></a><a name="vpc_port02_0002_p1094612597019"></a><strong id="vpc_port02_0002_b040313816465"><a name="vpc_port02_0002_b040313816465"></a><a name="vpc_port02_0002_b040313816465"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="vpc_port02_0002_p29466591203"><a name="vpc_port02_0002_p29466591203"></a><a name="vpc_port02_0002_p29466591203"></a><strong id="vpc_port02_0002_b1192918393464"><a name="vpc_port02_0002_b1192918393464"></a><a name="vpc_port02_0002_b1192918393464"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_port02_0002_row1494695918012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="vpc_port02_0002_p9946159600"><a name="vpc_port02_0002_p9946159600"></a><a name="vpc_port02_0002_p9946159600"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="vpc_port02_0002_p09465594017"><a name="vpc_port02_0002_p09465594017"></a><a name="vpc_port02_0002_p09465594017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="vpc_port02_0002_p394618591401"><a name="vpc_port02_0002_p394618591401"></a><a name="vpc_port02_0002_p394618591401"></a>Specifies the port ID, which uniquely identifies the port.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0062207359_section52706911"></a>

None

## Response Message<a name="en-us_topic_0062207359_section4600155"></a>

None

## Example:<a name="en-us_topic_0062207359_section41401397"></a>

Example request

```
DELETE https://{Endpoint}/v2.0/ports/2b098395-046a-4071-b009-312bcee665cb 
```

Example response

None

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

