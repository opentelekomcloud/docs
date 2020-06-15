# Viewing the Cluster List<a name="dws_01_0020"></a>

On the  **Cluster Management**  page, you can view the brief information about all clusters.

## Cluster List Overview<a name="section1864014116328"></a>

Log in to the DWS management console. In the navigation tree on the left, click  **Cluster Management**. The cluster list displays all created clusters. If there are a large number of clusters, you can turn pages to view the clusters in any status

Clusters that fail to be created are not displayed in the cluster list. For more information, see section  [Managing Clusters That Fail to Be Created](managing-clusters-that-fail-to-be-created.md).

Clusters are listed in chronological order by default, with the most recent clusters displayed at the top.  [Table 1](#table3950169215120)  lists the cluster list parameters.

**Figure  1**  Cluster list<a name="fig424813487315"></a>  
![](figures/cluster-list.png "cluster-list")

**Table  1**  Cluster list parameters

<a name="table3950169215120"></a>
<table><thead align="left"><tr id="row2555468715120"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p4021197415120"><a name="p4021197415120"></a><a name="p4021197415120"></a><strong id="b44458202184919"><a name="b44458202184919"></a><a name="b44458202184919"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p3594448915120"><a name="p3594448915120"></a><a name="p3594448915120"></a><strong id="b4530545184410"><a name="b4530545184410"></a><a name="b4530545184410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3067086316226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p4535230516226"><a name="p4535230516226"></a><a name="p4535230516226"></a>Cluster Name</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p186225616226"><a name="p186225616226"></a><a name="p186225616226"></a>Cluster name specified when a cluster is created</p>
</td>
</tr>
<tr id="row4848715816226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p2038980616226"><a name="p2038980616226"></a><a name="p2038980616226"></a>Cluster Status</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p4372926616226"><a name="p4372926616226"></a><a name="p4372926616226"></a>Cluster running status. For details, see <a href="#table344018476323">Table 2</a>.</p>
</td>
</tr>
<tr id="row79178716226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p336023416226"><a name="p336023416226"></a><a name="p336023416226"></a>Task Information</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p4130844516226"><a name="p4130844516226"></a><a name="p4130844516226"></a>Cluster task status. For details, see <a href="#table14807124711323">Table 3</a>.</p>
</td>
</tr>
<tr id="row3434627416226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p3691952116226"><a name="p3691952116226"></a><a name="p3691952116226"></a>Node Flavor</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p4620786916226"><a name="p4620786916226"></a><a name="p4620786916226"></a>Node flavors of clusters. For details, see section <a href="creating-a-cluster.md#table111901234141316">Table 3</a>.</p>
</td>
</tr>
<tr id="row1241899616226"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p3154882516226"><a name="p3154882516226"></a><a name="p3154882516226"></a>Operation</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><a name="ul8157907161719"></a><a name="ul8157907161719"></a><ul id="ul8157907161719"><li><strong id="b3717750114317"><a name="b3717750114317"></a><a name="b3717750114317"></a>View Metric</strong>: For details, see section <a href="monitoring-a-cluster.md">Monitoring a Cluster</a>.</li><li><strong id="b132715820439"><a name="b132715820439"></a><a name="b132715820439"></a>Restart</strong>: Click <span class="uicontrol" id="uicontrol5732216124314"><a name="uicontrol5732216124314"></a><a name="uicontrol5732216124314"></a><b>Restart</b></span> to restart a cluster. For details, see section <a href="restarting-a-cluster.md">Restarting a Cluster</a>.</li><li><strong id="b423334017439"><a name="b423334017439"></a><a name="b423334017439"></a>More</strong><a name="ul63475607161741"></a><a name="ul63475607161741"></a><ul id="ul63475607161741"><li><strong id="b513911834416"><a name="b513911834416"></a><a name="b513911834416"></a>Scale Out</strong>: For details, see section <a href="scaling-out-a-cluster.md">Scaling Out a Cluster</a>.</li><li><strong id="b1139053664418"><a name="b1139053664418"></a><a name="b1139053664418"></a>Reset Password</strong>: For details, see section <a href="resetting-the-password-of-the-cluster-administrator.md">Resetting the Password of the Cluster Administrator</a>.</li><li><strong id="b987553454510"><a name="b987553454510"></a><a name="b987553454510"></a>Change Parameter Group</strong>: For details, see section <a href="managing-parameter-groups.md#section2615131874812">Changing the Parameter Group</a>.</li><li><strong id="b205001347124511"><a name="b205001347124511"></a><a name="b205001347124511"></a>Delete</strong>: Click <strong id="b20968165112457"><a name="b20968165112457"></a><a name="b20968165112457"></a>Delete</strong> to delete a cluster. For details, see section <a href="deleting-a-cluster.md">Deleting a Cluster</a>.</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

The following table describes cluster statuses:

**Table  2**  Cluster status description

<a name="table344018476323"></a>
<table><thead align="left"><tr id="row7467447173216"><th class="cellrowborder" valign="top" width="16.07%" id="mcps1.2.3.1.1"><p id="p5491847123220"><a name="p5491847123220"></a><a name="p5491847123220"></a><strong id="a816cb4668a2f4064a090e5167d622d2c"><a name="a816cb4668a2f4064a090e5167d622d2c"></a><a name="a816cb4668a2f4064a090e5167d622d2c"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="83.93%" id="mcps1.2.3.1.2"><p id="p17505134714326"><a name="p17505134714326"></a><a name="p17505134714326"></a><strong id="b1861928191910"><a name="b1861928191910"></a><a name="b1861928191910"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row952284720329"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p105311547193216"><a name="p105311547193216"></a><a name="p105311547193216"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p554094714326"><a name="p554094714326"></a><a name="p554094714326"></a>Indicates that the cluster runs properly.</p>
</td>
</tr>
<tr id="row135451047193216"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p155413470325"><a name="p155413470325"></a><a name="p155413470325"></a>Read-only</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p1156694703214"><a name="p1156694703214"></a><a name="p1156694703214"></a>A cluster goes into this status when the cluster storage usage is greater than 90%. The cluster can still work in this status but supports only query operations. You can check the disk capacity and scale out the disk when its capacity is insufficient. For details, see section <a href="scaling-out-a-cluster.md">Scaling Out a Cluster</a>.</p>
</td>
</tr>
<tr id="row457484763217"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p145833473325"><a name="p145833473325"></a><a name="p145833473325"></a>Low performance</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p16591747203211"><a name="p16591747203211"></a><a name="p16591747203211"></a>A cluster goes into this status when some nodes in the cluster cannot work properly, which has no adverse impact on DWS. The cluster can still work in this status. You can restart the cluster to restore the nodes. For details, see section <a href="restarting-a-cluster.md">Restarting a Cluster</a>.</p>
</td>
</tr>
<tr id="row1600154714320"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p1860813470320"><a name="p1860813470320"></a><a name="p1860813470320"></a>Redistributing</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p10617104793217"><a name="p10617104793217"></a><a name="p10617104793217"></a>A cluster goes into this status when it detects that the service data volume on the original nodes is significantly larger than that on the new node after a new node is added to the cluster. In this case, the system automatically redistributes data on all nodes. The cluster can still work in this status.</p>
</td>
</tr>
<tr id="row5621204793218"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p20628174743220"><a name="p20628174743220"></a><a name="p20628174743220"></a>Redistribution failed</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p206356473329"><a name="p206356473329"></a><a name="p206356473329"></a>A cluster goes into this status when data redistribution fails, but no data loss occurs. The cluster can still work in this status. You are advised to contact technical support.</p>
</td>
</tr>
<tr id="row2639047183212"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p06487471323"><a name="p06487471323"></a><a name="p06487471323"></a>Degraded</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p136562047133218"><a name="p136562047133218"></a><a name="p136562047133218"></a>A cluster goes into this status when some nodes in the cluster are faulty, but the whole cluster runs properly. You are advised to contact technical support.</p>
</td>
</tr>
<tr id="row1966054714329"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p266984710320"><a name="p266984710320"></a><a name="p266984710320"></a>Unavailable</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p186791347173217"><a name="p186791347173217"></a><a name="p186791347173217"></a>A cluster goes into this status when it cannot provide the database service. You are advised to contact technical support.</p>
</td>
</tr>
<tr id="row106841547183214"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p1969354711323"><a name="p1969354711323"></a><a name="p1969354711323"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p117011847113211"><a name="p117011847113211"></a><a name="p117011847113211"></a>Indicates that a cluster is being created.</p>
</td>
</tr>
<tr id="row2705134711324"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p117191747123211"><a name="p117191747123211"></a><a name="p117191747123211"></a>Creation failed</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p672894711324"><a name="p672894711324"></a><a name="p672894711324"></a>Indicates that a cluster fails to be created.</p>
</td>
</tr>
<tr id="row97338474329"><td class="cellrowborder" valign="top" width="16.07%" headers="mcps1.2.3.1.1 "><p id="p07411847113220"><a name="p07411847113220"></a><a name="p07411847113220"></a>Creating, restoring</p>
</td>
<td class="cellrowborder" valign="top" width="83.93%" headers="mcps1.2.3.1.2 "><p id="p67492047133214"><a name="p67492047133214"></a><a name="p67492047133214"></a>Indicates that a cluster is being created and it is restored from a snapshot. In this status, the cluster is being restored. A snapshot will be restored to a new cluster. During the process, the new cluster goes into this status.</p>
</td>
</tr>
</tbody>
</table>

The following table describes cluster task statuses:

**Table  3**  Task information description

<a name="table14807124711323"></a>
<table><thead align="left"><tr id="row17827194743213"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.3.1.1"><p id="p14831184753216"><a name="p14831184753216"></a><a name="p14831184753216"></a><strong id="b12833731175310"><a name="b12833731175310"></a><a name="b12833731175310"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="83.59%" id="mcps1.2.3.1.2"><p id="p128371347163220"><a name="p128371347163220"></a><a name="p128371347163220"></a><strong id="b88810328535"><a name="b88810328535"></a><a name="b88810328535"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17844194783220"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p38489474328"><a name="p38489474328"></a><a name="p38489474328"></a>Creating snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p98542047153210"><a name="p98542047153210"></a><a name="p98542047153210"></a>Indicates that a snapshot is being created in the cluster.</p>
</td>
</tr>
<tr id="row1785714479326"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p7862147193210"><a name="p7862147193210"></a><a name="p7862147193210"></a>Snapshot creation failed</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p1286814714328"><a name="p1286814714328"></a><a name="p1286814714328"></a>Indicates that a snapshot fails to be created.</p>
</td>
</tr>
<tr id="row11870134719324"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p12875194715326"><a name="p12875194715326"></a><a name="p12875194715326"></a>Configuring</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p1287914712322"><a name="p1287914712322"></a><a name="p1287914712322"></a>Indicates that the system is storing modifications of cluster parameters.</p>
</td>
</tr>
<tr id="row48815471322"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p1188594733212"><a name="p1188594733212"></a><a name="p1188594733212"></a>Restarting</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p188904479327"><a name="p188904479327"></a><a name="p188904479327"></a>Indicates that a cluster is being restarted.</p>
</td>
</tr>
<tr id="row78921647123215"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p48961447183219"><a name="p48961447183219"></a><a name="p48961447183219"></a>Restart failed</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p1990011478328"><a name="p1990011478328"></a><a name="p1990011478328"></a>Indicates that a cluster fails to be restarted.</p>
</td>
</tr>
<tr id="row15902164714327"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p1690554743210"><a name="p1690554743210"></a><a name="p1690554743210"></a>Scaling out</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p19911447193216"><a name="p19911447193216"></a><a name="p19911447193216"></a>Indicates that a cluster is being scaled out.</p>
</td>
</tr>
<tr id="row119151247113219"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.3.1.1 "><p id="p199221947183217"><a name="p199221947183217"></a><a name="p199221947183217"></a>Scale-out failed</p>
</td>
<td class="cellrowborder" valign="top" width="83.59%" headers="mcps1.2.3.1.2 "><p id="p793318470327"><a name="p793318470327"></a><a name="p793318470327"></a>Indicates that a cluster fails to be scaled out.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Button description

<a name="table14995478145753"></a>
<table><thead align="left"><tr id="row34648328145753"><th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.3.1.1"><p id="p25698260145753"><a name="p25698260145753"></a><a name="p25698260145753"></a><strong id="b1135112365620"><a name="b1135112365620"></a><a name="b1135112365620"></a>Button</strong></p>
</th>
<th class="cellrowborder" valign="top" width="83.35000000000001%" id="mcps1.2.3.1.2"><p id="p1184341145753"><a name="p1184341145753"></a><a name="p1184341145753"></a><strong id="b842352706191716"><a name="b842352706191716"></a><a name="b842352706191716"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60954660145753"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.3.1.1 "><p id="p1171986415013"><a name="p1171986415013"></a><a name="p1171986415013"></a><a name="image145412311186"></a><a name="image145412311186"></a><span><img id="image145412311186" src="figures/icon-dws-search-cluster-02.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="83.35000000000001%" headers="mcps1.2.3.1.2 "><p id="p2095556215013"><a name="p2095556215013"></a><a name="p2095556215013"></a>Enter the cluster name in the search box, and click <a name="image913333811816"></a><a name="image913333811816"></a><span><img id="image913333811816" src="figures/icon-dws-search-cluster-02.png"></span> to search a cluster.</p>
</td>
</tr>
<tr id="row5392135513410"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.3.1.1 "><p id="p1427711183519"><a name="p1427711183519"></a><a name="p1427711183519"></a>Search by Tag</p>
</td>
<td class="cellrowborder" valign="top" width="83.35000000000001%" headers="mcps1.2.3.1.2 "><p id="p73922551348"><a name="p73922551348"></a><a name="p73922551348"></a>Click <span class="uicontrol" id="uicontrol44951351125611"><a name="uicontrol44951351125611"></a><a name="uicontrol44951351125611"></a><b>Search by Tag</b></span> to expand the tag page, on which you can set tag filtering criteria to search for clusters. For details, see section <a href="tag-management.md#section887643535616">Searching for Clusters Based on Tags</a>.</p>
</td>
</tr>
<tr id="row62041377145753"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.3.1.1 "><p id="p5049056515013"><a name="p5049056515013"></a><a name="p5049056515013"></a><a name="image1163515308616"></a><a name="image1163515308616"></a><span><img id="image1163515308616" src="figures/icon-dws-refresh-02.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="83.35000000000001%" headers="mcps1.2.3.1.2 "><p id="p3196483515013"><a name="p3196483515013"></a><a name="p3196483515013"></a>Click <a name="image8968728474"></a><a name="image8968728474"></a><span><img id="image8968728474" src="figures/icon-dws-refresh-02.png"></span> to manually refresh the cluster list.</p>
</td>
</tr>
</tbody>
</table>

