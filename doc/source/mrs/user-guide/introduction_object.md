# Introduction<a name="EN-US_TOPIC_0125375752"></a>

An MRS cluster contains different types of basic objects.  [Table 1](#table23400575171145)  describes these objects.

**Table  1**  MRS basic objects

<a name="table23400575171145"></a>
<table><thead align="left"><tr id="row14789438171145"><th class="cellrowborder" valign="top" width="12.831283128312831%" id="mcps1.2.4.1.1"><p id="p57093844171145"><a name="p57093844171145"></a><a name="p57093844171145"></a><strong id="b62646689165236"><a name="b62646689165236"></a><a name="b62646689165236"></a>Object</strong></p>
</th>
<th class="cellrowborder" valign="top" width="46.16461646164616%" id="mcps1.2.4.1.2"><p id="p61198658171145"><a name="p61198658171145"></a><a name="p61198658171145"></a><strong id="b3346852165226"><a name="b3346852165226"></a><a name="b3346852165226"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.004100410041%" id="mcps1.2.4.1.3"><p id="p58144305171145"><a name="p58144305171145"></a><a name="p58144305171145"></a><strong id="b28890064165221"><a name="b28890064165221"></a><a name="b28890064165221"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12068297171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p65009296165138"><a name="p65009296165138"></a><a name="p65009296165138"></a>Service</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p31261658165138"><a name="p31261658165138"></a><a name="p31261658165138"></a>Function set that can complete specific <span id="ph1771136693154"><a name="ph1771136693154"></a><a name="ph1771136693154"></a>operations</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p49166397165138"><a name="p49166397165138"></a><a name="p49166397165138"></a>KrbServer service and LdapServer service</p>
</td>
</tr>
<tr id="row11779622171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p14625339171145"><a name="p14625339171145"></a><a name="p14625339171145"></a>Service instance</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p43801796171145"><a name="p43801796171145"></a><a name="p43801796171145"></a>Specific instance of a service, often referred to as a service.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p54799227171145"><a name="p54799227171145"></a><a name="p54799227171145"></a>KrbServer service</p>
</td>
</tr>
<tr id="row23430996171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p2566311416529"><a name="p2566311416529"></a><a name="p2566311416529"></a>Service role</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p6544636916529"><a name="p6544636916529"></a><a name="p6544636916529"></a>Function<span id="ph1139110493418"><a name="ph1139110493418"></a><a name="ph1139110493418"></a>al</span>&nbsp;entity that forms a complete service,&nbsp;<span id="ph2454737393436"><a name="ph2454737393436"></a><a name="ph2454737393436"></a>often referred to as a</span> role.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p6666456516529"><a name="p6666456516529"></a><a name="p6666456516529"></a>KrbServer consists of the KerberosAdmin role and the KerberosServer role.</p>
</td>
</tr>
<tr id="row6356459171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p1165071416529"><a name="p1165071416529"></a><a name="p1165071416529"></a>Role instance</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p418381216529"><a name="p418381216529"></a><a name="p418381216529"></a>Specific instance of a service role running on a host.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p334451916529"><a name="p334451916529"></a><a name="p334451916529"></a>KerberosAdmin&nbsp;running on Host2 and KerberosServer&nbsp;running on Host3</p>
</td>
</tr>
<tr id="row18706969171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p2223541916529"><a name="p2223541916529"></a><a name="p2223541916529"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p11946317114133"><a name="p11946317114133"></a><a name="p11946317114133"></a>Elastic Cloud Server (ECS) <span id="ph4548876893519"><a name="ph4548876893519"></a><a name="ph4548876893519"></a>running</span> a Linux OS.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p5902444516529"><a name="p5902444516529"></a><a name="p5902444516529"></a>Host1 to Host5</p>
</td>
</tr>
<tr id="row15528860171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p1203865016529"><a name="p1203865016529"></a><a name="p1203865016529"></a>Rack</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p3560661616529"><a name="p3560661616529"></a><a name="p3560661616529"></a>Physical entity that contains multiple hosts connecting to the same switch.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p6556362216529"><a name="p6556362216529"></a><a name="p6556362216529"></a>Rack1 contains Host1 to Host5.</p>
</td>
</tr>
<tr id="row46217402171145"><td class="cellrowborder" valign="top" width="12.831283128312831%" headers="mcps1.2.4.1.1 "><p id="p1436932816529"><a name="p1436932816529"></a><a name="p1436932816529"></a>Cluster</p>
</td>
<td class="cellrowborder" valign="top" width="46.16461646164616%" headers="mcps1.2.4.1.2 "><p id="p2306491016529"><a name="p2306491016529"></a><a name="p2306491016529"></a>Logical entity that consists of multiple hosts and provides various services.</p>
</td>
<td class="cellrowborder" valign="top" width="41.004100410041%" headers="mcps1.2.4.1.3 "><p id="p5631842516529"><a name="p5631842516529"></a><a name="p5631842516529"></a>Cluster1&nbsp;consists of five hosts (Host1 to Host5) and provides services such as KrbServer and LdapServer.</p>
</td>
</tr>
</tbody>
</table>

