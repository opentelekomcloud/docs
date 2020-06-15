# kubectl Usage Guide<a name="cce_01_0023"></a>

Before running  Kubectl  commands, you should have the Kubectl development skills and understand the Kubectl operations. For details, see  [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)  and  [Kubetl CLI](https://kubernetes.io/docs/reference/kubectl/overview/).

**Table  1**  kubectl usage guide

<a name="table4373319566"></a>
<table><thead align="left"><tr id="row939163115620"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p1353119199565"><a name="p1353119199565"></a><a name="p1353119199565"></a>Task</p>
</th>
<th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p53917335610"><a name="p53917335610"></a><a name="p53917335610"></a>kubectl Usage</p>
</th>
</tr>
</thead>
<tbody><tr id="row123917316569"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p8531919135617"><a name="p8531919135617"></a><a name="p8531919135617"></a>Connecting to a <span class="keyword" id="keyword10871712173515"><a name="keyword10871712173515"></a><a name="keyword10871712173515"></a>cluster</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1239183205611"><a name="p1239183205611"></a><a name="p1239183205611"></a><a href="connecting-to-a-kubernetes-cluster-using-kubectl.md">Connecting to a Kubernetes Cluster Using kubectl</a></p>
</td>
</tr>
<tr id="row891519223810"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p491622211811"><a name="p491622211811"></a><a name="p491622211811"></a><span class="keyword" id="keyword331034414163442"><a name="keyword331034414163442"></a><a name="keyword331034414163442"></a>kube-dns</span> <span class="keyword" id="keyword1734901100163444"><a name="keyword1734901100163444"></a><a name="keyword1734901100163444"></a>HA</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p7916162220816"><a name="p7916162220816"></a><a name="p7916162220816"></a><a href="configuring-high-availability-of-kube-dns-coredns-using-kubectl.md">Configuring High Availability of kube-dns/coredns Using kubectl</a></p>
</td>
</tr>
<tr id="row183953145614"><td class="cellrowborder" rowspan="2" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p19239401986"><a name="p19239401986"></a><a name="p19239401986"></a>Creating a workload</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p53918315564"><a name="p53918315564"></a><a name="p53918315564"></a><a href="creating-a-deployment.md#section155246177178">Creating a Deployment Using kubectl</a></p>
</td>
</tr>
<tr id="row9391730563"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p103917345612"><a name="p103917345612"></a><a name="p103917345612"></a><a href="creating-a-statefulset.md#section113441881214">Creating a StatefulSet Using kubectl</a></p>
</td>
</tr>
<tr id="row1339233567"><td class="cellrowborder" rowspan="6" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p104807404911"><a name="p104807404911"></a><a name="p104807404911"></a>Workload <span class="keyword" id="keyword2125179630163515"><a name="keyword2125179630163515"></a><a name="keyword2125179630163515"></a>affinity</span>/<span class="keyword" id="keyword1303019494163518"><a name="keyword1303019494163518"></a><a name="keyword1303019494163518"></a>anti-affinity</span> scheduling</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1641153105613"><a name="p1641153105613"></a><a name="p1641153105613"></a><a href="workload-node-affinity.md#section711574271117">Example YAML for Running a Workload on a Specified Node</a></p>
</td>
</tr>
<tr id="row1341103105616"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p641183115613"><a name="p641183115613"></a><a name="p641183115613"></a><a href="workload-node-anti-affinity.md#section1361482522712">Example YAML for Refraining a Workload from Running on a Specified Node</a></p>
</td>
</tr>
<tr id="row1141113135619"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p94173185614"><a name="p94173185614"></a><a name="p94173185614"></a><a href="workload-workload-affinity.md#section5140193643912">Example YAML for Co-locating Workloads on the Same Node</a></p>
</td>
</tr>
<tr id="row5179024686"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1818120241088"><a name="p1818120241088"></a><a name="p1818120241088"></a><a href="workload-workload-anti-affinity.md#section1894310152317">Example YAML for Running Workloads on Different Nodes</a></p>
</td>
</tr>
<tr id="row41820243812"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1018212418818"><a name="p1018212418818"></a><a name="p1018212418818"></a><a href="workload-az-affinity.md#section4201420133117">Example YAML for Running a Workload in a Specified AZ</a></p>
</td>
</tr>
<tr id="row17182122410811"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1718232418812"><a name="p1718232418812"></a><a name="p1718232418812"></a><a href="workload-az-anti-affinity.md#section102822029173111">Example YAML for Refraining a Workload from Running in a Specified AZ</a></p>
</td>
</tr>
<tr id="row134570472507"><td class="cellrowborder" rowspan="5" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p54571347155012"><a name="p54571347155012"></a><a name="p54571347155012"></a><span class="keyword" id="keyword5305161855114"><a name="keyword5305161855114"></a><a name="keyword5305161855114"></a>Workload access mode</span> settings</p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p9457204705017"><a name="p9457204705017"></a><a name="p9457204705017"></a><a href="intra-cluster-access-(clusterip).md">Implementing Intra-Cluster Access Using kubectl</a></p>
</td>
</tr>
<tr id="row27191745105013"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p671919450507"><a name="p671919450507"></a><a name="p671919450507"></a><a href="nodeport.md#section813715073217">Implementing Intra-VPC Access Using kubectl</a></p>
</td>
</tr>
<tr id="row1381416402507"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1381424005017"><a name="p1381424005017"></a><a name="p1381424005017"></a><a href="loadbalancer.md">Implementing Layer 4 Load Balancing Using kubectl</a></p>
</td>
</tr>
<tr id="row138591638155014"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p185973818507"><a name="p185973818507"></a><a name="p185973818507"></a><a href="nodeport.md#section178584033417">Implementing EIP-based Access Using kubectl</a></p>
</td>
</tr>
<tr id="row1080633614505"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p18075363502"><a name="p18075363502"></a><a name="p18075363502"></a><a href="layer-7-load-balancing-(ingress).md#section1944313158364">Implementing Layer 7 Load Balancing Using kubectl</a></p>
</td>
</tr>
<tr id="row612955614108"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p171821246813"><a name="p171821246813"></a><a name="p171821246813"></a><span class="keyword" id="keyword1569546850163650"><a name="keyword1569546850163650"></a><a name="keyword1569546850163650"></a>Workload advanced settings</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p201821924182"><a name="p201821924182"></a><a name="p201821924182"></a><a href="setting-container-lifecycle-parameters.md#section151181981167">Example YAML for Setting the Container Lifecycle</a></p>
</td>
</tr>
<tr id="row1151169125"><td class="cellrowborder" rowspan="2" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p96316171219"><a name="p96316171219"></a><a name="p96316171219"></a><span class="keyword" id="keyword719890177163712"><a name="keyword719890177163712"></a><a name="keyword719890177163712"></a>Task management</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p961016191214"><a name="p961016191214"></a><a name="p961016191214"></a><a href="creating-a-job.md#section450152719412">Creating a Job Using kubectl</a></p>
</td>
</tr>
<tr id="row143011122131214"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p83011622121215"><a name="p83011622121215"></a><a name="p83011622121215"></a><a href="creating-a-cron-job.md#section13519162224919">Creating a Cron Job Using kubectl</a></p>
</td>
</tr>
<tr id="row9301132271214"><td class="cellrowborder" rowspan="2" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p10301122121214"><a name="p10301122121214"></a><a name="p10301122121214"></a><span class="keyword" id="keyword1611535067163714"><a name="keyword1611535067163714"></a><a name="keyword1611535067163714"></a>Configuration center</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p193011222120"><a name="p193011222120"></a><a name="p193011222120"></a><a href="creating-a-configmap.md#section639712716372">Creating a ConfigMap Using kubectl</a></p>
</td>
</tr>
<tr id="row193016226127"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p113035222125"><a name="p113035222125"></a><a name="p113035222125"></a><a href="creating-a-secret.md#section821112149514">Creating a Secret Using kubectl</a></p>
</td>
</tr>
<tr id="row46702615201"><td class="cellrowborder" rowspan="4" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1168172611206"><a name="p1168172611206"></a><a name="p1168172611206"></a><span class="keyword" id="keyword1650232884"><a name="keyword1650232884"></a><a name="keyword1650232884"></a>Storage management</span></p>
</td>
<td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p66810264201"><a name="p66810264201"></a><a name="p66810264201"></a><a href="using-evs-disks-for-storage.md#section198505107598">Creating an EVS Disk Using kubectl</a></p>
</td>
</tr>
<tr id="row3707532132012"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p117081732102015"><a name="p117081732102015"></a><a name="p117081732102015"></a><a href="using-evs-disks-for-storage.md#section1996254515127">Mounting an EVS Disk Using kubectl</a></p>
</td>
</tr>
<tr id="row44771630132017"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p6477193011201"><a name="p6477193011201"></a><a name="p6477193011201"></a><a href="using-sfs-file-systems-for-storage.md#section5806637172015">Creating an SFS File System Using kubectl</a></p>
</td>
</tr>
<tr id="row93481281209"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p5348328192012"><a name="p5348328192012"></a><a name="p5348328192012"></a><a href="using-sfs-file-systems-for-storage.md#section1094712153215">Mounting SFS File Systems Using kubectl</a></p>
</td>
</tr>
</tbody>
</table>

