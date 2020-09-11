# Should I Choose DWS or RDS on Public Cloud?<a name="dws_03_0009"></a>

Both DWS and RDS on the public cloud allow you to run conventional relational databases on the cloud and transfer database management loads. You can use RDS databases for OLTP, reporting, and analysis. However, RDS provides insufficient support for read operations of a large amount of data \(complex read-only queries\). With multi-node scale and resources and various optimized algorithms \(**column-based storage, vectorized executors, and distributed frameworks**\), DWS focuses on OLAP, reducing analysis and report workloads of large data sets by an order of magnitude.

DWS delivers scale-out capabilities when the data and query complexity increases or when you want to prevent report and analysis from increasing OLTP workloads.

You can determine the scenario where DWS or RDS is more suitable according to the following table.

**Table  1**  Feature comparison between OLTP and OLAP 

<a name="table1612418683415"></a>
<table><thead align="left"><tr id="row212513623416"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p012515673411"><a name="p012515673411"></a><a name="p012515673411"></a><strong id="b842352706112930"><a name="b842352706112930"></a><a name="b842352706112930"></a>Feature</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.2"><p id="p212514633410"><a name="p212514633410"></a><a name="p212514633410"></a>OLTP</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.4.1.3"><p id="p1312596203415"><a name="p1312596203415"></a><a name="p1312596203415"></a>OLAP</p>
</th>
</tr>
</thead>
<tbody><tr id="row91251861341"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1912516183420"><a name="p1912516183420"></a><a name="p1912516183420"></a>User</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p912596113418"><a name="p912596113418"></a><a name="p912596113418"></a>Operation personnel and low-level management personnel</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p912519613341"><a name="p912519613341"></a><a name="p912519613341"></a>Decision-making personnel and senior management personnel</p>
</td>
</tr>
<tr id="row3126206143416"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p81269633415"><a name="p81269633415"></a><a name="p81269633415"></a>Function</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p8126468341"><a name="p8126468341"></a><a name="p8126468341"></a>Daily operation processing</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p4126166163414"><a name="p4126166163414"></a><a name="p4126166163414"></a>Analysis and decision-making</p>
</td>
</tr>
<tr id="row21262062341"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p19126569346"><a name="p19126569346"></a><a name="p19126569346"></a>Design</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p131262673414"><a name="p131262673414"></a><a name="p131262673414"></a>Application-centric </p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p121269611343"><a name="p121269611343"></a><a name="p121269611343"></a>Subject-oriented</p>
</td>
</tr>
<tr id="row1912696143411"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p191265612341"><a name="p191265612341"></a><a name="p191265612341"></a>Data</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p141262613342"><a name="p141262613342"></a><a name="p141262613342"></a>Latest, detailed, two-dimensional, and discrete</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p6126106143417"><a name="p6126106143417"></a><a name="p6126106143417"></a>Historical, integrated, multidimensional, and unified</p>
</td>
</tr>
<tr id="row104371119354"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p84381512359"><a name="p84381512359"></a><a name="p84381512359"></a>Access</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p1143910173511"><a name="p1143910173511"></a><a name="p1143910173511"></a>Dozens of read and write records </p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p64391143512"><a name="p64391143512"></a><a name="p64391143512"></a>Millions of read records</p>
</td>
</tr>
<tr id="row321416303511"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p52144315356"><a name="p52144315356"></a><a name="p52144315356"></a>Work scope</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p7214334354"><a name="p7214334354"></a><a name="p7214334354"></a>Simple read and write operations</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p3214132350"><a name="p3214132350"></a><a name="p3214132350"></a>Complex query</p>
</td>
</tr>
<tr id="row0723182173519"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p1723122143516"><a name="p1723122143516"></a><a name="p1723122143516"></a>Database size</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.2 "><p id="p117235211353"><a name="p117235211353"></a><a name="p117235211353"></a>Hundreds of GB</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.4.1.3 "><p id="p1872312114354"><a name="p1872312114354"></a><a name="p1872312114354"></a>TB or PB</p>
</td>
</tr>
</tbody>
</table>

