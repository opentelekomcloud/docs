# Function Comparison<a name="rds_00_0011"></a>

Single DB instances use the single-node architecture. In contrast to the mainstream primary/standby DB instances, a single DB instance contains only one node and has no slave node for fault recovery. 

## Advantage Comparison<a name="section4541101692212"></a>

-   Single: supports the creation of read replicas \(except for Microsoft SQL Server\) and error or slow query log queries. While primary/standby DB instances have two database nodes, a single DB instance has only one. As a result, restoration after node failure on the primary/standby DB instances will take a long time. Therefore, primary/standby DB instances are not recommended for sensitive services that have high requirements on database availability.
-   Primary/Standby DB instances: The slave database node is used only for failover and restoration. It does not provide services. The performance of single DB instances is similar to or even higher than the primary/standby DB instances.

**Table  1**  Function comparisons

<a name="table1539112616503"></a>
<table><thead align="left"><tr id="row1554422655015"><th class="cellrowborder" valign="top" width="23.28767123287671%" id="mcps1.2.4.1.1"><p id="p135461826135014"><a name="p135461826135014"></a><a name="p135461826135014"></a><strong id="b6297464344"><a name="b6297464344"></a><a name="b6297464344"></a>DB Engine</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.35616438356164%" id="mcps1.2.4.1.2"><p id="p1054812263501"><a name="p1054812263501"></a><a name="p1054812263501"></a><strong id="b581941263415"><a name="b581941263415"></a><a name="b581941263415"></a>Single</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.35616438356164%" id="mcps1.2.4.1.3"><p id="p8550112619503"><a name="p8550112619503"></a><a name="p8550112619503"></a><strong id="b17927142320348"><a name="b17927142320348"></a><a name="b17927142320348"></a>Primary/Standby</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3127629534"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p1128928536"><a name="p1128928536"></a><a name="p1128928536"></a>MySQL</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p48841453217"><a name="p48841453217"></a><a name="p48841453217"></a>5.7</p>
<p id="p0560152619504"><a name="p0560152619504"></a><a name="p0560152619504"></a>5.6</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p25657266508"><a name="p25657266508"></a><a name="p25657266508"></a>5.7</p>
<p id="p195672026155018"><a name="p195672026155018"></a><a name="p195672026155018"></a>5.6</p>
</td>
</tr>
<tr id="row1223994413545"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p12391244145410"><a name="p12391244145410"></a><a name="p12391244145410"></a>PostgreSQL</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p37251581462"><a name="p37251581462"></a><a name="p37251581462"></a>11</p>
<p id="p18521131210314"><a name="p18521131210314"></a><a name="p18521131210314"></a>10</p>
<p id="p125641726145014"><a name="p125641726145014"></a><a name="p125641726145014"></a>9.6</p>
<p id="p20564182612506"><a name="p20564182612506"></a><a name="p20564182612506"></a>9.5</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p16797350144617"><a name="p16797350144617"></a><a name="p16797350144617"></a>11</p>
<p id="p48301145134"><a name="p48301145134"></a><a name="p48301145134"></a>10</p>
<p id="p75702266504"><a name="p75702266504"></a><a name="p75702266504"></a>9.6</p>
<p id="p25701426165013"><a name="p25701426165013"></a><a name="p25701426165013"></a>9.5</p>
</td>
</tr>
<tr id="row17556826195016"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p17559122611501"><a name="p17559122611501"></a><a name="p17559122611501"></a>Microsoft SQL Server</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1063012521281"><a name="p1063012521281"></a><a name="p1063012521281"></a>2016 EE</p>
<p id="p18560426115012"><a name="p18560426115012"></a><a name="p18560426115012"></a>2016 SE</p>
<p id="p282033211912"><a name="p282033211912"></a><a name="p282033211912"></a>2014 SE</p>
<p id="p256219266505"><a name="p256219266505"></a><a name="p256219266505"></a>2014 SP2 SE</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p146518305319"><a name="p146518305319"></a><a name="p146518305319"></a>2016 EE</p>
<p id="p065193175317"><a name="p065193175317"></a><a name="p065193175317"></a>2016 SE</p>
<p id="p265213175314"><a name="p265213175314"></a><a name="p265213175314"></a>2014 SE</p>
<p id="p828335713273"><a name="p828335713273"></a><a name="p828335713273"></a>2014 SP2 SE</p>
</td>
</tr>
<tr id="row15721826125019"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p11573326135018"><a name="p11573326135018"></a><a name="p11573326135018"></a>Number of nodes</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p18574162645011"><a name="p18574162645011"></a><a name="p18574162645011"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p757532619507"><a name="p757532619507"></a><a name="p757532619507"></a>2</p>
</td>
</tr>
<tr id="row45781826125017"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p17580112611501"><a name="p17580112611501"></a><a name="p17580112611501"></a>Specifications</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1642075716319"><a name="p1642075716319"></a><a name="p1642075716319"></a>vCPUs: a maximum of 60</p>
<p id="p16421155712317"><a name="p16421155712317"></a><a name="p16421155712317"></a>Memory: a maximum of 512 GB</p>
<p id="p24233579317"><a name="p24233579317"></a><a name="p24233579317"></a>Storage space: a maximum of 4 TB</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p21251049133213"><a name="p21251049133213"></a><a name="p21251049133213"></a>vCPUs: a maximum of 60</p>
<p id="p11126154911327"><a name="p11126154911327"></a><a name="p11126154911327"></a>Memory: a maximum of 512 GB</p>
<p id="p112764920323"><a name="p112764920323"></a><a name="p112764920323"></a>Storage space: a maximum of 4 TB</p>
</td>
</tr>
<tr id="row35871826185018"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p18588926175016"><a name="p18588926175016"></a><a name="p18588926175016"></a>Monitoring and alarms</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1859118265507"><a name="p1859118265507"></a><a name="p1859118265507"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p16595192685018"><a name="p16595192685018"></a><a name="p16595192685018"></a>Supported</p>
</td>
</tr>
<tr id="row11598132615501"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p135993267508"><a name="p135993267508"></a><a name="p135993267508"></a>Security group</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1760212685020"><a name="p1760212685020"></a><a name="p1760212685020"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p1460252612506"><a name="p1460252612506"></a><a name="p1460252612506"></a>Supported</p>
</td>
</tr>
<tr id="row1560482645020"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p460612616502"><a name="p460612616502"></a><a name="p460612616502"></a>Backups and restorations</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1607192665012"><a name="p1607192665012"></a><a name="p1607192665012"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p8608152610508"><a name="p8608152610508"></a><a name="p8608152610508"></a>Supported</p>
</td>
</tr>
<tr id="row1161032685016"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p461162610503"><a name="p461162610503"></a><a name="p461162610503"></a>Parameter settings</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p96121026145019"><a name="p96121026145019"></a><a name="p96121026145019"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p1761332610501"><a name="p1761332610501"></a><a name="p1761332610501"></a>Supported</p>
</td>
</tr>
<tr id="row19615152675018"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p161872614504"><a name="p161872614504"></a><a name="p161872614504"></a>SSL</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p66191626145018"><a name="p66191626145018"></a><a name="p66191626145018"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p1862052615508"><a name="p1862052615508"></a><a name="p1862052615508"></a>Supported</p>
</td>
</tr>
<tr id="row86221926185017"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p18624142619505"><a name="p18624142619505"></a><a name="p18624142619505"></a>Log management</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p12624112610505"><a name="p12624112610505"></a><a name="p12624112610505"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p662672625016"><a name="p662672625016"></a><a name="p662672625016"></a>Supported</p>
</td>
</tr>
<tr id="row56287263504"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p136321726145015"><a name="p136321726145015"></a><a name="p136321726145015"></a>Read replicas (need to be created)</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1963342611505"><a name="p1963342611505"></a><a name="p1963342611505"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p1163520264503"><a name="p1163520264503"></a><a name="p1163520264503"></a>Supported</p>
</td>
</tr>
<tr id="row66486267503"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p136491626185013"><a name="p136491626185013"></a><a name="p136491626185013"></a>High-frequency monitoring</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p19650122665018"><a name="p19650122665018"></a><a name="p19650122665018"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p265214264507"><a name="p265214264507"></a><a name="p265214264507"></a>Supported</p>
</td>
</tr>
<tr id="row19155439103113"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p9156163912311"><a name="p9156163912311"></a><a name="p9156163912311"></a>Primary/standby switchover or failover</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p9156173943113"><a name="p9156173943113"></a><a name="p9156173943113"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p1285424218320"><a name="p1285424218320"></a><a name="p1285424218320"></a>Supported</p>
</td>
</tr>
<tr id="row173431034133120"><td class="cellrowborder" valign="top" width="23.28767123287671%" headers="mcps1.2.4.1.1 "><p id="p462355373113"><a name="p462355373113"></a><a name="p462355373113"></a>Standby DB instance migration</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.2 "><p id="p1934414347319"><a name="p1934414347319"></a><a name="p1934414347319"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="38.35616438356164%" headers="mcps1.2.4.1.3 "><p id="p885413426324"><a name="p885413426324"></a><a name="p885413426324"></a>Supported</p>
</td>
</tr>
</tbody>
</table>

