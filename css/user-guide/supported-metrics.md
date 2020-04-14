# Supported Metrics<a name="css_01_0042"></a>

You can use Cloud Eye provided by the public cloud platform to monitor cluster metrics of CSS in real time, facilitating prompt exception handling. For details about Cloud Eye, see the  [Cloud Eye User Guide](https://docs.otc.t-systems.com/en-us/usermanual/ces/en-us_topic_0015479886.html).

[Table 1](#table978532322710)  lists the metrics supported by CSS.

**Table  1**  Supported metrics

<a name="table978532322710"></a>
<table><thead align="left"><tr id="row180042322710"><th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.6.1.1"><p id="p1380032312276"><a name="p1380032312276"></a><a name="p1380032312276"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.6.1.2"><p id="p16800162315271"><a name="p16800162315271"></a><a name="p16800162315271"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.6.1.3"><p id="p17800123112713"><a name="p17800123112713"></a><a name="p17800123112713"></a>Formula</p>
</th>
<th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.6.1.4"><p id="p17800623112718"><a name="p17800623112718"></a><a name="p17800623112718"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.6.1.5"><p id="p1382175911481"><a name="p1382175911481"></a><a name="p1382175911481"></a>Monitoring Interval</p>
</th>
</tr>
</thead>
<tbody><tr id="row1280022318278"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.1 "><p id="p6800132362720"><a name="p6800132362720"></a><a name="p6800132362720"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.2 "><p id="p0800192322711"><a name="p0800192322711"></a><a name="p0800192322711"></a>Calculates the disk usage of a <span id="text560416151686"><a name="text560416151686"></a><a name="text560416151686"></a>CSS</span> cluster.</p>
<p id="p58631629145119"><a name="p58631629145119"></a><a name="p58631629145119"></a>Unit: %</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.3 "><p id="p16801342201115"><a name="p16801342201115"></a><a name="p16801342201115"></a>Used disk space of a cluster/Total disk space of a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.6.1.4 "><p id="p180022322712"><a name="p180022322712"></a><a name="p180022322712"></a>0 to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.6.1.5 "><p id="p4838059144820"><a name="p4838059144820"></a><a name="p4838059144820"></a>1 minute</p>
</td>
</tr>
<tr id="row19751914182817"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.1 "><p id="p8975181412288"><a name="p8975181412288"></a><a name="p8975181412288"></a>Cluster Health Status</p>
</td>
<td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.6.1.2 "><p id="p897531412813"><a name="p897531412813"></a><a name="p897531412813"></a>Measures the health status of a <span id="text75731417585"><a name="text75731417585"></a><a name="text75731417585"></a>CSS</span> cluster.</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.6.1.3 "><p id="p18756183133015"><a name="p18756183133015"></a><a name="p18756183133015"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.6.1.4 "><p id="p161524816305"><a name="p161524816305"></a><a name="p161524816305"></a>Available values are <strong id="b342432016712"><a name="b342432016712"></a><a name="b342432016712"></a>0</strong>, <strong id="b38151222178"><a name="b38151222178"></a><a name="b38151222178"></a>1</strong>, and <strong id="b108921631178"><a name="b108921631178"></a><a name="b108921631178"></a>2</strong>.</p>
<a name="ul1674834825210"></a><a name="ul1674834825210"></a><ul id="ul1674834825210"><li><strong id="b52474813401"><a name="b52474813401"></a><a name="b52474813401"></a>0</strong>: All primary and replica shards are allocated. Your cluster is 100% operational.</li><li><strong id="b121081502409"><a name="b121081502409"></a><a name="b121081502409"></a>1</strong>: All primary shards are allocated, but at least one replica is missing. No data is missing, so search results will still be complete. However, your high availability is compromised to some degree. If more shards disappear, you might lose data. Think of this state as a warning that should prompt investigation.</li><li><strong id="b14460152144015"><a name="b14460152144015"></a><a name="b14460152144015"></a>2</strong>: At least one primary shard (and all of its replicas) is missing. This means that you are missing data: searches will return partial results, and indexing into that shard will return an exception.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.6.1.5 "><p id="p138384596482"><a name="p138384596482"></a><a name="p138384596482"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

