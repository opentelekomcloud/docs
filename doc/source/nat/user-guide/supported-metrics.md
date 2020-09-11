# Supported Metrics<a name="nat_ces_0002"></a>

## Description<a name="section352319314226"></a>

This section describes metrics reported by NAT Gateway to Cloud Eye as well as their namespaces, monitoring metrics, and dimensions. You can use the management console or the APIs provided by Cloud Eye to query the metrics generated for NAT Gateway.

## Namespace<a name="section48641254172217"></a>

SYS.NAT

## Monitoring Metrics<a name="section1954874112249"></a>

<a name="table102675383222"></a>
<table><thead align="left"><tr id="row726893842214"><th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.1.7.1.1"><p id="p20269183892219"><a name="p20269183892219"></a><a name="p20269183892219"></a><strong id="b2632172310345"><a name="b2632172310345"></a><a name="b2632172310345"></a>Metric</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.1.7.1.2"><p id="p16270153816220"><a name="p16270153816220"></a><a name="p16270153816220"></a><strong id="b11883142563415"><a name="b11883142563415"></a><a name="b11883142563415"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.1.7.1.3"><p id="p527115383221"><a name="p527115383221"></a><a name="p527115383221"></a><strong id="b84235270619454"><a name="b84235270619454"></a><a name="b84235270619454"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.1.7.1.4"><p id="p202711238192210"><a name="p202711238192210"></a><a name="p202711238192210"></a><strong id="b84235270621366"><a name="b84235270621366"></a><a name="b84235270621366"></a>Value Range</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.1.7.1.5"><p id="p52723385226"><a name="p52723385226"></a><a name="p52723385226"></a><strong id="b29933953513"><a name="b29933953513"></a><a name="b29933953513"></a>Measurement Object &amp; Dimension</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.1.7.1.6"><p id="p12656105763615"><a name="p12656105763615"></a><a name="p12656105763615"></a><strong id="b426716527349"><a name="b426716527349"></a><a name="b426716527349"></a>Monitoring Interval (Raw Data)</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2272193812219"><td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.7.1.1 "><p id="p149641356171117"><a name="p149641356171117"></a><a name="p149641356171117"></a>snat_connection</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.7.1.2 "><p id="p59647568111"><a name="p59647568111"></a><a name="p59647568111"></a>SNAT connections</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.7.1.3 "><p id="p14964956111116"><a name="p14964956111116"></a><a name="p14964956111116"></a>Specifies the number of SNAT connections of the measurement object.</p>
<p id="p7369230172013"><a name="p7369230172013"></a><a name="p7369230172013"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.4 "><p id="p896412563116"><a name="p896412563116"></a><a name="p896412563116"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.7.1.5 "><p id="p1964356101112"><a name="p1964356101112"></a><a name="p1964356101112"></a>Measurement object: Active NAT gateway node</p>
<p id="p823153843717"><a name="p823153843717"></a><a name="p823153843717"></a>Dimension:</p>
<p id="p125462015382"><a name="p125462015382"></a><a name="p125462015382"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.7.1.6 "><p id="p765645713612"><a name="p765645713612"></a><a name="p765645713612"></a>5 minutes</p>
</td>
</tr>
<tr id="row1348614455913"><td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.7.1.1 "><p id="p748617451398"><a name="p748617451398"></a><a name="p748617451398"></a>Server IP address set</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.7.1.2 "><p id="p62811656991"><a name="p62811656991"></a><a name="p62811656991"></a>IP address set of the top 10 servers occupying the largest number of SNAT connections</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.7.1.3 "><p id="p92811561694"><a name="p92811561694"></a><a name="p92811561694"></a>Specifies the IP addresses of top 10 servers that occupy the largest number of SNAT connections.</p>
<p id="p853183420433"><a name="p853183420433"></a><a name="p853183420433"></a>Unit: Count</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.4 "><p id="p1528116561917"><a name="p1528116561917"></a><a name="p1528116561917"></a>≥ 0</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.1.7.1.5 "><p id="p57816332325"><a name="p57816332325"></a><a name="p57816332325"></a>Measurement object: NAT gateway</p>
<p id="p153301940183513"><a name="p153301940183513"></a><a name="p153301940183513"></a>Dimension:</p>
<p id="p93301940163514"><a name="p93301940163514"></a><a name="p93301940163514"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.1.7.1.6 "><p id="p1148634517920"><a name="p1148634517920"></a><a name="p1148634517920"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimensions<a name="section11173113215254"></a>

<a name="en-us_topic_0102475743_table13291038182217"></a>
<table><thead align="left"><tr id="en-us_topic_0102475743_row13292153862219"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="en-us_topic_0102475743_p17292638192211"><a name="en-us_topic_0102475743_p17292638192211"></a><a name="en-us_topic_0102475743_p17292638192211"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="en-us_topic_0102475743_p92938385226"><a name="en-us_topic_0102475743_p92938385226"></a><a name="en-us_topic_0102475743_p92938385226"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102475743_row1429373812228"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0102475743_p11777171991217"><a name="en-us_topic_0102475743_p11777171991217"></a><a name="en-us_topic_0102475743_p11777171991217"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0102475743_p11777101931217"><a name="en-us_topic_0102475743_p11777101931217"></a><a name="en-us_topic_0102475743_p11777101931217"></a>NAT gateway ID</p>
</td>
</tr>
</tbody>
</table>

