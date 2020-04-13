# Deleting a Floating IP Address<a name="vpc_floatingiP_0005"></a>

## Function<a name="section1285101621658"></a>

This API is used to delete a floating IP address.

## URI<a name="section4025916121658"></a>

DELETE /v2.0/floatingips/\{floatingip\_id\}

[Table 1](#table49321613135118)  describes the parameters.

**Table  1**  Parameter description

<a name="table49321613135118"></a>
<table><thead align="left"><tr id="row89331813135112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p116676362558"><a name="p116676362558"></a><a name="p116676362558"></a><strong id="b17651848105713"><a name="b17651848105713"></a><a name="b17651848105713"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p16671836175513"><a name="p16671836175513"></a><a name="p16671836175513"></a><strong id="b3655164915717"><a name="b3655164915717"></a><a name="b3655164915717"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1766716366555"><a name="p1766716366555"></a><a name="p1766716366555"></a><strong id="b1980395018576"><a name="b1980395018576"></a><a name="b1980395018576"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p116679360559"><a name="p116679360559"></a><a name="p116679360559"></a><strong id="b138701551205713"><a name="b138701551205713"></a><a name="b138701551205713"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4934113125120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1036313125105"><a name="p1036313125105"></a><a name="p1036313125105"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p11667113619558"><a name="p11667113619558"></a><a name="p11667113619558"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p26672036175513"><a name="p26672036175513"></a><a name="p26672036175513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p566713367557"><a name="p566713367557"></a><a name="p566713367557"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section5856898621658"></a>

None

## Response Message<a name="section1555365521658"></a>

None

## Example:<a name="section6432601621658"></a>

Example request

```
DELETE https://{Endpoint}/v2.0/floatingips/a95ec431-8473-463b-aede-34fb048ee3a7
```

Example response

None

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

