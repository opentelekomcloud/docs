# Cluster Lifecycle<a name="cce_01_0005"></a>

This section describes the status of each cluster lifecycle, helping you understand the running status of the cluster in different phases.

**Table  1**  Cluster status description

<a name="table12191040104"></a>
<table><thead align="left"><tr id="row222012402006"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.3.1.1"><p id="p1322094012018"><a name="p1322094012018"></a><a name="p1322094012018"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="74%" id="mcps1.2.3.1.2"><p id="p622024012014"><a name="p622024012014"></a><a name="p622024012014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6220640203"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p822064015018"><a name="p822064015018"></a><a name="p822064015018"></a><span class="keyword" id="keyword820014675154314"><a name="keyword820014675154314"></a><a name="keyword820014675154314"></a>Creating</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p8220440605"><a name="p8220440605"></a><a name="p8220440605"></a>A cluster is being created and is applying for cloud resources.</p>
</td>
</tr>
<tr id="row1822020409010"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p2022034016018"><a name="p2022034016018"></a><a name="p2022034016018"></a><span class="keyword" id="keyword1638575285154316"><a name="keyword1638575285154316"></a><a name="keyword1638575285154316"></a>Normal</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1222014401700"><a name="p1222014401700"></a><a name="p1222014401700"></a>The cluster is running properly.</p>
</td>
</tr>
<tr id="row14220840606"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p10220640508"><a name="p10220640508"></a><a name="p10220640508"></a><span class="keyword" id="keyword1781354701154320"><a name="keyword1781354701154320"></a><a name="keyword1781354701154320"></a>Scaling-out</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p17220184017012"><a name="p17220184017012"></a><a name="p17220184017012"></a>A node is being added to the cluster.</p>
</td>
</tr>
<tr id="row12220440503"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p680253414204"><a name="p680253414204"></a><a name="p680253414204"></a><span class="keyword" id="keyword1868096015155653"><a name="keyword1868096015155653"></a><a name="keyword1868096015155653"></a>Scaling-in</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p9208569201"><a name="p9208569201"></a><a name="p9208569201"></a>A node is being deleted from the cluster.</p>
</td>
</tr>
<tr id="row1224521014401"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p2246111054012"><a name="p2246111054012"></a><a name="p2246111054012"></a>Hibernating</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p72461510194016"><a name="p72461510194016"></a><a name="p72461510194016"></a>The cluster is hibernating.</p>
</td>
</tr>
<tr id="row1450522112209"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p8817339102011"><a name="p8817339102011"></a><a name="p8817339102011"></a>Awaking</p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1250502111207"><a name="p1250502111207"></a><a name="p1250502111207"></a>The cluster is being woken up.</p>
</td>
</tr>
<tr id="row13614111762019"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p1261441762018"><a name="p1261441762018"></a><a name="p1261441762018"></a><span class="keyword" id="keyword1958658580155658"><a name="keyword1958658580155658"></a><a name="keyword1958658580155658"></a>Upgrading</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p1361415175200"><a name="p1361415175200"></a><a name="p1361415175200"></a>The cluster is being upgraded.</p>
</td>
</tr>
<tr id="row142095617205"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p42065612200"><a name="p42065612200"></a><a name="p42065612200"></a><span class="keyword" id="keyword13976410515571"><a name="keyword13976410515571"></a><a name="keyword13976410515571"></a>Unavailable</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p22055652016"><a name="p22055652016"></a><a name="p22055652016"></a>The current cluster is unavailable.</p>
</td>
</tr>
<tr id="row2056716914216"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.3.1.1 "><p id="p13567129172113"><a name="p13567129172113"></a><a name="p13567129172113"></a><span class="keyword" id="keyword407179449155751"><a name="keyword407179449155751"></a><a name="keyword407179449155751"></a>Deleting</span></p>
</td>
<td class="cellrowborder" valign="top" width="74%" headers="mcps1.2.3.1.2 "><p id="p105678916214"><a name="p105678916214"></a><a name="p105678916214"></a>The cluster is being deleted.</p>
</td>
</tr>
</tbody>
</table>

**Figure  1**  Cluster status transition<a name="fig22977482545"></a>  
![](figures/cluster-status-transition.png "cluster-status-transition")

