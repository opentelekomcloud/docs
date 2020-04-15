# Cloud Search Service Metrics<a name="EN-US_TOPIC_0171212563"></a>

## Function<a name="section59820001153251"></a>

This topic describes metrics reported by Cloud Search Service \(CSS\) to Cloud Eye as well as their namespaces, list, and dimensions. You can use APIs provided by Cloud Eye to query the metric information generated for CSS.

## Namespace<a name="section172651386227"></a>

SYS.ES

## Metrics<a name="section18266133811225"></a>

<a name="table102675383222"></a>
<table><thead align="left"><tr id="row726893842214"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.6.1.1"><p id="p20269183892219"><a name="p20269183892219"></a><a name="p20269183892219"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.1.6.1.2"><p id="p16270153816220"><a name="p16270153816220"></a><a name="p16270153816220"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="34.300000000000004%" id="mcps1.1.6.1.3"><p id="p527115383221"><a name="p527115383221"></a><a name="p527115383221"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="13.18%" id="mcps1.1.6.1.4"><p id="p202711238192210"><a name="p202711238192210"></a><a name="p202711238192210"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="21.21%" id="mcps1.1.6.1.5"><p id="p52723385226"><a name="p52723385226"></a><a name="p52723385226"></a>Monitored Object</p>
</th>
</tr>
</thead>
<tbody><tr id="row472618584223"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p9726175820227"><a name="p9726175820227"></a><a name="p9726175820227"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.6.1.2 "><p id="p530281982319"><a name="p530281982319"></a><a name="p530281982319"></a>Cluster Health Status</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.1.6.1.3 "><p id="p87261958132220"><a name="p87261958132220"></a><a name="p87261958132220"></a>Health status of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.1.6.1.4 "><p id="p1431964322314"><a name="p1431964322314"></a><a name="p1431964322314"></a><strong id="b0951184711812"><a name="b0951184711812"></a><a name="b0951184711812"></a>0</strong>, <strong id="b5372175016815"><a name="b5372175016815"></a><a name="b5372175016815"></a>1</strong>, and <strong id="b343310514810"><a name="b343310514810"></a><a name="b343310514810"></a>2</strong></p>
<p id="p1812933419343"><a name="p1812933419343"></a><a name="p1812933419343"></a><strong id="b66644592815"><a name="b66644592815"></a><a name="b66644592815"></a>0</strong>: The cluster is 100% operational.</p>
<p id="p11571853191713"><a name="p11571853191713"></a><a name="p11571853191713"></a><strong id="b9150177162818"><a name="b9150177162818"></a><a name="b9150177162818"></a>1</strong>: Some replicas are missing. Your data is complete, but exceptions may occur because your high availability is compromised.</p>
<p id="p8807115951710"><a name="p8807115951710"></a><a name="p8807115951710"></a><strong id="b1614116107288"><a name="b1614116107288"></a><a name="b1614116107288"></a>2</strong>: Data missing occurs and the cluster fails to work.</p>
</td>
<td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.1.6.1.5 "><p id="p1932044312237"><a name="p1932044312237"></a><a name="p1932044312237"></a>CSS cluster</p>
</td>
</tr>
<tr id="row2272193812219"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.6.1.1 "><p id="p207641617184420"><a name="p207641617184420"></a><a name="p207641617184420"></a>disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.1.6.1.2 "><p id="p776471711444"><a name="p776471711444"></a><a name="p776471711444"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="34.300000000000004%" headers="mcps1.1.6.1.3 "><p id="p9255915115817"><a name="p9255915115817"></a><a name="p9255915115817"></a>Disk usage of the monitored object</p>
<p id="p17648171448"><a name="p17648171448"></a><a name="p17648171448"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.1.6.1.4 "><p id="p1676461734411"><a name="p1676461734411"></a><a name="p1676461734411"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.1.6.1.5 "><p id="p173746537577"><a name="p173746537577"></a><a name="p173746537577"></a>CSS cluster</p>
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
<tbody><tr id="row1429373812228"><td class="cellrowborder" valign="top" width="40.400000000000006%" headers="mcps1.1.3.1.1 "><p id="p178643281443"><a name="p178643281443"></a><a name="p178643281443"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.1.3.1.2 "><p id="p986422814446"><a name="p986422814446"></a><a name="p986422814446"></a>CSS Clusters</p>
</td>
</tr>
</tbody>
</table>

