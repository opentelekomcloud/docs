# DCS Instance Statuses<a name="dcs-api-0312047"></a>

**Table  1**  DCS instance statuses

<a name="table1875805420588"></a>
<table><thead align="left"><tr id="row57586542584"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p1875875412581"><a name="p1875875412581"></a><a name="p1875875412581"></a><strong id="b16374113319102"><a name="b16374113319102"></a><a name="b16374113319102"></a>State</strong></p>
</th>
<th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p18758754175815"><a name="p18758754175815"></a><a name="p18758754175815"></a><strong id="b1995713815919"><a name="b1995713815919"></a><a name="b1995713815919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row47592548587"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p1177218171807"><a name="p1177218171807"></a><a name="p1177218171807"></a>CREATING</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p077511574570"><a name="p077511574570"></a><a name="p077511574570"></a>Creating is the status before the Running state.</p>
</td>
</tr>
<tr id="row129751433494"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p684282010488"><a name="p684282010488"></a><a name="p684282010488"></a>CREATEFAILED</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1865313194481"><a name="p1865313194481"></a><a name="p1865313194481"></a>The DCS instance failed to be created.</p>
</td>
</tr>
<tr id="row27591054165817"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p77721417404"><a name="p77721417404"></a><a name="p77721417404"></a>RUNNING</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1776195795715"><a name="p1776195795715"></a><a name="p1776195795715"></a>The instance is running properly.</p>
<p id="p127762057155717"><a name="p127762057155717"></a><a name="p127762057155717"></a>Only instances in the Running state can provide in-memory cache service.</p>
</td>
</tr>
<tr id="row12759145465815"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p9773131720012"><a name="p9773131720012"></a><a name="p9773131720012"></a>ERROR</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p13776165713574"><a name="p13776165713574"></a><a name="p13776165713574"></a>The instance is not running properly.</p>
</td>
</tr>
<tr id="row1475918544587"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p147731176019"><a name="p147731176019"></a><a name="p147731176019"></a>RESTARTING</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p377719577578"><a name="p377719577578"></a><a name="p377719577578"></a>The instance is being restarted.</p>
</td>
</tr>
<tr id="row4162132872914"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p37741217508"><a name="p37741217508"></a><a name="p37741217508"></a>EXTENDING</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p777818571577"><a name="p777818571577"></a><a name="p777818571577"></a>The instance is being scaled up.</p>
</td>
</tr>
<tr id="row268424020193"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p17983104641918"><a name="p17983104641918"></a><a name="p17983104641918"></a>RESTORING</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1898314464193"><a name="p1898314464193"></a><a name="p1898314464193"></a>The instance data is being restored.</p>
</td>
</tr>
</tbody>
</table>

