# SFS Metrics<a name="sfs_01_0047"></a>

## Function<a name="section48080847153328"></a>

This topic describes metrics reported by Scalable File Service \(SFS\) as well as their namespaces and dimensions. You can use the console or APIs provided by Cloud Eye to query the metrics generated for SFS.

## Namespace<a name="section20110798153328"></a>

SYS.SFS

## Metrics<a name="section31039493153328"></a>

<a name="table31171041153328"></a>
<table><thead align="left"><tr id="row42397114153328"><th class="cellrowborder" valign="top" width="14.150000000000002%" id="mcps1.1.7.1.1"><p id="p11614228153328"><a name="p11614228153328"></a><a name="p11614228153328"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="8.890000000000002%" id="mcps1.1.7.1.2"><p id="p1228402153328"><a name="p1228402153328"></a><a name="p1228402153328"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.480000000000004%" id="mcps1.1.7.1.3"><p id="p32391741153328"><a name="p32391741153328"></a><a name="p32391741153328"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="11.600000000000001%" id="mcps1.1.7.1.4"><p id="p6485340153328"><a name="p6485340153328"></a><a name="p6485340153328"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="17.090000000000003%" id="mcps1.1.7.1.5"><p id="p58103874155224"><a name="p58103874155224"></a><a name="p58103874155224"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="14.790000000000003%" id="mcps1.1.7.1.6"><p id="p579105321217"><a name="p579105321217"></a><a name="p579105321217"></a>Monitoring Period (Original Metric)</p>
</th>
</tr>
</thead>
<tbody><tr id="row3298232153328"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p42751914173912"><a name="p42751914173912"></a><a name="p42751914173912"></a>read_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p1227531423917"><a name="p1227531423917"></a><a name="p1227531423917"></a>Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p15275514113912"><a name="p15275514113912"></a><a name="p15275514113912"></a>Read bandwidth of a file system within a monitoring period</p>
<p id="p192563149569"><a name="p192563149569"></a><a name="p192563149569"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p9072094155224"><a name="p9072094155224"></a><a name="p9072094155224"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p63750977155224"><a name="p63750977155224"></a><a name="p63750977155224"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="p20801153101219"><a name="p20801153101219"></a><a name="p20801153101219"></a>4 minutes</p>
</td>
</tr>
<tr id="row21884471153328"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p1527512146393"><a name="p1527512146393"></a><a name="p1527512146393"></a>write_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p0275161413911"><a name="p0275161413911"></a><a name="p0275161413911"></a>Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p527691413398"><a name="p527691413398"></a><a name="p527691413398"></a>Write bandwidth of a file system within a monitoring period</p>
<p id="p267311455718"><a name="p267311455718"></a><a name="p267311455718"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p05381407578"><a name="p05381407578"></a><a name="p05381407578"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p34127948155224"><a name="p34127948155224"></a><a name="p34127948155224"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p1298695092517"><a name="en-us_topic_0015479905_p1298695092517"></a><a name="en-us_topic_0015479905_p1298695092517"></a>4 minutes</p>
</td>
</tr>
<tr id="row58957821154029"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p32761214133911"><a name="p32761214133911"></a><a name="p32761214133911"></a>rw_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p7276614173915"><a name="p7276614173915"></a><a name="p7276614173915"></a>Read and Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p162085814429"><a name="p162085814429"></a><a name="p162085814429"></a>Read and write bandwidth of a file system within a monitoring period</p>
<p id="p127232169573"><a name="p127232169573"></a><a name="p127232169573"></a>Unit: byte/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p8260756155224"><a name="p8260756155224"></a><a name="p8260756155224"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p65141501155224"><a name="p65141501155224"></a><a name="p65141501155224"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p4986155018257"><a name="en-us_topic_0015479905_p4986155018257"></a><a name="en-us_topic_0015479905_p4986155018257"></a>4 minutes</p>
</td>
</tr>
<tr id="row144314183017"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p191794412012"><a name="p191794412012"></a><a name="p191794412012"></a>read_ops</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p71211445018"><a name="p71211445018"></a><a name="p71211445018"></a>Read OPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p42844700"><a name="p42844700"></a><a name="p42844700"></a>Read operations of a file system within a monitoring period</p>
<p id="p19317334214"><a name="p19317334214"></a><a name="p19317334214"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p29861434018"><a name="p29861434018"></a><a name="p29861434018"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p10986623532"><a name="p10986623532"></a><a name="p10986623532"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p6978532474"><a name="en-us_topic_0015479905_p6978532474"></a><a name="en-us_topic_0015479905_p6978532474"></a>4 minutes</p>
</td>
</tr>
<tr id="row1437110301405"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p173718301017"><a name="p173718301017"></a><a name="p173718301017"></a>write_ops</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p1837116304014"><a name="p1837116304014"></a><a name="p1837116304014"></a>Write OPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p93714301010"><a name="p93714301010"></a><a name="p93714301010"></a>Write operations of a file system within a monitoring period</p>
<p id="p55110426215"><a name="p55110426215"></a><a name="p55110426215"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p145330439614"><a name="p145330439614"></a><a name="p145330439614"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p169871423038"><a name="p169871423038"></a><a name="p169871423038"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p164315331370"><a name="en-us_topic_0015479905_p164315331370"></a><a name="en-us_topic_0015479905_p164315331370"></a>4 minutes</p>
</td>
</tr>
<tr id="row68191277020"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p15819172713016"><a name="p15819172713016"></a><a name="p15819172713016"></a>rw_ops</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p128193277013"><a name="p128193277013"></a><a name="p128193277013"></a>Read Write OPS</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p1681915276017"><a name="p1681915276017"></a><a name="p1681915276017"></a>Read and write operations of a file system within a monitoring period</p>
<p id="p145661544728"><a name="p145661544728"></a><a name="p145661544728"></a>Unit: Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p46657452614"><a name="p46657452614"></a><a name="p46657452614"></a>≥ 0 Count/s</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p11988823131"><a name="p11988823131"></a><a name="p11988823131"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p1810443310716"><a name="en-us_topic_0015479905_p1810443310716"></a><a name="en-us_topic_0015479905_p1810443310716"></a>4 minutes</p>
</td>
</tr>
<tr id="row65779351003"><td class="cellrowborder" valign="top" width="14.150000000000002%" headers="mcps1.1.7.1.1 "><p id="p1353511351301"><a name="p1353511351301"></a><a name="p1353511351301"></a>used_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="8.890000000000002%" headers="mcps1.1.7.1.2 "><p id="p15356351708"><a name="p15356351708"></a><a name="p15356351708"></a>Used Capacity</p>
</td>
<td class="cellrowborder" valign="top" width="33.480000000000004%" headers="mcps1.1.7.1.3 "><p id="p125361351017"><a name="p125361351017"></a><a name="p125361351017"></a>Used capacity of a file system within a monitoring period</p>
<p id="p46311646521"><a name="p46311646521"></a><a name="p46311646521"></a>Unit: byte</p>
</td>
<td class="cellrowborder" valign="top" width="11.600000000000001%" headers="mcps1.1.7.1.4 "><p id="p65391249314"><a name="p65391249314"></a><a name="p65391249314"></a>≥ 0 bytes</p>
</td>
<td class="cellrowborder" valign="top" width="17.090000000000003%" headers="mcps1.1.7.1.5 "><p id="p55391835905"><a name="p55391835905"></a><a name="p55391835905"></a>SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="14.790000000000003%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0015479905_p5561131614716"><a name="en-us_topic_0015479905_p5561131614716"></a><a name="en-us_topic_0015479905_p5561131614716"></a>4 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section43930857153328"></a>

<a name="table1629697153328"></a>
<table><thead align="left"><tr id="row64993686153328"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="p29997214153328"><a name="p29997214153328"></a><a name="p29997214153328"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="p13855283153328"><a name="p13855283153328"></a><a name="p13855283153328"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row48536124153328"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p1344191314404"><a name="p1344191314404"></a><a name="p1344191314404"></a>share_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p4441121324012"><a name="p4441121324012"></a><a name="p4441121324012"></a>SFS file system</p>
</td>
</tr>
</tbody>
</table>

## Viewing Monitoring Statistics<a name="section893454153710"></a>

1.  Log in to the management console.
2.  View the monitoring graphs using either of the following methods.
    -   Method 1: Choose  **Service List**  \>  **Storage**  \>  **Scalable File Service**. In the file system list, click  **View Metric**  in the  **Operation**  column of the target file system.
    -   Method 2: Choose  **Management & Deployment**  \>  **Cloud Eye**  \>  **Cloud Service Monitoring**  \>  **Scalable File Service**. In the file system list, click  **View Metric**  in the  **Operation**  column of the target file system.

3.  You can view the SFS file system monitoring data by metric or monitored duration.

    [Figure 1](#fig4460418173118)  shows the monitoring graphs. For more information about Cloud Eye, see the  _Cloud Eye User Guide_.

    **Figure  1**  Monitoring graphs<a name="fig4460418173118"></a>  
    ![](figures/monitoring-graphs.png "monitoring-graphs")


