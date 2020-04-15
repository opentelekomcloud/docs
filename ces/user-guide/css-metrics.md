# CSS Metrics<a name="EN-US_TOPIC_0102610089"></a>

**Table  1**  CSS metrics

<a name="table102675383222"></a>
<table><thead align="left"><tr id="row726893842214"><th class="cellrowborder" valign="top" width="16.7016701670167%" id="mcps1.2.7.1.1"><p id="p54981328154714"><a name="p54981328154714"></a><a name="p54981328154714"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="15.23152315231523%" id="mcps1.2.7.1.2"><p id="p16270153816220"><a name="p16270153816220"></a><a name="p16270153816220"></a>Metric</p>
</th>
<th class="cellrowborder" valign="top" width="21.372137213721373%" id="mcps1.2.7.1.3"><p id="p527115383221"><a name="p527115383221"></a><a name="p527115383221"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.171917191719174%" id="mcps1.2.7.1.4"><p id="p202711238192210"><a name="p202711238192210"></a><a name="p202711238192210"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.7.1.5"><p id="p52723385226"><a name="p52723385226"></a><a name="p52723385226"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="14.65146514651465%" id="mcps1.2.7.1.6"><p id="p2152145910542"><a name="p2152145910542"></a><a name="p2152145910542"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row12119181122417"><td class="cellrowborder" valign="top" width="16.7016701670167%" headers="mcps1.2.7.1.1 "><p id="p9726175820227"><a name="p9726175820227"></a><a name="p9726175820227"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="15.23152315231523%" headers="mcps1.2.7.1.2 "><p id="p530281982319"><a name="p530281982319"></a><a name="p530281982319"></a>Cluster Health Status</p>
</td>
<td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.7.1.3 "><p id="p87261958132220"><a name="p87261958132220"></a><a name="p87261958132220"></a>Health status of the monitored object</p>
</td>
<td class="cellrowborder" valign="top" width="19.171917191719174%" headers="mcps1.2.7.1.4 "><p id="p1431964322314"><a name="p1431964322314"></a><a name="p1431964322314"></a><strong id="b117611531776"><a name="b117611531776"></a><a name="b117611531776"></a>0</strong>, <strong id="b203471154173"><a name="b203471154173"></a><a name="b203471154173"></a>1</strong>, and <strong id="b1621310571715"><a name="b1621310571715"></a><a name="b1621310571715"></a>2</strong></p>
<p id="p1787419542187"><a name="p1787419542187"></a><a name="p1787419542187"></a><strong id="b1228975832516"><a name="b1228975832516"></a><a name="b1228975832516"></a>0</strong>: The cluster is 100% operational.</p>
<p id="p11571853191713"><a name="p11571853191713"></a><a name="p11571853191713"></a><strong id="b484411302610"><a name="b484411302610"></a><a name="b484411302610"></a>1</strong>: Some replicas are missing. Your data is complete, but exceptions may occur because your high availability is compromised.</p>
<p id="p8807115951710"><a name="p8807115951710"></a><a name="p8807115951710"></a><strong id="b158451755112612"><a name="b158451755112612"></a><a name="b158451755112612"></a>2</strong>: Data missing occurs and the cluster fails to work.</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.5 "><p id="p1932044312237"><a name="p1932044312237"></a><a name="p1932044312237"></a>CSS cluster</p>
</td>
<td class="cellrowborder" valign="top" width="14.65146514651465%" headers="mcps1.2.7.1.6 "><p id="p915215955416"><a name="p915215955416"></a><a name="p915215955416"></a>1 minute</p>
</td>
</tr>
<tr id="row2272193812219"><td class="cellrowborder" valign="top" width="16.7016701670167%" headers="mcps1.2.7.1.1 "><p id="p207641617184420"><a name="p207641617184420"></a><a name="p207641617184420"></a>disk_util</p>
</td>
<td class="cellrowborder" valign="top" width="15.23152315231523%" headers="mcps1.2.7.1.2 "><p id="p776471711444"><a name="p776471711444"></a><a name="p776471711444"></a>Disk Usage</p>
</td>
<td class="cellrowborder" valign="top" width="21.372137213721373%" headers="mcps1.2.7.1.3 "><p id="p17648171448"><a name="p17648171448"></a><a name="p17648171448"></a>Disk usage of the monitored object</p>
<p id="p1986421575118"><a name="p1986421575118"></a><a name="p1986421575118"></a>Unit: Percent</p>
</td>
<td class="cellrowborder" valign="top" width="19.171917191719174%" headers="mcps1.2.7.1.4 "><p id="p1676461734411"><a name="p1676461734411"></a><a name="p1676461734411"></a>0-100%</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.7.1.5 "><p id="p173746537577"><a name="p173746537577"></a><a name="p173746537577"></a>CSS cluster</p>
</td>
<td class="cellrowborder" valign="top" width="14.65146514651465%" headers="mcps1.2.7.1.6 "><p id="p181528592546"><a name="p181528592546"></a><a name="p181528592546"></a>1 minute</p>
</td>
</tr>
</tbody>
</table>

