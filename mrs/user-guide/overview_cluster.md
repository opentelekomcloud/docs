# Overview<a name="EN-US_TOPIC_0125375628"></a>

You can view the overall cluster status on the  **Dashboard \> Overview** page, and obtain relevant MRS documents by clicking the document name under **Helpful Links**.

MRS helps manage and analyze massive data. MRS is easy to use and allows you to create a cluster in about 20 minutes. You can add MapReduce, Spark, and Hive jobs to clusters to process and analyze user data. Additionally, processed data can be encrypted by using Secure Sockets Layer \(SSL\) and transmitted to OBS, ensuring data security and integrity.

## Cluster Status<a name="section36109842165553"></a>

[Table 1](#table164091551415)  describes the possible status of each cluster on the MRS management console.

**Table  1**  Cluster status

<a name="table164091551415"></a>
<table><thead align="left"><tr id="row440945515411"><th class="cellrowborder" valign="top" width="25.759999999999998%" id="mcps1.2.3.1.1"><p id="p840912551345"><a name="p840912551345"></a><a name="p840912551345"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="74.24%" id="mcps1.2.3.1.2"><p id="p1640917551148"><a name="p1640917551148"></a><a name="p1640917551148"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14784105351"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p378520517517"><a name="p378520517517"></a><a name="p378520517517"></a>Starting</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p1778510518511"><a name="p1778510518511"></a><a name="p1778510518511"></a><span>A cluster is being created.</span></p>
</td>
</tr>
<tr id="row18409155844"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p240917551947"><a name="p240917551947"></a><a name="p240917551947"></a>Running</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p1240915559419"><a name="p1240915559419"></a><a name="p1240915559419"></a><span>A cluster has been created successfully and all components in the cluster are </span>running properly<span>.</span></p>
</td>
</tr>
<tr id="row16360650133424"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p19235707133445"><a name="p19235707133445"></a><a name="p19235707133445"></a>Expanding</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p14588430133445"><a name="p14588430133445"></a><a name="p14588430133445"></a>Core/Task nodes are being added to a cluster.</p>
</td>
</tr>
<tr id="row17478813103852"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p1640160103852"><a name="p1640160103852"></a><a name="p1640160103852"></a>Shrinking</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p24178000103852"><a name="p24178000103852"></a><a name="p24178000103852"></a>The <strong id="b6237062511139"><a name="b6237062511139"></a><a name="b6237062511139"></a>Shrinking</strong> state is displayed when a node is being deleted in the following operations: shutting down the node, deleting the node, changing the OS of the node, reinstalling the OS of the node, and modifying the specifications of the node.</p>
</td>
</tr>
<tr id="row2041010551541"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p13410135511418"><a name="p13410135511418"></a><a name="p13410135511418"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p3410185514420"><a name="p3410185514420"></a><a name="p3410185514420"></a>Some components in a cluster are abnormal, and the cluster is abnormal.</p>
</td>
</tr>
<tr id="row34101551248"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p536874921661"><a name="p536874921661"></a><a name="p536874921661"></a>Terminating</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p1241025512411"><a name="p1241025512411"></a><a name="p1241025512411"></a><span>A cluster is being </span>terminated<span>.</span></p>
</td>
</tr>
<tr id="row49906879133244"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p39083470133335"><a name="p39083470133335"></a><a name="p39083470133335"></a>Failed</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p11644483133335"><a name="p11644483133335"></a><a name="p11644483133335"></a>Cluster creation, termination, or capacity expansion fails.</p>
</td>
</tr>
<tr id="row20910863133251"><td class="cellrowborder" valign="top" width="25.759999999999998%" headers="mcps1.2.3.1.1 "><p id="p23603928133312"><a name="p23603928133312"></a><a name="p23603928133312"></a>Terminated</p>
</td>
<td class="cellrowborder" valign="top" width="74.24%" headers="mcps1.2.3.1.2 "><p id="p32870020133312"><a name="p32870020133312"></a><a name="p32870020133312"></a><span>A cluster has been </span>terminated<span>.</span></p>
</td>
</tr>
</tbody>
</table>

## Job Status<a name="section28322884165637"></a>

[Table 2](#table792216529274)  describes the status of jobs that you can add after logging in to the MRS management console.

**Table  2**  Job status

<a name="table792216529274"></a>
<table><thead align="left"><tr id="row18923105282716"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.3.1.1"><p id="p1576571162457"><a name="p1576571162457"></a><a name="p1576571162457"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="81%" id="mcps1.2.3.1.2"><p id="p60593435162457"><a name="p60593435162457"></a><a name="p60593435162457"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16924252202713"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.3.1.1 "><p id="p44376580102832"><a name="p44376580102832"></a><a name="p44376580102832"></a>Running</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.2.3.1.2 "><p id="p37733260102832"><a name="p37733260102832"></a><a name="p37733260102832"></a>A job is being executed.</p>
</td>
</tr>
<tr id="row8924852112720"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.3.1.1 "><p id="p60021381102832"><a name="p60021381102832"></a><a name="p60021381102832"></a>Completed</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.2.3.1.2 "><p id="p29893721102832"><a name="p29893721102832"></a><a name="p29893721102832"></a>Job execution is complete and successful.</p>
</td>
</tr>
<tr id="row992465202717"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.3.1.1 "><p id="p49251038102832"><a name="p49251038102832"></a><a name="p49251038102832"></a>Terminated</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.2.3.1.2 "><p id="p29911176102832"><a name="p29911176102832"></a><a name="p29911176102832"></a>A job is stopped during execution.</p>
</td>
</tr>
<tr id="row15925952132720"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.3.1.1 "><p id="p61975973102832"><a name="p61975973102832"></a><a name="p61975973102832"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="81%" headers="mcps1.2.3.1.2 "><p id="p53997887102832"><a name="p53997887102832"></a><a name="p53997887102832"></a>An error occurs during job execution or job execution fails.</p>
</td>
</tr>
</tbody>
</table>

