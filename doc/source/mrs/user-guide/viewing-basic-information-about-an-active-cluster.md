# Viewing Basic Information About an Active Cluster<a name="EN-US_TOPIC_0125375341"></a>

After clusters are created, you can monitor and manage clusters. Choose  **Clusters \> Active Clusters**. Select a cluster and click its name to switch to the cluster details page. Click **Cluster Details**  to view information about a cluster such as the configurations, deployed nodes, and other basic information.

[Table 1](#table65852771163242), [Table 2](#table52580381164149), [Table 3](#table5392696116422), [Table 4](#table2714878316527), [Table 5](#table19851621164055), and [Table 6](#table14995478145753)  describe the information about cluster configurations and nodes, respectively.

**Table  1**  Cluster configuration information

<a name="table65852771163242"></a>
<table><thead align="left"><tr id="row60125107163242"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p38295527163242"><a name="p38295527163242"></a><a name="p38295527163242"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p14929983163242"><a name="p14929983163242"></a><a name="p14929983163242"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1369124163242"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p13392698163343"><a name="p13392698163343"></a><a name="p13392698163343"></a>Cluster Name</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p11066735163343"><a name="p11066735163343"></a><a name="p11066735163343"></a>Cluster name</p>
<p id="p32491757163343"><a name="p32491757163343"></a><a name="p32491757163343"></a>This parameter is set when a cluster is created.</p>
</td>
</tr>
<tr id="row14491309163242"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p47295640163452"><a name="p47295640163452"></a><a name="p47295640163452"></a>Cluster Status</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5741617163452"><a name="p5741617163452"></a><a name="p5741617163452"></a>Status of a cluster</p>
</td>
</tr>
<tr id="row907670163328"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p8169031163328"><a name="p8169031163328"></a><a name="p8169031163328"></a>Cluster Manager</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p57720953163618"><a name="p57720953163618"></a><a name="p57720953163618"></a>Click <span class="uicontrol" id="uicontrol4400013163636"><a name="uicontrol4400013163636"></a><a name="uicontrol4400013163636"></a><b>View</b></span>&nbsp;to open the&nbsp;<span class="wintitle" id="wintitle49772886163826"><a name="wintitle49772886163826"></a><a name="wintitle49772886163826"></a><b>Cluster Manager</b></span> page.</p>
</td>
</tr>
<tr id="row63990726163242"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p15866338163242"><a name="p15866338163242"></a><a name="p15866338163242"></a>Cluster Details</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1317545163618"><a name="p1317545163618"></a><a name="p1317545163618"></a>Cluster details include basic information, node information, and component information. You can click <strong id="b135121235133016"><a name="b135121235133016"></a><a name="b135121235133016"></a>Cluster Details</strong> to hide information.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Basic information

<a name="table52580381164149"></a>
<table><thead align="left"><tr id="row44688168164149"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p62971847164149"><a name="p62971847164149"></a><a name="p62971847164149"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p446007164149"><a name="p446007164149"></a><a name="p446007164149"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23751746164149"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p44843255164149"><a name="p44843255164149"></a><a name="p44843255164149"></a>Cluster Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p8425053164149"><a name="p8425053164149"></a><a name="p8425053164149"></a>MRS version</p>
<p id="p18377143111717"><a name="p18377143111717"></a><a name="p18377143111717"></a>Currently, MRS 1.6.3, MRS 1.7.2, MRS 1.9.2 and MRS 2.1.0 are supported.</p>
<p id="p60741887164149"><a name="p60741887164149"></a><a name="p60741887164149"></a>This parameter is set when a cluster is created.</p>
</td>
</tr>
<tr id="row9806075164149"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p56094612164149"><a name="p56094612164149"></a><a name="p56094612164149"></a>Cluster Type</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><div class="p" id="p47369758164149"><a name="p47369758164149"></a><a name="p47369758164149"></a>MRS provides three types of clusters:<a name="ul27443787164149"></a><a name="ul27443787164149"></a><ul id="ul27443787164149"><li>Analysis cluster: is used for offline data analysis and provides Hadoop components.</li><li>Streaming cluster: is used for streaming tasks and provides stream processing components.</li><li>Hybrid cluster: is used for both offline data analysis and streaming processing and provides Hadoop components and streaming processing components. (MRS 1.9.2 or later supports hybrid clusters.)</li></ul>
</div>
<p id="p50466426164149"><a name="p50466426164149"></a><a name="p50466426164149"></a>This parameter is set when a cluster is created.</p>
</td>
</tr>
<tr id="row1794183164229"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p63572563164238"><a name="p63572563164238"></a><a name="p63572563164238"></a>Cluster ID</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p49103999164238"><a name="p49103999164238"></a><a name="p49103999164238"></a>Unique identifier of a cluster</p>
<p id="p39282815164238"><a name="p39282815164238"></a><a name="p39282815164238"></a>This parameter is automatically assigned when a cluster is created.</p>
</td>
</tr>
<tr id="row13813375164257"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4027242016439"><a name="p4027242016439"></a><a name="p4027242016439"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4084061716439"><a name="p4084061716439"></a><a name="p4084061716439"></a>Time when MRS starts charging MRS clusters of the customer</p>
</td>
</tr>
<tr id="row51544658164149"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p14367744164149"><a name="p14367744164149"></a><a name="p14367744164149"></a>AZ</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p22936582164149"><a name="p22936582164149"></a><a name="p22936582164149"></a>An availability zone of the working zone in the cluster</p>
<p id="p5102650164149"><a name="p5102650164149"></a><a name="p5102650164149"></a>This parameter is set when a cluster is created.</p>
</td>
</tr>
<tr id="row45923853164149"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p28844604164149"><a name="p28844604164149"></a><a name="p28844604164149"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p54711612164149"><a name="p54711612164149"></a><a name="p54711612164149"></a>VPC information</p>
<p id="p22642466164149"><a name="p22642466164149"></a><a name="p22642466164149"></a>This parameter is set when a cluster is created.</p>
<p id="p2455605164149"><a name="p2455605164149"></a><a name="p2455605164149"></a>A VPC is a secure, isolated, and logical network environment.</p>
</td>
</tr>
<tr id="row22100446164149"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p45305662164149"><a name="p45305662164149"></a><a name="p45305662164149"></a>Subnet</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p45879978164149"><a name="p45879978164149"></a><a name="p45879978164149"></a>Subnet information</p>
<p id="p10266625164149"><a name="p10266625164149"></a><a name="p10266625164149"></a>This parameter is set when a cluster is created.</p>
<p id="p25290763164149"><a name="p25290763164149"></a><a name="p25290763164149"></a>A subnet provides dedicated network resources that are isolated from other networks, improving network security.</p>
</td>
</tr>
<tr id="row2402562517720"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2936809817724"><a name="p2936809817724"></a><a name="p2936809817724"></a>Cluster Manager IP Address</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3000577017724"><a name="p3000577017724"></a><a name="p3000577017724"></a>Floating IP address for accessing MRS Manager.</p>
<div class="note" id="note3513746921533"><a name="note3513746921533"></a><a name="note3513746921533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul0345195585611"></a><a name="ul0345195585611"></a><ul id="ul0345195585611"><li>This parameter is displayed only after Kerberos authentication is enabled. The cluster manager IP address is displayed on the basic information page of the cluster with Kerberos authentication enabled instead of the cluster with Kerberos authentication disabled.</li><li>This parameter is valid only in versions earlier than MRS 1.9.2.</li></ul>
</div></div>
</td>
</tr>
<tr id="row13802276817"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p934412373610"><a name="p934412373610"></a><a name="p934412373610"></a>EIP</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1896163715354"><a name="p1896163715354"></a><a name="p1896163715354"></a>After binding an EIP to an MRS cluster, you can use the EIP to access the <strong id="b95237561193"><a name="b95237561193"></a><a name="b95237561193"></a>MRS Manager</strong> page of the cluster.</p>
<div class="note" id="note355320459352"><a name="note355320459352"></a><a name="note355320459352"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10572204543515"><a name="p10572204543515"></a><a name="p10572204543515"></a>This parameter is valid only in MRS 1.9.2 or later.</p>
</div></div>
</td>
</tr>
<tr id="row34741516164337"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p39051468164443"><a name="p39051468164443"></a><a name="p39051468164443"></a>Key Pair</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p9052321164443"><a name="p9052321164443"></a><a name="p9052321164443"></a>Key pair name</p>
<p id="p14362031164443"><a name="p14362031164443"></a><a name="p14362031164443"></a>This parameter is set when a cluster is created.</p>
</td>
</tr>
<tr id="row43641542186"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p18144944134315"><a name="p18144944134315"></a><a name="p18144944134315"></a>Kerberos Authentication</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p10145744134315"><a name="p10145744134315"></a><a name="p10145744134315"></a>Whether to enable Kerberos authentication when logging in to MRS Manager.</p>
</td>
</tr>
<tr id="row18691942287"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3145204414313"><a name="p3145204414313"></a><a name="p3145204414313"></a>Logging</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p114574411437"><a name="p114574411437"></a><a name="p114574411437"></a>Whether the tenant has enabled the log collection function.</p>
</td>
</tr>
<tr id="row2957134216815"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p114731314500"><a name="p114731314500"></a><a name="p114731314500"></a><span id="ph885418135500"><a name="ph885418135500"></a><a name="ph885418135500"></a></span>Security Group</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p84735315016"><a name="p84735315016"></a><a name="p84735315016"></a><span id="ph19712125875119"><a name="ph19712125875119"></a><a name="ph19712125875119"></a>Security group name of the cluster</span></p>
</td>
</tr>
<tr id="row1128719435810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1914564494313"><a name="p1914564494313"></a><a name="p1914564494313"></a>Streaming Core Node LVM</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p8145204434319"><a name="p8145204434319"></a><a name="p8145204434319"></a>Indicates whether to enable the Logical Volume Manager (LVM) function of streaming Core nodes.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Node information

<a name="table5392696116422"></a>
<table><thead align="left"><tr id="row2393301016422"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p5952566216422"><a name="p5952566216422"></a><a name="p5952566216422"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p5684931416422"><a name="p5684931416422"></a><a name="p5684931416422"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row869735716422"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3339728616422"><a name="p3339728616422"></a><a name="p3339728616422"></a>Master Node</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2082560716422"><a name="p2082560716422"></a><a name="p2082560716422"></a>Information about the Master node</p>
<p id="p5321273816422"><a name="p5321273816422"></a><a name="p5321273816422"></a>Format: [instance specification | node quantity]</p>
</td>
</tr>
<tr id="row915260116422"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p316320316422"><a name="p316320316422"></a><a name="p316320316422"></a>Core Node</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5489291016422"><a name="p5489291016422"></a><a name="p5489291016422"></a>Information about a Core node</p>
<p id="p2427414716422"><a name="p2427414716422"></a><a name="p2427414716422"></a>Format: [instance specification | node quantity]</p>
</td>
</tr>
<tr id="row33016177162853"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p707311162859"><a name="p707311162859"></a><a name="p707311162859"></a>Task Node</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p57292265162859"><a name="p57292265162859"></a><a name="p57292265162859"></a>Information about a Task node</p>
<p id="p45868344162859"><a name="p45868344162859"></a><a name="p45868344162859"></a>Format: [instance specification | node quantity]</p>
</td>
</tr>
<tr id="row1714073816422"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4622250116422"><a name="p4622250116422"></a><a name="p4622250116422"></a>Active Master Node IP Address</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5303513816422"><a name="p5303513816422"></a><a name="p5303513816422"></a>IP address of the active Master node in a cluster, which is also the IP address of the active management node of MRS Manager.</p>
</td>
</tr>
<tr id="row58388109162847"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p55730934162847"><a name="p55730934162847"></a><a name="p55730934162847"></a>Task Node Auto Scaling</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4899373717954"><a name="p4899373717954"></a><a name="p4899373717954"></a>Auto Scaling can automatically adjust computing resources based on customers' service requirements and preset policies. With auto scaling, the number of instances in MRS tasks can increase and decrease as the service load increases and decreases, ensuring smooth operation of services.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Component information

<a name="table2714878316527"></a>
<table><thead align="left"><tr id="row4043090716527"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p5367805916527"><a name="p5367805916527"></a><a name="p5367805916527"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p5295554016527"><a name="p5295554016527"></a><a name="p5295554016527"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3941823316527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3876027116527"><a name="p3876027116527"></a><a name="p3876027116527"></a>Hadoop Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5257424616527"><a name="p5257424616527"></a><a name="p5257424616527"></a>Hadoop version</p>
</td>
</tr>
<tr id="row340616916527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p746427616527"><a name="p746427616527"></a><a name="p746427616527"></a>Spark Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p62659516527"><a name="p62659516527"></a><a name="p62659516527"></a>Spark version</p>
<p id="p563935816527"><a name="p563935816527"></a><a name="p563935816527"></a>Only a Spark cluster displays this version. Because Spark and Hive must be used together, Spark and Hive versions are displayed at the same time.</p>
</td>
</tr>
<tr id="row5075422316527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1745135916527"><a name="p1745135916527"></a><a name="p1745135916527"></a>HBase Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p427394716527"><a name="p427394716527"></a><a name="p427394716527"></a>HBase version</p>
<p id="p3846553016527"><a name="p3846553016527"></a><a name="p3846553016527"></a>Only an HBase cluster displays this version.</p>
</td>
</tr>
<tr id="row1064545216527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p5697532216527"><a name="p5697532216527"></a><a name="p5697532216527"></a>Hive Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5159838016527"><a name="p5159838016527"></a><a name="p5159838016527"></a>Hive version</p>
<p id="p6173224316527"><a name="p6173224316527"></a><a name="p6173224316527"></a>Only a Hive cluster displays this version.</p>
</td>
</tr>
<tr id="row1871927516527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3986630216527"><a name="p3986630216527"></a><a name="p3986630216527"></a>Hue Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p794503816527"><a name="p794503816527"></a><a name="p794503816527"></a>Hue version</p>
</td>
</tr>
<tr id="row3067736816527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p183885716527"><a name="p183885716527"></a><a name="p183885716527"></a>Loader Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1472976016527"><a name="p1472976016527"></a><a name="p1472976016527"></a>Loader Version</p>
<p id="p6545897616527"><a name="p6545897616527"></a><a name="p6545897616527"></a>This parameter is displayed when the MRS version is <span id="text26244364172035"><a name="text26244364172035"></a><a name="text26244364172035"></a>MRS 1.5.0</span> or later.</p>
</td>
</tr>
<tr id="row4672276016527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2644722516527"><a name="p2644722516527"></a><a name="p2644722516527"></a>Kafka Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p6185048216527"><a name="p6185048216527"></a><a name="p6185048216527"></a>Kafka Version</p>
<p id="p1978343416527"><a name="p1978343416527"></a><a name="p1978343416527"></a>Only a Kafka cluster displays this version.</p>
</td>
</tr>
<tr id="row4383318016527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6082671916527"><a name="p6082671916527"></a><a name="p6082671916527"></a>Storm Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2801718616527"><a name="p2801718616527"></a><a name="p2801718616527"></a>Storm Version</p>
<p id="p5082808316527"><a name="p5082808316527"></a><a name="p5082808316527"></a>Only a Storm cluster displays this version.</p>
</td>
</tr>
<tr id="row5479956516527"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p957978516527"><a name="p957978516527"></a><a name="p957978516527"></a>Flume Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3776511716527"><a name="p3776511716527"></a><a name="p3776511716527"></a>Flume Version</p>
</td>
</tr>
<tr id="row144271172519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6565144412512"><a name="p6565144412512"></a><a name="p6565144412512"></a>Tez Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1956584416258"><a name="p1956584416258"></a><a name="p1956584416258"></a>Tez version.</p>
</td>
</tr>
<tr id="row7783121115253"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p193271731155110"><a name="p193271731155110"></a><a name="p193271731155110"></a>Presto Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1432753114518"><a name="p1432753114518"></a><a name="p1432753114518"></a>Presto version.</p>
</td>
</tr>
<tr id="row171002012142512"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p35281049115111"><a name="p35281049115111"></a><a name="p35281049115111"></a>KafkaManager Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p75288497518"><a name="p75288497518"></a><a name="p75288497518"></a>KafkaManager version.</p>
</td>
</tr>
<tr id="row14665131212251"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p14673351102719"><a name="p14673351102719"></a><a name="p14673351102719"></a>Opentsdb Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p14673205162712"><a name="p14673205162712"></a><a name="p14673205162712"></a>Opentsdb version.</p>
</td>
</tr>
<tr id="row744943616371"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1286103453619"><a name="p1286103453619"></a><a name="p1286103453619"></a>Flink Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p32511559174414"><a name="p32511559174414"></a><a name="p32511559174414"></a>Flink version.</p>
</td>
</tr>
<tr id="row66683614362"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p8668206103617"><a name="p8668206103617"></a><a name="p8668206103617"></a>Alluxio Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p9658124073619"><a name="p9658124073619"></a><a name="p9658124073619"></a>Alluxio version.</p>
</td>
</tr>
<tr id="row3178578360"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p181786718366"><a name="p181786718366"></a><a name="p181786718366"></a>Ranger  Version</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p196583407362"><a name="p196583407362"></a><a name="p196583407362"></a>Ranger  version.</p>
</td>
</tr>
<tr id="row8437594165255"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3805334016535"><a name="p3805334016535"></a><a name="p3805334016535"></a>Kerberos Authentication</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p6242168516535"><a name="p6242168516535"></a><a name="p6242168516535"></a>Indicates whether to enable Kerberos authentication when logging in to MRS Manager.</p>
</td>
</tr>
<tr id="row4281054316532"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p559891616535"><a name="p559891616535"></a><a name="p559891616535"></a>Logging</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5085902316535"><a name="p5085902316535"></a><a name="p5085902316535"></a>Indicates whether the tenant has enabled the log collection function.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Node description

<a name="table19851621164055"></a>
<table><thead align="left"><tr id="row49442205164055"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p45395657164055"><a name="p45395657164055"></a><a name="p45395657164055"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p53169561164055"><a name="p53169561164055"></a><a name="p53169561164055"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43838921164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p61291706164055"><a name="p61291706164055"></a><a name="p61291706164055"></a>Resize Cluster</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p65681119164055"><a name="p65681119164055"></a><a name="p65681119164055"></a>For details about adding or deleting a Core/Task node to a cluster, see <a href="expanding-a-cluster.md">Expanding a Cluster</a>&nbsp;or&nbsp;<a href="shrinking-a-cluster.md">Shrinking a Cluster</a>. This applies to MRS 1.6.3 or later.</p>
<p id="p55234618153230"><a name="p55234618153230"></a><a name="p55234618153230"></a><span class="uicontrol" id="uicontrol3245292153243"><a name="uicontrol3245292153243"></a><a name="uicontrol3245292153243"></a><b>Resize Cluster</b></span> is unavailable and capacity expansion or reduction is not allowed in any of the following situations:</p>
<a name="ul938939115335"></a><a name="ul938939115335"></a><ul id="ul938939115335"><li>The cluster is not in the running state.</li><li>The number of Core nodes or Task nodes exceeds the maximum value (<span id="ph157322409368"><a name="ph157322409368"></a><a name="ph157322409368"></a>5</span>00).</li><li>The cluster charging mode is not on-demand.</li></ul>
</td>
</tr>
<tr id="row4968400893458"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p119914099355"><a name="p119914099355"></a><a name="p119914099355"></a>Add Node</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p19164660141614"><a name="p19164660141614"></a><a name="p19164660141614"></a>For details about adding or deleting a Core node to a cluster, see <a href="expanding-a-cluster.md">Expanding a Cluster</a>. This applies to MRS 1.6.3 or earlier.</p>
<p id="p670877369355"><a name="p670877369355"></a><a name="p670877369355"></a><span class="uicontrol" id="uicontrol669187199355"><a name="uicontrol669187199355"></a><a name="uicontrol669187199355"></a><b>Add Node</b></span> is unavailable and capacity expansion is not allowed in any of the following situations:</p>
<a name="ul627111279355"></a><a name="ul627111279355"></a><ul id="ul627111279355"><li>The cluster is not in the running state.</li><li>The number of Core nodes exceeds the maximum value (100).</li><li>The cluster charging mode is not on-demand.</li></ul>
</td>
</tr>
<tr id="row18570400164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p27807463164055"><a name="p27807463164055"></a><a name="p27807463164055"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p37811993164055"><a name="p37811993164055"></a><a name="p37811993164055"></a>Name of a cluster node</p>
</td>
</tr>
<tr id="row4281235123111"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2116648131016"><a name="p2116648131016"></a><a name="p2116648131016"></a>Scale Up Master Node Specifications</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p31161048181014"><a name="p31161048181014"></a><a name="p31161048181014"></a>For details about how to scale up the Master node specifications, see <a href="scaling-up-master-node-specifications.md">Scaling Up Master Node Specifications</a>.</p>
</td>
</tr>
<tr id="row7229105171249"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p65061946171249"><a name="p65061946171249"></a><a name="p65061946171249"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p35526268171249"><a name="p35526268171249"></a><a name="p35526268171249"></a>Status of a cluster</p>
</td>
</tr>
<tr id="row4763623164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p50309159164055"><a name="p50309159164055"></a><a name="p50309159164055"></a>Type</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p48510088164055"><a name="p48510088164055"></a><a name="p48510088164055"></a>Node type</p>
<a name="ul33937612164055"></a><a name="ul33937612164055"></a><ul id="ul33937612164055"><li>Master<p id="p5294591091134"><a name="p5294591091134"></a><a name="p5294591091134"></a>A Master node in an MRS cluster manages the cluster, assigns MapReduce executable files to Core nodes, traces the execution status of each job, and monitors DataNode running status.</p>
</li><li>Core<p id="p2662450891142"><a name="p2662450891142"></a><a name="p2662450891142"></a>A Core node in a cluster processes data and stores processed data in HDFS.</p>
</li><li>Task<p id="p784710470218"><a name="p784710470218"></a><a name="p784710470218"></a>A Task node in a cluster is used for computing and does not store persistent data. Task nodes are optional, and the number of Task nodes can be zero. When the data volume change is small in a cluster but the cluster's service processing capabilities need to be remarkably and temporarily improved, add Task nodes. Task nodes can be used to reduce costs and facilitate cluster node scaling, flexibly meeting users' requirements for increasing or decreasing cluster computing capabilities. (Task nodes are supported by MRS 1.6.3 or later.)</p>
</li></ul>
</td>
</tr>
<tr id="row44457675164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p44301950164055"><a name="p44301950164055"></a><a name="p44301950164055"></a>IP Address</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p31688177164055"><a name="p31688177164055"></a><a name="p31688177164055"></a>IP address of a cluster node</p>
</td>
</tr>
<tr id="row16758138164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p15231920164055"><a name="p15231920164055"></a><a name="p15231920164055"></a>Configuration</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p96768599175"><a name="p96768599175"></a><a name="p96768599175"></a>Instance specifications of a node</p>
<p id="p25826044164055"><a name="p25826044164055"></a><a name="p25826044164055"></a>This parameter is determined by the CPU, memory, and disks used.</p>
<div class="note" id="note31107804164055"><a name="note31107804164055"></a><a name="note31107804164055"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11534787164055"><a name="p11534787164055"></a><a name="p11534787164055"></a>More advanced instance specifications allow better data processing.</p>
</div></div>
</td>
</tr>
<tr id="row36704225164055"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p20252271164055"><a name="p20252271164055"></a><a name="p20252271164055"></a>Default Security Group</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p29821229164055"><a name="p29821229164055"></a><a name="p29821229164055"></a>Security group name for master and Core/Task nodes, which are automatically assigned when a cluster is created.</p>
<p id="p67064469164055"><a name="p67064469164055"></a><a name="p67064469164055"></a>This is the default security group. Do not modify or delete the security group because modifying or deleting it will cause a cluster exception.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Button description

<a name="table14995478145753"></a>
<table><thead align="left"><tr id="row34648328145753"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p25698260145753"><a name="p25698260145753"></a><a name="p25698260145753"></a>Button</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p1184341145753"><a name="p1184341145753"></a><a name="p1184341145753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10659077145753"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p31390333102326"><a name="p31390333102326"></a><a name="p31390333102326"></a><a name="image21167408145618"></a><a name="image21167408145618"></a><span><img id="image21167408145618" src="figures/icon_mrs_fresh_r.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p66539681102326"><a name="p66539681102326"></a><a name="p66539681102326"></a>Click <a name="image20461066145633"></a><a name="image20461066145633"></a><span><img id="image20461066145633" src="figures/icon_mrs_fresh_r.png"></span> to manually refresh the node.</p>
</td>
</tr>
</tbody>
</table>

