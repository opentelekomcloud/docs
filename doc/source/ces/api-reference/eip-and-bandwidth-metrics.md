# EIP and Bandwidth Metrics<a name="EN-US_TOPIC_0171212586"></a>

## Function<a name="s4d3199bf99ec4230b43792a4dc2c02a4"></a>

This section describes the namespace, list, and dimensions of EIP and Bandwidth metrics on Cloud Eye. You can use APIs provided by Cloud Eye to query the metrics of the monitored object and alarms generated for EIP and Bandwidth.

## Namespace<a name="sc26b78984c0d44a69af4eaf6c453585b"></a>

SYS.VPC

## Metrics<a name="s1d6be673bc4e43c49b1917bc610074e7"></a>

<a name="table1148615265912"></a>
<table><thead align="left"><tr id="row1248762165917"><th class="cellrowborder" valign="top" width="19.000000000000004%" id="mcps1.1.6.1.1"><p id="p19487162115911"><a name="p19487162115911"></a><a name="p19487162115911"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.000000000000004%" id="mcps1.1.6.1.2"><p id="p1548712135916"><a name="p1548712135916"></a><a name="p1548712135916"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="29.000000000000004%" id="mcps1.1.6.1.3"><p id="p348742165919"><a name="p348742165919"></a><a name="p348742165919"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000004%" id="mcps1.1.6.1.4"><p id="p54871235918"><a name="p54871235918"></a><a name="p54871235918"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="22.000000000000004%" id="mcps1.1.6.1.5"><p id="p64871627593"><a name="p64871627593"></a><a name="p64871627593"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row18489122595"><td class="cellrowborder" valign="top" width="19.000000000000004%" headers="mcps1.1.6.1.1 "><p id="p74894285920"><a name="p74894285920"></a><a name="p74894285920"></a>upstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.000000000000004%" headers="mcps1.1.6.1.2 "><p id="p84891126596"><a name="p84891126596"></a><a name="p84891126596"></a>Outbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="29.000000000000004%" headers="mcps1.1.6.1.3 "><p id="p114894216591"><a name="p114894216591"></a><a name="p114894216591"></a>Network rate of outbound traffic </p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000004%" headers="mcps1.1.6.1.4 "><p id="p154891211593"><a name="p154891211593"></a><a name="p154891211593"></a>≥ 0 bits/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.6.1.5 "><p id="p1448952185916"><a name="p1448952185916"></a><a name="p1448952185916"></a>Bandwidth or EIP</p>
</td>
</tr>
<tr id="row048982135916"><td class="cellrowborder" valign="top" width="19.000000000000004%" headers="mcps1.1.6.1.1 "><p id="p20489225598"><a name="p20489225598"></a><a name="p20489225598"></a>downstream_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.000000000000004%" headers="mcps1.1.6.1.2 "><p id="p1348962195911"><a name="p1348962195911"></a><a name="p1348962195911"></a>Inbound Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="29.000000000000004%" headers="mcps1.1.6.1.3 "><p id="p164891826592"><a name="p164891826592"></a><a name="p164891826592"></a>Network rate of inbound traffic </p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000004%" headers="mcps1.1.6.1.4 "><p id="p1748912217599"><a name="p1748912217599"></a><a name="p1748912217599"></a>≥ 0 bits/s</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.6.1.5 "><p id="p1548913213598"><a name="p1548913213598"></a><a name="p1548913213598"></a>Bandwidth or EIP</p>
</td>
</tr>
<tr id="row174911126594"><td class="cellrowborder" valign="top" width="19.000000000000004%" headers="mcps1.1.6.1.1 "><p id="p7491121596"><a name="p7491121596"></a><a name="p7491121596"></a>up_stream</p>
</td>
<td class="cellrowborder" valign="top" width="16.000000000000004%" headers="mcps1.1.6.1.2 "><p id="p18491202135916"><a name="p18491202135916"></a><a name="p18491202135916"></a>Outbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="29.000000000000004%" headers="mcps1.1.6.1.3 "><p id="p0491328599"><a name="p0491328599"></a><a name="p0491328599"></a>Network traffic going out of the cloud platform </p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000004%" headers="mcps1.1.6.1.4 "><p id="p1449118285910"><a name="p1449118285910"></a><a name="p1449118285910"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.6.1.5 "><p id="p849172165919"><a name="p849172165919"></a><a name="p849172165919"></a>Bandwidth or EIP</p>
</td>
</tr>
<tr id="row164911922591"><td class="cellrowborder" valign="top" width="19.000000000000004%" headers="mcps1.1.6.1.1 "><p id="p134918218594"><a name="p134918218594"></a><a name="p134918218594"></a>down_stream</p>
</td>
<td class="cellrowborder" valign="top" width="16.000000000000004%" headers="mcps1.1.6.1.2 "><p id="p1349112155912"><a name="p1349112155912"></a><a name="p1349112155912"></a>Inbound Traffic</p>
</td>
<td class="cellrowborder" valign="top" width="29.000000000000004%" headers="mcps1.1.6.1.3 "><p id="p1849115217593"><a name="p1849115217593"></a><a name="p1849115217593"></a>Network traffic going into the cloud platform </p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000004%" headers="mcps1.1.6.1.4 "><p id="p164912235918"><a name="p164912235918"></a><a name="p164912235918"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.1.6.1.5 "><p id="p04911255910"><a name="p04911255910"></a><a name="p04911255910"></a>Bandwidth or EIP</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="sbed2cc4b637744078092d8c79edd95e8"></a>

<a name="te72cdfb8602c42c0bdb344213631c4aa"></a>
<table><thead align="left"><tr id="rd64b6ea52374450685d0150f5fb2176c"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a86d21576ea0e4de98ac2d85726ec9374"><a name="a86d21576ea0e4de98ac2d85726ec9374"></a><a name="a86d21576ea0e4de98ac2d85726ec9374"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a57f777ab4b8942b8b6128fdecb30f612"><a name="a57f777ab4b8942b8b6128fdecb30f612"></a><a name="a57f777ab4b8942b8b6128fdecb30f612"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="rb8d2fe852aa945028c6625ca9b107dde"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4ea0f031a4fa46e385cdfb1e4748ca9f"><a name="a4ea0f031a4fa46e385cdfb1e4748ca9f"></a><a name="a4ea0f031a4fa46e385cdfb1e4748ca9f"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abd0316e50605489e8fd86d80109df09f"><a name="abd0316e50605489e8fd86d80109df09f"></a><a name="abd0316e50605489e8fd86d80109df09f"></a>EIP ID</p>
</td>
</tr>
<tr id="r73d5b19ec8c642a6ade0aec551915f8a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af03acfb524a34c109c368dbb6950d9f5"><a name="af03acfb524a34c109c368dbb6950d9f5"></a><a name="af03acfb524a34c109c368dbb6950d9f5"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a95409ae6e2984d3a959766e1652f2610"><a name="a95409ae6e2984d3a959766e1652f2610"></a><a name="a95409ae6e2984d3a959766e1652f2610"></a>Bandwidth ID</p>
</td>
</tr>
</tbody>
</table>

