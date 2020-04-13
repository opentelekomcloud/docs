# Deleting a Firewall Policy<a name="vpc_firewall_0010"></a>

## Function<a name="section2007643132549"></a>

This API is used to delete a firewall policy.

## URI<a name="section2168718132549"></a>

DELETE /v2.0/fwaas/firewall\_policies/\{firewall\_policy\_id\}

[Table 1](#table18880184689)  describes the parameters.

**Table  1**  Parameter description

<a name="table18880184689"></a>
<table><thead align="left"><tr id="row13968641385"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p209684410817"><a name="p209684410817"></a><a name="p209684410817"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p69681441386"><a name="p69681441386"></a><a name="p69681441386"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.5.1.3"><p id="p1096813412811"><a name="p1096813412811"></a><a name="p1096813412811"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.5.1.4"><p id="p139686416813"><a name="p139686416813"></a><a name="p139686416813"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19681041189"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1682422682817"><a name="p1682422682817"></a><a name="p1682422682817"></a>firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1797015416817"><a name="p1797015416817"></a><a name="p1797015416817"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.5.1.3 "><p id="p19701411813"><a name="p19701411813"></a><a name="p19701411813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.5.1.4 "><p id="p109701641488"><a name="p109701641488"></a><a name="p109701641488"></a>Specifies the firewall policy ID, which uniquely identifies the firewall policy.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section31261317132549"></a>

None

## Response Message<a name="section40411496132549"></a>

None

## Example:<a name="section10091651132549"></a>

Example request

```
DELETE https://{Endpoint}/v2.0/fwaas/firewall_policies/2fb0e81f-9f63-44b2-9894-c13a3284594a
```

Example response

None

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

