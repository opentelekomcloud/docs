# NAT Gateway Metrics<a name="EN-US_TOPIC_0171212544"></a>

## Function<a name="section59820001153251"></a>

This section describes metrics reported by NAT Gateway to Cloud Eye as well as their namespaces, list, and dimensions. You can use APIs provided by Cloud Eye to query the metric information generated for NAT Gateway.

## Namespace<a name="section172651386227"></a>

SYS.NAT

## Metrics<a name="section18266133811225"></a>

<a name="table102675383222"></a>
<table><thead align="left"><tr id="row726893842214"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.6.1.1"><p id="p20269183892219"><a name="p20269183892219"></a><a name="p20269183892219"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.1.6.1.2"><p id="p16270153816220"><a name="p16270153816220"></a><a name="p16270153816220"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363637%" id="mcps1.1.6.1.3"><p id="p527115383221"><a name="p527115383221"></a><a name="p527115383221"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.1.6.1.4"><p id="p202711238192210"><a name="p202711238192210"></a><a name="p202711238192210"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.6.1.5"><p id="p52723385226"><a name="p52723385226"></a><a name="p52723385226"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row2272193812219"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.6.1.1 "><p id="p149641356171117"><a name="p149641356171117"></a><a name="p149641356171117"></a>snat_connection</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.1.6.1.2 "><p id="p59647568111"><a name="p59647568111"></a><a name="p59647568111"></a>SNAT Connections</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363637%" headers="mcps1.1.6.1.3 "><p id="p14964956111116"><a name="p14964956111116"></a><a name="p14964956111116"></a>Number of SNAT connections initiated by the current user</p>
<p id="p7369230172013"><a name="p7369230172013"></a><a name="p7369230172013"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.6.1.4 "><p id="p896412563116"><a name="p896412563116"></a><a name="p896412563116"></a>≥ 0 counts</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.6.1.5 "><p id="p1964356101112"><a name="p1964356101112"></a><a name="p1964356101112"></a>Active node of NAT Gateway</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section102905383226"></a>

<a name="table13291038182217"></a>
<table><thead align="left"><tr id="row13292153862219"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="p17292638192211"><a name="p17292638192211"></a><a name="p17292638192211"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="p92938385226"><a name="p92938385226"></a><a name="p92938385226"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row1429373812228"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p11777171991217"><a name="p11777171991217"></a><a name="p11777171991217"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p11777101931217"><a name="p11777101931217"></a><a name="p11777101931217"></a>NAT Gateway instance ID</p>
</td>
</tr>
</tbody>
</table>

