# Deleting an IPsec Policy<a name="en_topic_0093011508"></a>

## **Function**<a name="section44896221"></a>

This interface is used to delete an IPsec policy.

## URI<a name="section1412808"></a>

DELETE /v2.0/vpn/ipsecpolicies/\{ipsecpolicy\_id\}

**Table  1**  Parameter description

<a name="table44973181017"></a>
<table><thead align="left"><tr id="row15504918204"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1550413181805"><a name="p1550413181805"></a><a name="p1550413181805"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p135113181904"><a name="p135113181904"></a><a name="p135113181904"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p45111018804"><a name="p45111018804"></a><a name="p45111018804"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p125111818109"><a name="p125111818109"></a><a name="p125111818109"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1151910188014"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p11519418808"><a name="p11519418808"></a><a name="p11519418808"></a>ipsecpolicy_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p051911182003"><a name="p051911182003"></a><a name="p051911182003"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p125198181109"><a name="p125198181109"></a><a name="p125198181109"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1651921810014"><a name="p1651921810014"></a><a name="p1651921810014"></a>Specifies the IPsec policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section47328638"></a>

None

## Response Message<a name="section23304563"></a>

None

## Example<a name="section8414476"></a>

-   Example Request

```
DELETE /v2.0/vpn/ipsecpolicies/{ipsecpolicy_id}
```

-   Example Response

    None


## Returned Values<a name="section6578292"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

