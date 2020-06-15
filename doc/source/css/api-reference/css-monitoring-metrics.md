# CSS Monitoring Metrics<a name="css_03_0042"></a>

## Function Description<a name="en-us_topic_0171139356_section59820001153251"></a>

This section describes monitoring metrics reported by CSS to Cloud Eye as well as their namespaces and dimensions. You can use APIs provided by Cloud Eye to view the monitoring metrics of the monitored object and alarms generated for CSS.

## Namespace<a name="en-us_topic_0171139356_section172651386227"></a>

SYS.ES

## Monitoring Metrics<a name="en-us_topic_0171139356_section18266133811225"></a>

<a name="en-us_topic_0171139356_table102675383222"></a>
<table><thead align="left"><tr id="en-us_topic_0171139356_row726893842214"><th class="cellrowborder" valign="top" width="6.0606060606060606%" id="mcps1.1.7.1.1"><p id="en-us_topic_0171139356_p20269183892219"><a name="en-us_topic_0171139356_p20269183892219"></a><a name="en-us_topic_0171139356_p20269183892219"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="9.090909090909092%" id="mcps1.1.7.1.2"><p id="en-us_topic_0171139356_p16270153816220"><a name="en-us_topic_0171139356_p16270153816220"></a><a name="en-us_topic_0171139356_p16270153816220"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.1.7.1.3"><p id="en-us_topic_0171139356_p527115383221"><a name="en-us_topic_0171139356_p527115383221"></a><a name="en-us_topic_0171139356_p527115383221"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.1.7.1.4"><p id="en-us_topic_0171139356_p202711238192210"><a name="en-us_topic_0171139356_p202711238192210"></a><a name="en-us_topic_0171139356_p202711238192210"></a>Formula</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.1.7.1.5"><p id="en-us_topic_0171139356_p09541536155512"><a name="en-us_topic_0171139356_p09541536155512"></a><a name="en-us_topic_0171139356_p09541536155512"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="8.080808080808081%" id="mcps1.1.7.1.6"><p id="en-us_topic_0171139356_p1382175911481"><a name="en-us_topic_0171139356_p1382175911481"></a><a name="en-us_topic_0171139356_p1382175911481"></a>Monitoring Interval</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171139356_row472618584223"><td class="cellrowborder" valign="top" width="6.0606060606060606%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0171139356_p9726175820227"><a name="en-us_topic_0171139356_p9726175820227"></a><a name="en-us_topic_0171139356_p9726175820227"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0171139356_p530281982319"><a name="en-us_topic_0171139356_p530281982319"></a><a name="en-us_topic_0171139356_p530281982319"></a>Cluster health status</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0171139356_p87261958132220"><a name="en-us_topic_0171139356_p87261958132220"></a><a name="en-us_topic_0171139356_p87261958132220"></a>Measures the health status of a <span id="en-us_topic_0171139356_text1678223111546"><a name="en-us_topic_0171139356_text1678223111546"></a><a name="en-us_topic_0171139356_text1678223111546"></a>CSS</span> cluster.</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0171139356_p1337749155616"><a name="en-us_topic_0171139356_p1337749155616"></a><a name="en-us_topic_0171139356_p1337749155616"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0171139356_p2954193610556"><a name="en-us_topic_0171139356_p2954193610556"></a><a name="en-us_topic_0171139356_p2954193610556"></a>Available values are <strong id="en-us_topic_0171139356_b342432016712"><a name="en-us_topic_0171139356_b342432016712"></a><a name="en-us_topic_0171139356_b342432016712"></a>0</strong>, <strong id="en-us_topic_0171139356_b38151222178"><a name="en-us_topic_0171139356_b38151222178"></a><a name="en-us_topic_0171139356_b38151222178"></a>1</strong>, and <strong id="en-us_topic_0171139356_b108921631178"><a name="en-us_topic_0171139356_b108921631178"></a><a name="en-us_topic_0171139356_b108921631178"></a>2</strong>.</p>
<a name="en-us_topic_0171139356_ul29543361556"></a><a name="en-us_topic_0171139356_ul29543361556"></a><ul id="en-us_topic_0171139356_ul29543361556"><li><strong id="en-us_topic_0171139356_b52474813401"><a name="en-us_topic_0171139356_b52474813401"></a><a name="en-us_topic_0171139356_b52474813401"></a>0</strong>: All primary and replica shards are allocated. Your cluster is 100% operational.</li><li><strong id="en-us_topic_0171139356_b121081502409"><a name="en-us_topic_0171139356_b121081502409"></a><a name="en-us_topic_0171139356_b121081502409"></a>1</strong>: All primary shards are allocated, but at least one replica is missing. No data is missing, so search results will still be complete. However, your high availability is compromised to some degree. If more shards disappear, you might lose data. Think of this state as a warning that should prompt investigation.</li><li><strong id="en-us_topic_0171139356_b14460152144015"><a name="en-us_topic_0171139356_b14460152144015"></a><a name="en-us_topic_0171139356_b14460152144015"></a>2</strong>: At least one primary shard (and all of its replicas) is missing. This means that you are missing data: searches will return partial results, and indexing into that shard will return an exception.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="8.080808080808081%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0171139356_p4838059144820"><a name="en-us_topic_0171139356_p4838059144820"></a><a name="en-us_topic_0171139356_p4838059144820"></a>1 minute</p>
</td>
</tr>
<tr id="en-us_topic_0171139356_row2272193812219"><td class="cellrowborder" valign="top" width="6.0606060606060606%" headers="mcps1.1.7.1.1 "><p id="en-us_topic_0171139356_p207641617184420"><a name="en-us_topic_0171139356_p207641617184420"></a><a name="en-us_topic_0171139356_p207641617184420"></a>disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="9.090909090909092%" headers="mcps1.1.7.1.2 "><p id="en-us_topic_0171139356_p776471711444"><a name="en-us_topic_0171139356_p776471711444"></a><a name="en-us_topic_0171139356_p776471711444"></a>Disk usage</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.1.7.1.3 "><p id="en-us_topic_0171139356_p9255915115817"><a name="en-us_topic_0171139356_p9255915115817"></a><a name="en-us_topic_0171139356_p9255915115817"></a>Calculates the disk usage of a <span id="en-us_topic_0171139356_text1795244118543"><a name="en-us_topic_0171139356_text1795244118543"></a><a name="en-us_topic_0171139356_text1795244118543"></a>CSS</span> cluster.</p>
<p id="en-us_topic_0171139356_p17648171448"><a name="en-us_topic_0171139356_p17648171448"></a><a name="en-us_topic_0171139356_p17648171448"></a>Unit: %</p>
</td>
<td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.7.1.4 "><p id="en-us_topic_0171139356_p1676461734411"><a name="en-us_topic_0171139356_p1676461734411"></a><a name="en-us_topic_0171139356_p1676461734411"></a>Used disk space of a cluster/Total disk space of a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.1.7.1.5 "><p id="en-us_topic_0171139356_p9970123675515"><a name="en-us_topic_0171139356_p9970123675515"></a><a name="en-us_topic_0171139356_p9970123675515"></a>0 to 100%</p>
</td>
<td class="cellrowborder" valign="top" width="8.080808080808081%" headers="mcps1.1.7.1.6 "><p id="en-us_topic_0171139356_p138384596482"><a name="en-us_topic_0171139356_p138384596482"></a><a name="en-us_topic_0171139356_p138384596482"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="en-us_topic_0171139356_section102905383226"></a>

<a name="en-us_topic_0171139356_table13291038182217"></a>
<table><thead align="left"><tr id="en-us_topic_0171139356_row13292153862219"><th class="cellrowborder" valign="top" width="40.400000000000006%" id="mcps1.1.3.1.1"><p id="en-us_topic_0171139356_p17292638192211"><a name="en-us_topic_0171139356_p17292638192211"></a><a name="en-us_topic_0171139356_p17292638192211"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.1.3.1.2"><p id="en-us_topic_0171139356_p92938385226"><a name="en-us_topic_0171139356_p92938385226"></a><a name="en-us_topic_0171139356_p92938385226"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171139356_row1429373812228"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0171139356_p178643281443"><a name="en-us_topic_0171139356_p178643281443"></a><a name="en-us_topic_0171139356_p178643281443"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0171139356_p986422814446"><a name="en-us_topic_0171139356_p986422814446"></a><a name="en-us_topic_0171139356_p986422814446"></a>Specifies the cluster ID.</p>
</td>
</tr>
</tbody>
</table>

