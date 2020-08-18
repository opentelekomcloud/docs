# Checklist for Migrating Containerized Applications to the Cloud<a name="cce_faq_00006"></a>

## Overview<a name="en-us_topic_0242566240_section277217531231"></a>

Cloud Container Engine \(CCE\) provides highly scalable, high-performance, enterprise-class Kubernetes clusters and supports Docker containers. With CCE, you can easily deploy, manage, and scale out containerized applications.

This checklist describes the system availability, data reliability, and O&M reliability of migrating containerized applications to the cloud. It contains check items, impact, FAQs, and examples, helping you migrate services to CCE and avoid application exceptions or cluster reconstruction caused by improper use.

## Check Items<a name="en-us_topic_0242566240_section182281181291"></a>

**Table  1**  System availability

<a name="en-us_topic_0242566240_table164991312201710"></a>
<table><thead align="left"><tr id="en-us_topic_0242566240_row135006125171"><th class="cellrowborder" valign="top" width="14.090000000000003%" id="mcps1.2.5.1.1"><p id="en-us_topic_0242566240_p75001612181713"><a name="en-us_topic_0242566240_p75001612181713"></a><a name="en-us_topic_0242566240_p75001612181713"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="29.990000000000006%" id="mcps1.2.5.1.2"><p id="en-us_topic_0242566240_p150131214173"><a name="en-us_topic_0242566240_p150131214173"></a><a name="en-us_topic_0242566240_p150131214173"></a>Check Item</p>
</th>
<th class="cellrowborder" valign="top" width="22.330000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0242566240_p125011712171711"><a name="en-us_topic_0242566240_p125011712171711"></a><a name="en-us_topic_0242566240_p125011712171711"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.59%" id="mcps1.2.5.1.4"><p id="en-us_topic_0242566240_p5501512151719"><a name="en-us_topic_0242566240_p5501512151719"></a><a name="en-us_topic_0242566240_p5501512151719"></a>Impact</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0242566240_row14501131220173"><td class="cellrowborder" rowspan="4" valign="top" width="14.090000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p11501191220174"><a name="en-us_topic_0242566240_p11501191220174"></a><a name="en-us_topic_0242566240_p11501191220174"></a>Cluster</p>
</td>
<td class="cellrowborder" valign="top" width="29.990000000000006%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p1650115126174"><a name="en-us_topic_0242566240_p1650115126174"></a><a name="en-us_topic_0242566240_p1650115126174"></a>When creating a cluster, set <strong id="en-us_topic_0242566240_b8813162133119"><a name="en-us_topic_0242566240_b8813162133119"></a><a name="en-us_topic_0242566240_b8813162133119"></a>High Availability</strong> to <strong id="en-us_topic_0242566240_b1881816213313"><a name="en-us_topic_0242566240_b1881816213313"></a><a name="en-us_topic_0242566240_b1881816213313"></a>Yes</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="22.330000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p11501191211174"><a name="en-us_topic_0242566240_p11501191211174"></a><a name="en-us_topic_0242566240_p11501191211174"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" width="33.59%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p16501161281714"><a name="en-us_topic_0242566240_p16501161281714"></a><a name="en-us_topic_0242566240_p16501161281714"></a>A cluster with <strong id="en-us_topic_0242566240_b8461184317318"><a name="en-us_topic_0242566240_b8461184317318"></a><a name="en-us_topic_0242566240_b8461184317318"></a>High Availability</strong> set to <strong id="en-us_topic_0242566240_b1546124353112"><a name="en-us_topic_0242566240_b1546124353112"></a><a name="en-us_topic_0242566240_b1546124353112"></a>No</strong> is a non-HA cluster with only one master. If the master node is faulty, the entire cluster will be unavailable. Therefore, you are advised to create an HA cluster in the production environment.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row1850117122170"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p4501812101719"><a name="en-us_topic_0242566240_p4501812101719"></a><a name="en-us_topic_0242566240_p4501812101719"></a>Before creating a cluster, determine the container network model that is suitable to the service scenario.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p1250131220173"><a name="en-us_topic_0242566240_p1250131220173"></a><a name="en-us_topic_0242566240_p1250131220173"></a>Network planning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p135361626948"><a name="en-us_topic_0242566240_p135361626948"></a><a name="en-us_topic_0242566240_p135361626948"></a>Different container network models apply to different scenarios.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row75011212161711"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p155319281619"><a name="en-us_topic_0242566240_p155319281619"></a><a name="en-us_topic_0242566240_p155319281619"></a>Before creating a cluster, plan the subnet CIDR block and container network CIDR block properly.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p150101291710"><a name="en-us_topic_0242566240_p150101291710"></a><a name="en-us_topic_0242566240_p150101291710"></a>Network planning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p0501151216175"><a name="en-us_topic_0242566240_p0501151216175"></a><a name="en-us_topic_0242566240_p0501151216175"></a>If the range of the subnet and container network CIDR blocks is not properly set, the number of available nodes in the cluster will be less than the number of nodes supported by the cluster. Network planning has different constraints on different container network models.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row1750191218170"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p141771091211"><a name="en-us_topic_0242566240_p141771091211"></a><a name="en-us_topic_0242566240_p141771091211"></a>Before creating a cluster, properly plan CIDR blocks for the related Direct Connect, peering connection, container network, service network, and subnet to avoid IP address conflicts.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p17501151211171"><a name="en-us_topic_0242566240_p17501151211171"></a><a name="en-us_topic_0242566240_p17501151211171"></a>Network planning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p18501312141712"><a name="en-us_topic_0242566240_p18501312141712"></a><a name="en-us_topic_0242566240_p18501312141712"></a>If CIDR blocks are not properly set and IP address conflicts occur, service access will be affected.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row20501101281711"><td class="cellrowborder" rowspan="6" valign="top" width="14.090000000000003%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p0501712141714"><a name="en-us_topic_0242566240_p0501712141714"></a><a name="en-us_topic_0242566240_p0501712141714"></a>Workload</p>
</td>
<td class="cellrowborder" valign="top" width="29.990000000000006%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p1150131216175"><a name="en-us_topic_0242566240_p1150131216175"></a><a name="en-us_topic_0242566240_p1150131216175"></a>When creating a workload, set the upper and lower limits of CPU and memory resources.</p>
</td>
<td class="cellrowborder" valign="top" width="22.330000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p14502212181712"><a name="en-us_topic_0242566240_p14502212181712"></a><a name="en-us_topic_0242566240_p14502212181712"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" width="33.59%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p650251271716"><a name="en-us_topic_0242566240_p650251271716"></a><a name="en-us_topic_0242566240_p650251271716"></a>If the upper and lower resource limits are not set for an application, a resource leak of this application will make resources unavailable for other applications deployed on the same node. In addition, applications that do not have upper and lower resource limits cannot be accurately monitored.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row918205611309"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p2018125612304"><a name="en-us_topic_0242566240_p2018125612304"></a><a name="en-us_topic_0242566240_p2018125612304"></a>When creating an application, set the number of pods to more than two and set the scheduling policy based on service requirements.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p9183565309"><a name="en-us_topic_0242566240_p9183565309"></a><a name="en-us_topic_0242566240_p9183565309"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p71825612306"><a name="en-us_topic_0242566240_p71825612306"></a><a name="en-us_topic_0242566240_p71825612306"></a>A single-pod application will be faulty if the node or pod is faulty.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row161825673020"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p7181656183010"><a name="en-us_topic_0242566240_p7181656183010"></a><a name="en-us_topic_0242566240_p7181656183010"></a>Properly set affinity and anti-affinity.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p1618205603013"><a name="en-us_topic_0242566240_p1618205603013"></a><a name="en-us_topic_0242566240_p1618205603013"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p1218656113019"><a name="en-us_topic_0242566240_p1218656113019"></a><a name="en-us_topic_0242566240_p1218656113019"></a>If affinity and anti-affinity are both configured for an application that provides Services externally, Services may fail to be accessed after the application is upgraded or restarted.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row12493344576"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p6250434165712"><a name="en-us_topic_0242566240_p6250434165712"></a><a name="en-us_topic_0242566240_p6250434165712"></a>When creating a workload, set the health check policy, that is, set the workload liveness probe and the readiness probe.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p725043418577"><a name="en-us_topic_0242566240_p725043418577"></a><a name="en-us_topic_0242566240_p725043418577"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p10251534185714"><a name="en-us_topic_0242566240_p10251534185714"></a><a name="en-us_topic_0242566240_p10251534185714"></a>If the two probes are not set, pods cannot detect service exceptions or automatically restart the service to restore it. This results in a situation where the pod status is normal but the service in the pod is abnormal.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row676864612304"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p6768114643017"><a name="en-us_topic_0242566240_p6768114643017"></a><a name="en-us_topic_0242566240_p6768114643017"></a>When creating a workload, set the pre-stop processing command (<strong id="en-us_topic_0242566240_b730814121392"><a name="en-us_topic_0242566240_b730814121392"></a><a name="en-us_topic_0242566240_b730814121392"></a>Lifecycle</strong> &gt; <strong id="en-us_topic_0242566240_b14309312490"><a name="en-us_topic_0242566240_b14309312490"></a><a name="en-us_topic_0242566240_b14309312490"></a>Pre-Stop</strong>) to ensure that the services running in the pods can be completed in advance in the case of application upgrade or pod deletion.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p77685468309"><a name="en-us_topic_0242566240_p77685468309"></a><a name="en-us_topic_0242566240_p77685468309"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p1076804618309"><a name="en-us_topic_0242566240_p1076804618309"></a><a name="en-us_topic_0242566240_p1076804618309"></a>If the pre-stop processing command is not configured, the pod will be directly killed and services will be interrupted during application upgrade.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row16357154013015"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p13581405302"><a name="en-us_topic_0242566240_p13581405302"></a><a name="en-us_topic_0242566240_p13581405302"></a>When creating a Service, select an access mode based on service requirements. Currently, the following types of access modes are supported: intra-cluster access, intra-VPC access, and external access.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p935844033015"><a name="en-us_topic_0242566240_p935844033015"></a><a name="en-us_topic_0242566240_p935844033015"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p1635814015304"><a name="en-us_topic_0242566240_p1635814015304"></a><a name="en-us_topic_0242566240_p1635814015304"></a>If the access mode is not properly set, internal and external access may be in disorder and resources may be wasted.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Data reliability

<a name="en-us_topic_0242566240_table34517594413"></a>
<table><thead align="left"><tr id="en-us_topic_0242566240_row17452105910416"><th class="cellrowborder" valign="top" width="12.72%" id="mcps1.2.5.1.1"><p id="en-us_topic_0242566240_p19452175916417"><a name="en-us_topic_0242566240_p19452175916417"></a><a name="en-us_topic_0242566240_p19452175916417"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="32.76%" id="mcps1.2.5.1.2"><p id="en-us_topic_0242566240_p17452155913418"><a name="en-us_topic_0242566240_p17452155913418"></a><a name="en-us_topic_0242566240_p17452155913418"></a>Check Item</p>
</th>
<th class="cellrowborder" valign="top" width="16.64%" id="mcps1.2.5.1.3"><p id="en-us_topic_0242566240_p14452155944117"><a name="en-us_topic_0242566240_p14452155944117"></a><a name="en-us_topic_0242566240_p14452155944117"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="37.88%" id="mcps1.2.5.1.4"><p id="en-us_topic_0242566240_p164528599411"><a name="en-us_topic_0242566240_p164528599411"></a><a name="en-us_topic_0242566240_p164528599411"></a>Impact</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0242566240_row174521959164116"><td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p11452195974113"><a name="en-us_topic_0242566240_p11452195974113"></a><a name="en-us_topic_0242566240_p11452195974113"></a>Container data persistency</p>
</td>
<td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p0452185913416"><a name="en-us_topic_0242566240_p0452185913416"></a><a name="en-us_topic_0242566240_p0452185913416"></a>Store application data in the cloud, rather than on a local disk.</p>
</td>
<td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p445295913416"><a name="en-us_topic_0242566240_p445295913416"></a><a name="en-us_topic_0242566240_p445295913416"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p6452125917415"><a name="en-us_topic_0242566240_p6452125917415"></a><a name="en-us_topic_0242566240_p6452125917415"></a>If a node is faulty and cannot be restored, data on the local disk cannot be restored.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row4452125984114"><td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p5452125904110"><a name="en-us_topic_0242566240_p5452125904110"></a><a name="en-us_topic_0242566240_p5452125904110"></a>Backup</p>
</td>
<td class="cellrowborder" valign="top" width="32.76%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p745313591413"><a name="en-us_topic_0242566240_p745313591413"></a><a name="en-us_topic_0242566240_p745313591413"></a>Back up application data.</p>
</td>
<td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p9453125934120"><a name="en-us_topic_0242566240_p9453125934120"></a><a name="en-us_topic_0242566240_p9453125934120"></a>Reliability</p>
</td>
<td class="cellrowborder" valign="top" width="37.88%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p18453559154115"><a name="en-us_topic_0242566240_p18453559154115"></a><a name="en-us_topic_0242566240_p18453559154115"></a>Data cannot be restored after being lost.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  O&M reliability

<a name="en-us_topic_0242566240_table1177832919469"></a>
<table><thead align="left"><tr id="en-us_topic_0242566240_row777822934612"><th class="cellrowborder" valign="top" width="12.668733126687332%" id="mcps1.2.5.1.1"><p id="en-us_topic_0242566240_p6779102924617"><a name="en-us_topic_0242566240_p6779102924617"></a><a name="en-us_topic_0242566240_p6779102924617"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="32.586741325867415%" id="mcps1.2.5.1.2"><p id="en-us_topic_0242566240_p13779102994610"><a name="en-us_topic_0242566240_p13779102994610"></a><a name="en-us_topic_0242566240_p13779102994610"></a>Check Item</p>
</th>
<th class="cellrowborder" valign="top" width="16.43835616438356%" id="mcps1.2.5.1.3"><p id="en-us_topic_0242566240_p7779132913462"><a name="en-us_topic_0242566240_p7779132913462"></a><a name="en-us_topic_0242566240_p7779132913462"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="38.30616938306169%" id="mcps1.2.5.1.4"><p id="en-us_topic_0242566240_p1577915295469"><a name="en-us_topic_0242566240_p1577915295469"></a><a name="en-us_topic_0242566240_p1577915295469"></a>Impact</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0242566240_row137791294464"><td class="cellrowborder" rowspan="3" valign="top" width="12.668733126687332%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p1477919292464"><a name="en-us_topic_0242566240_p1477919292464"></a><a name="en-us_topic_0242566240_p1477919292464"></a>Project</p>
<p id="en-us_topic_0242566240_p37791629144613"><a name="en-us_topic_0242566240_p37791629144613"></a><a name="en-us_topic_0242566240_p37791629144613"></a></p>
<p id="en-us_topic_0242566240_p18780529124612"><a name="en-us_topic_0242566240_p18780529124612"></a><a name="en-us_topic_0242566240_p18780529124612"></a></p>
</td>
<td class="cellrowborder" valign="top" width="32.586741325867415%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p3779182912468"><a name="en-us_topic_0242566240_p3779182912468"></a><a name="en-us_topic_0242566240_p3779182912468"></a>The quotas of ECS, VPC, subnet, EIP, and EVS resources must meet customer requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="16.43835616438356%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p15779172984614"><a name="en-us_topic_0242566240_p15779172984614"></a><a name="en-us_topic_0242566240_p15779172984614"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" width="38.30616938306169%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p20779162914614"><a name="en-us_topic_0242566240_p20779162914614"></a><a name="en-us_topic_0242566240_p20779162914614"></a>If the quota is insufficient, resources will fail to be created. Specifically, users who have configured automatic capacity expansion must have sufficient resource quotas.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row10779102919461"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p147791329154618"><a name="en-us_topic_0242566240_p147791329154618"></a><a name="en-us_topic_0242566240_p147791329154618"></a>Do not install private software or modify OS configurations on a cluster node.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p1177917296468"><a name="en-us_topic_0242566240_p1177917296468"></a><a name="en-us_topic_0242566240_p1177917296468"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p3779102919464"><a name="en-us_topic_0242566240_p3779102919464"></a><a name="en-us_topic_0242566240_p3779102919464"></a>If private software is installed on a cluster node or OS configurations are modified, exceptions may occur on Kubernetes components on the node, making it unavailable for application deployment.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row19779142934618"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p137801295461"><a name="en-us_topic_0242566240_p137801295461"></a><a name="en-us_topic_0242566240_p137801295461"></a>Do not modify information about resources created by CCE, such as security groups and EVS disks. Resources created by CCE are labeled <strong id="en-us_topic_0242566240_b824395071512"><a name="en-us_topic_0242566240_b824395071512"></a><a name="en-us_topic_0242566240_b824395071512"></a>cce</strong>.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p27801829144618"><a name="en-us_topic_0242566240_p27801829144618"></a><a name="en-us_topic_0242566240_p27801829144618"></a>Deployment</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p8780142913462"><a name="en-us_topic_0242566240_p8780142913462"></a><a name="en-us_topic_0242566240_p8780142913462"></a>CCE cluster functions may be abnormal.</p>
</td>
</tr>
<tr id="en-us_topic_0242566240_row8780182974617"><td class="cellrowborder" valign="top" width="12.668733126687332%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0242566240_p978082984614"><a name="en-us_topic_0242566240_p978082984614"></a><a name="en-us_topic_0242566240_p978082984614"></a>Proactive O&amp;M</p>
</td>
<td class="cellrowborder" valign="top" width="32.586741325867415%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0242566240_p778002974612"><a name="en-us_topic_0242566240_p778002974612"></a><a name="en-us_topic_0242566240_p778002974612"></a>Configure alarm monitoring on AOM for the applications you deployed in CCE clusters.</p>
</td>
<td class="cellrowborder" valign="top" width="16.43835616438356%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0242566240_p4780192914467"><a name="en-us_topic_0242566240_p4780192914467"></a><a name="en-us_topic_0242566240_p4780192914467"></a>Monitoring</p>
</td>
<td class="cellrowborder" valign="top" width="38.30616938306169%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0242566240_p3780172964611"><a name="en-us_topic_0242566240_p3780172964611"></a><a name="en-us_topic_0242566240_p3780172964611"></a>If alarm monitoring is not configured, you cannot receive alarms when applications are faulty and need to manually locate the faults.</p>
</td>
</tr>
</tbody>
</table>

