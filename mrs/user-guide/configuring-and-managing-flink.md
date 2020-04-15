# Configuring and Managing Flink<a name="EN-US_TOPIC_0221415089"></a>

## Configuring Parameter Paths<a name="section4819172518615"></a>

All parameters of Flink must be set on a client. The path of a configuration file is as follows:  _Client installation path_**/Flink/flink/conf/flink-conf.yaml**

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   You are advised to modify the  **flink-conf.yaml**  configuration file on the client to configure parameters. The configuration format of the YAML file is  **key: value**.  
>    Example:  **taskmanager.heap.mb: 512**  
>    Note that a space is required between  **key:**  and  **value**.  
>-   If you modify parameter configuration in  **Service Configuration**  on MRS Manager, the client must be downloaded and installed again after the modification.   

## Configuring the JobManager and TaskManager<a name="section4452655171416"></a>

The JobManager and TaskManager are main components of Flink. You can set related parameters on the client based on various security and performance scenarios.

The main configuration items include the communication ports, memory management, and connection retry.

**Table  1**  Parameter description

<a name="table91792019191713"></a>
<table><thead align="left"><tr id="row91791919191719"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5179111941713"><a name="p5179111941713"></a><a name="p5179111941713"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p101796192178"><a name="p101796192178"></a><a name="p101796192178"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p13179111951711"><a name="p13179111951711"></a><a name="p13179111951711"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p61791419191711"><a name="p61791419191711"></a><a name="p61791419191711"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18179121931710"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p27068241192"><a name="p27068241192"></a><a name="p27068241192"></a>taskmanager.rpc.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p14805194821916"><a name="p14805194821916"></a><a name="p14805194821916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p7931104141917"><a name="p7931104141917"></a><a name="p7931104141917"></a>32326-32390</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p191319325196"><a name="p191319325196"></a><a name="p191319325196"></a>Akka system listening port on the TaskManager</p>
</td>
</tr>
<tr id="row1318010197178"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12707152413197"><a name="p12707152413197"></a><a name="p12707152413197"></a>taskmanager.data.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p08051848141916"><a name="p08051848141916"></a><a name="p08051848141916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p6932124114198"><a name="p6932124114198"></a><a name="p6932124114198"></a>32391-32455</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1013183214194"><a name="p1013183214194"></a><a name="p1013183214194"></a>NettyServer listening port used for data exchange operations between TaskManagers</p>
</td>
</tr>
<tr id="row1518091921713"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4707324151912"><a name="p4707324151912"></a><a name="p4707324151912"></a>taskmanager.data.ssl.enabled</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p168057488199"><a name="p168057488199"></a><a name="p168057488199"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p793215413197"><a name="p793215413197"></a><a name="p793215413197"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p15131432131912"><a name="p15131432131912"></a><a name="p15131432131912"></a>SSL flag for data communication between TaskManagers. This is applicable only when the global ssl flag <strong id="b1461263522716"><a name="b1461263522716"></a><a name="b1461263522716"></a>security.ssl</strong> is enabled.</p>
</td>
</tr>
<tr id="row1573125391914"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p183181422014"><a name="p183181422014"></a><a name="p183181422014"></a>taskmanager.numberOfTaskSlots</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1435613268202"><a name="p1435613268202"></a><a name="p1435613268202"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13588161916209"><a name="p13588161916209"></a><a name="p13588161916209"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1642051219208"><a name="p1642051219208"></a><a name="p1642051219208"></a>Number of slots occupied by the TaskManager. Generally, the value is configured as the number of physical CPU cores. In <strong id="b1234842143114"><a name="b1234842143114"></a><a name="b1234842143114"></a>yarn-session</strong> mode, the value can be transmitted by the <strong id="b161511211163113"><a name="b161511211163113"></a><a name="b161511211163113"></a>-s</strong> parameter only. In <strong id="b189181824143113"><a name="b189181824143113"></a><a name="b189181824143113"></a>yarn-cluster</strong> mode, the value can be transmitted by the <strong id="b79549308312"><a name="b79549308312"></a><a name="b79549308312"></a>-ys</strong> parameter only.</p>
</td>
</tr>
<tr id="row989714536194"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4402174222019"><a name="p4402174222019"></a><a name="p4402174222019"></a>parallelism.default</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p192878302119"><a name="p192878302119"></a><a name="p192878302119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1296485510203"><a name="p1296485510203"></a><a name="p1296485510203"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1658184920204"><a name="p1658184920204"></a><a name="p1658184920204"></a>Number of concurrent job operators</p>
</td>
</tr>
<tr id="row642515491913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12402142162018"><a name="p12402142162018"></a><a name="p12402142162018"></a>taskmanager.memory.size</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p14287139218"><a name="p14287139218"></a><a name="p14287139218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p7964205582016"><a name="p7964205582016"></a><a name="p7964205582016"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p14581204917204"><a name="p14581204917204"></a><a name="p14581204917204"></a>Amount of memory that the TaskManager reserves on the JVM's heap space for sorting, hash tables, and caching of intermediate results. If unspecified, the memory manager will take a fixed ratio of the heap memory available to the JVM, as specified by <strong id="b425332911371"><a name="b425332911371"></a><a name="b425332911371"></a>taskmanager.memory.fraction</strong>. The unit is MB.</p>
</td>
</tr>
<tr id="row058545431917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11402114211204"><a name="p11402114211204"></a><a name="p11402114211204"></a>taskmanager.memory.fraction</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p328716372110"><a name="p328716372110"></a><a name="p328716372110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p14964755192019"><a name="p14964755192019"></a><a name="p14964755192019"></a>0.7</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17581134915204"><a name="p17581134915204"></a><a name="p17581134915204"></a>Ratio of JVM heap memory that the TaskManager reserves for sorting, hash tables, and caching of intermediate results.</p>
</td>
</tr>
<tr id="row1291515543199"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p340284282015"><a name="p340284282015"></a><a name="p340284282015"></a>taskmanager.memory.off-heap</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p228719313215"><a name="p228719313215"></a><a name="p228719313215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p11964955192012"><a name="p11964955192012"></a><a name="p11964955192012"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5581104992012"><a name="p5581104992012"></a><a name="p5581104992012"></a>Whether the TaskManager uses off-heap memory, which is used for sorting, hash tables, and caching of intermediate results. You are advised to enable this configuration item for large memory to improve memory operation efficiency.</p>
</td>
</tr>
<tr id="row11180119121715"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1248825152110"><a name="p1248825152110"></a><a name="p1248825152110"></a>taskmanager.memory.segment-size</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p467918434213"><a name="p467918434213"></a><a name="p467918434213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p8544123719210"><a name="p8544123719210"></a><a name="p8544123719210"></a>32768</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p128293116218"><a name="p128293116218"></a><a name="p128293116218"></a>Size of memory segments on the TaskManager. Memory segment is the basic unit of the reserved memory space and is used to configure a network buffer stack. The unit is bytes.</p>
</td>
</tr>
<tr id="row126421921102118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5481825162119"><a name="p5481825162119"></a><a name="p5481825162119"></a>taskmanager.memory.preallocate</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1567924314215"><a name="p1567924314215"></a><a name="p1567924314215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p7544537122117"><a name="p7544537122117"></a><a name="p7544537122117"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p7282173110219"><a name="p7282173110219"></a><a name="p7282173110219"></a>Whether TaskManagers should allocate all reserved memory when starting up. When off-heap memory is used, it is recommended that this configuration item be enabled. </p>
</td>
</tr>
<tr id="row6418222102114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p310114802216"><a name="p310114802216"></a><a name="p310114802216"></a>taskmanager.registration.initial-backoff</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p157412562211"><a name="p157412562211"></a><a name="p157412562211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p640731912215"><a name="p640731912215"></a><a name="p640731912215"></a>500 ms</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5189101462212"><a name="p5189101462212"></a><a name="p5189101462212"></a>Initial registration backoff between two consecutive registration attempts. The unit is ms/s/m/h/d.</p>
<div class="note" id="note397143972210"><a name="note397143972210"></a><a name="note397143972210"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p3971939202218"><a name="p3971939202218"></a><a name="p3971939202218"></a>There is a single-byte space between the value and the unit. <strong id="b7280104503319"><a name="b7280104503319"></a><a name="b7280104503319"></a>ms/s/m/h/d</strong> indicates millisecond, second, minute, hour, day, respectively.</p>
</div></div>
</td>
</tr>
<tr id="row1160062212111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11021185225"><a name="p11021185225"></a><a name="p11021185225"></a>taskmanager.registration.refused-backoff</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p574182582218"><a name="p574182582218"></a><a name="p574182582218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p540711198226"><a name="p540711198226"></a><a name="p540711198226"></a>5 min</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p18190614172219"><a name="p18190614172219"></a><a name="p18190614172219"></a>Backoff after a registration has been refused by the JobManager before retrying to connect.</p>
</td>
</tr>
<tr id="row7534193714615"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p65352371662"><a name="p65352371662"></a><a name="p65352371662"></a>task.cancellation.interval</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1553514371964"><a name="p1553514371964"></a><a name="p1553514371964"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1535537569"><a name="p1535537569"></a><a name="p1535537569"></a>30000</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p953513715610"><a name="p953513715610"></a><a name="p953513715610"></a>Time interval between two successive task cancellation attempts in milliseconds.</p>
</td>
</tr>
</tbody>
</table>

## Configuring the BLOB<a name="section193756481261"></a>

A BLOB server on a JobManager node is used to receive JAR files uploaded from a client, send JAR files to the TaskManager, or upload logs. Flink provides configuration items about the BLOB server in the  **flink-conf.yaml**  file.

You can configure configuration items, such as the port, SSL, retry times, and concurrency.

**Table  2**  Parameter description

<a name="table199651434182719"></a>
<table><thead align="left"><tr id="row796693412712"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p119661134122720"><a name="p119661134122720"></a><a name="p119661134122720"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p7966183413275"><a name="p7966183413275"></a><a name="p7966183413275"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p18966173412273"><a name="p18966173412273"></a><a name="p18966173412273"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p1196663412279"><a name="p1196663412279"></a><a name="p1196663412279"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6966143452716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p116661421152811"><a name="p116661421152811"></a><a name="p116661421152811"></a>blob.server.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2082059182911"><a name="p2082059182911"></a><a name="p2082059182911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p113171527202911"><a name="p113171527202911"></a><a name="p113171527202911"></a>32456-32520</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p14706136142911"><a name="p14706136142911"></a><a name="p14706136142911"></a>BLOB server port</p>
</td>
</tr>
<tr id="row35761553284"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1866692118284"><a name="p1866692118284"></a><a name="p1866692118284"></a>blob.service.ssl.enabled</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p482012922915"><a name="p482012922915"></a><a name="p482012922915"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p143171271294"><a name="p143171271294"></a><a name="p143171271294"></a>true</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p18706136132916"><a name="p18706136132916"></a><a name="p18706136132916"></a>SSL flag for BLOB service client/server communication. This is applicable only when the global ssl flag <strong id="b113043569296"><a name="b113043569296"></a><a name="b113043569296"></a>security.ssl</strong> is enabled.</p>
</td>
</tr>
<tr id="row1114169281"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p146661221202816"><a name="p146661221202816"></a><a name="p146661221202816"></a>blob.fetch.retries</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1582016992917"><a name="p1582016992917"></a><a name="p1582016992917"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p131732752919"><a name="p131732752919"></a><a name="p131732752919"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p20707336162915"><a name="p20707336162915"></a><a name="p20707336162915"></a>Number of retries for the TaskManager to download BLOB files from the JobManager</p>
</td>
</tr>
<tr id="row12966123411274"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p266612215289"><a name="p266612215289"></a><a name="p266612215289"></a>blob.fetch.num-concurrent</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p582018914290"><a name="p582018914290"></a><a name="p582018914290"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p431720275295"><a name="p431720275295"></a><a name="p431720275295"></a>50</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p10707036142919"><a name="p10707036142919"></a><a name="p10707036142919"></a>Maximum number of concurrent BLOB fetches that the JobManager serves</p>
</td>
</tr>
<tr id="row596633462714"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p513913132919"><a name="p513913132919"></a><a name="p513913132919"></a>blob.fetch.backlog</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p351191682915"><a name="p351191682915"></a><a name="p351191682915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p855072072910"><a name="p855072072910"></a><a name="p855072072910"></a>1000</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p09461442112917"><a name="p09461442112917"></a><a name="p09461442112917"></a>Maximum number of queued BLOB fetches (such as JAR file downloads) that the JobManager allows </p>
</td>
</tr>
</tbody>
</table>

## Configuring the Distributed Coordination \(via Akka\)<a name="section10197757112916"></a>

The Akka actor model is the basis of communications between a Flink client and JobManager, JobManager and TaskManager, as well as TaskManagers. Flink enables you to configure the Akka connection parameters in the  **flink-conf.yaml**  file based on the network environment or optimization policy.

The configuration items include the timeout settings of frame sending and waiting, and the configuration of the Akka listening mechanism Deathwatch.

**Table  3**  Parameter description

<a name="table8198157172919"></a>
<table><thead align="left"><tr id="row12198757192914"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p9198145720293"><a name="p9198145720293"></a><a name="p9198145720293"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p51981857102912"><a name="p51981857102912"></a><a name="p51981857102912"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p12198557152912"><a name="p12198557152912"></a><a name="p12198557152912"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p11981957142915"><a name="p11981957142915"></a><a name="p11981957142915"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1198115762915"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62145455513"><a name="p62145455513"></a><a name="p62145455513"></a>akka.ask.timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p13197987564"><a name="p13197987564"></a><a name="p13197987564"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5121164135617"><a name="p5121164135617"></a><a name="p5121164135617"></a>10s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p485535814552"><a name="p485535814552"></a><a name="p485535814552"></a>Timeout used for all futures and blocking Akka calls. If Flink fails due to timeouts then you should try to increase this value. Timeouts can be caused by slow machines or a congested network. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row1719985762912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p112554125512"><a name="p112554125512"></a><a name="p112554125512"></a>akka.lookup.timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p81983835613"><a name="p81983835613"></a><a name="p81983835613"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p612111417564"><a name="p612111417564"></a><a name="p612111417564"></a>10s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p138556589553"><a name="p138556589553"></a><a name="p138556589553"></a>Timeout used for the lookup of the JobManager actor object. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row519985712915"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1721554105514"><a name="p1721554105514"></a><a name="p1721554105514"></a>akka.framesize</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4198188155611"><a name="p4198188155611"></a><a name="p4198188155611"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3121144562"><a name="p3121144562"></a><a name="p3121144562"></a>10485760b</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p885575845510"><a name="p885575845510"></a><a name="p885575845510"></a>Maximum size of messages which are sent between the JobManager and the TaskManagers. If Flink fails because messages exceed this limit, then you should increase it. The unit is b/B/KB/MB.</p>
</td>
</tr>
<tr id="row5199857192912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p662721515561"><a name="p662721515561"></a><a name="p662721515561"></a>akka.watch.heartbeat.interval</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p171973315569"><a name="p171973315569"></a><a name="p171973315569"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p178702710567"><a name="p178702710567"></a><a name="p178702710567"></a>10s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p62841820185610"><a name="p62841820185610"></a><a name="p62841820185610"></a>Heartbeat interval for Akka's DeathWatch mechanism to detect dead TaskManagers. If TaskManagers are wrongly marked dead because of lost or delayed heartbeat messages, then you should decrease this value. The unit is ms/s/m/h/d.</p>
<div class="note" id="note1542393885610"><a name="note1542393885610"></a><a name="note1542393885610"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15424538105615"><a name="p15424538105615"></a><a name="p15424538105615"></a>A thorough description of Akka's DeathWatch can be found at <a href="http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector" target="_blank" rel="noopener noreferrer">http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector</a>.</p>
</div></div>
</td>
</tr>
<tr id="row82003573299"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7627141511561"><a name="p7627141511561"></a><a name="p7627141511561"></a>akka.watch.heartbeat.pause</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p117191133145617"><a name="p117191133145617"></a><a name="p117191133145617"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p987927165611"><a name="p987927165611"></a><a name="p987927165611"></a>60s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p122843206562"><a name="p122843206562"></a><a name="p122843206562"></a>Acceptable heartbeat pause for Akka's DeathWatch mechanism. A low value does not allow an irregular heartbeat. The unit is ms/s/m/h/d.</p>
<div class="note" id="note28881951135617"><a name="note28881951135617"></a><a name="note28881951135617"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p48900519565"><a name="p48900519565"></a><a name="p48900519565"></a>A thorough description of Akka's DeathWatch can be found at <a href="http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector" target="_blank" rel="noopener noreferrer">http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector</a>.</p>
</div></div>
</td>
</tr>
<tr id="row3200125742911"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1657712548571"><a name="p1657712548571"></a><a name="p1657712548571"></a>akka.watch.threshold</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p99629169587"><a name="p99629169587"></a><a name="p99629169587"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17661013583"><a name="p17661013583"></a><a name="p17661013583"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p62761659105717"><a name="p62761659105717"></a><a name="p62761659105717"></a>Threshold for the DeathWatch failure detector. A low value is prone to false positives whereas a high value increases the time to detect a dead TaskManager.</p>
<div class="note" id="note0806521165812"><a name="note0806521165812"></a><a name="note0806521165812"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p027616591576"><a name="p027616591576"></a><a name="p027616591576"></a>A thorough description of Akka's DeathWatch can be found at <a href="http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector" target="_blank" rel="noopener noreferrer">http://doc.akka.io/docs/akka/snapshot/scala/remoting.html#failure-detector</a>.</p>
</div></div>
</td>
</tr>
<tr id="row1278412518579"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10577654165714"><a name="p10577654165714"></a><a name="p10577654165714"></a>akka.tcp.timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p18962131615817"><a name="p18962131615817"></a><a name="p18962131615817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p568100588"><a name="p568100588"></a><a name="p568100588"></a>20s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p192774598574"><a name="p192774598574"></a><a name="p192774598574"></a>Timeout for all outbound TCP connections. If you should experience problems with connecting to a TaskManager due to a slow network, you should increase this value. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row1996655114579"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p457735415712"><a name="p457735415712"></a><a name="p457735415712"></a>akka.throughput</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p159623161587"><a name="p159623161587"></a><a name="p159623161587"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p12661035815"><a name="p12661035815"></a><a name="p12661035815"></a>15</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p027711599579"><a name="p027711599579"></a><a name="p027711599579"></a>Number of messages that are processed in a batch before returning the thread to the pool. Low values denote a fair scheduling for actor message processing whereas high values can increase the performance at the cost of unfairness.</p>
</td>
</tr>
<tr id="row715211529576"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p689014019581"><a name="p689014019581"></a><a name="p689014019581"></a>akka.log.lifecycle.events</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p515112165912"><a name="p515112165912"></a><a name="p515112165912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p124581561583"><a name="p124581561583"></a><a name="p124581561583"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1396295065813"><a name="p1396295065813"></a><a name="p1396295065813"></a>Turns on the Akka's remote logging of events. Set this value to <strong id="b74370180719"><a name="b74370180719"></a><a name="b74370180719"></a>true</strong> in case of debugging.</p>
</td>
</tr>
<tr id="row532715214576"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p138902040135813"><a name="p138902040135813"></a><a name="p138902040135813"></a>akka.startup-timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1015120115912"><a name="p1015120115912"></a><a name="p1015120115912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p34583565582"><a name="p34583565582"></a><a name="p34583565582"></a>The default value is the same as the value of <strong id="b1080481418811"><a name="b1080481418811"></a><a name="b1080481418811"></a>akka.ask.timeout</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p18962750195818"><a name="p18962750195818"></a><a name="p18962750195818"></a>Timeout after which the startup of a remote component is considered being failed. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row95187522578"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6890940145815"><a name="p6890940145815"></a><a name="p6890940145815"></a>akka.ssl.enabled</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1215119165913"><a name="p1215119165913"></a><a name="p1215119165913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1845825613583"><a name="p1845825613583"></a><a name="p1845825613583"></a>true</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p16963115016585"><a name="p16963115016585"></a><a name="p16963115016585"></a>Turns on SSL for Akka's remote communication. This is applicable only when the global ssl flag <strong id="b1814052910912"><a name="b1814052910912"></a><a name="b1814052910912"></a>security.ssl</strong> is enabled.</p>
</td>
</tr>
</tbody>
</table>

## Configuring Secure Sockets Layer \(SSL\)<a name="section8618438178"></a>

When you need to configure a Flink cluster in security mode, you need to configure the SSL configuration items.

The configuration items include the SSL switch, certificate, password, and encryption algorithm.

**Table  4**  Parameter description

<a name="table956544414184"></a>
<table><thead align="left"><tr id="row65654448188"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p125657441185"><a name="p125657441185"></a><a name="p125657441185"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.02%" id="mcps1.2.5.1.2"><p id="p2056564431818"><a name="p2056564431818"></a><a name="p2056564431818"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.979999999999999%" id="mcps1.2.5.1.3"><p id="p13566644111819"><a name="p13566644111819"></a><a name="p13566644111819"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p20566644111819"><a name="p20566644111819"></a><a name="p20566644111819"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row175661544171818"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p81073617194"><a name="p81073617194"></a><a name="p81073617194"></a>security.ssl.internal.enabled</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p14385122514194"><a name="p14385122514194"></a><a name="p14385122514194"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p3514121911910"><a name="p3514121911910"></a><a name="p3514121911910"></a>The value is automatically configured based on the cluster installation mode.</p>
<a name="ul1251481921919"></a><a name="ul1251481921919"></a><ul id="ul1251481921919"><li>Security mode: The default value is <strong id="b1913333592011"><a name="b1913333592011"></a><a name="b1913333592011"></a>true</strong>.</li><li>Normal mode: The default value is <strong id="b0391348132015"><a name="b0391348132015"></a><a name="b0391348132015"></a>false</strong>.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p49151910101915"><a name="p49151910101915"></a><a name="p49151910101915"></a>Turns on SSL for internal network communication</p>
</td>
</tr>
<tr id="row145662044171818"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p310712613195"><a name="p310712613195"></a><a name="p310712613195"></a>security.ssl.internal.keystore</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p10385025161918"><a name="p10385025161918"></a><a name="p10385025161918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p115141819191915"><a name="p115141819191915"></a><a name="p115141819191915"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17915201041917"><a name="p17915201041917"></a><a name="p17915201041917"></a>Java keystore file</p>
</td>
</tr>
<tr id="row2566124421810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1410716171910"><a name="p1410716171910"></a><a name="p1410716171910"></a>security.ssl.internal.keystore-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p2038522514193"><a name="p2038522514193"></a><a name="p2038522514193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p85141219201914"><a name="p85141219201914"></a><a name="p85141219201914"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p109154103190"><a name="p109154103190"></a><a name="p109154103190"></a>Password used to decrypt the keystore file</p>
</td>
</tr>
<tr id="row2566044141812"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8666743171916"><a name="p8666743171916"></a><a name="p8666743171916"></a>security.ssl.internal.key-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p1243982122017"><a name="p1243982122017"></a><a name="p1243982122017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p122986550192"><a name="p122986550192"></a><a name="p122986550192"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8390124917196"><a name="p8390124917196"></a><a name="p8390124917196"></a>Password used to decrypt the server key in the keystore file</p>
</td>
</tr>
<tr id="row556784451810"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16666114317195"><a name="p16666114317195"></a><a name="p16666114317195"></a>security.ssl.internal.truststore</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p8439828207"><a name="p8439828207"></a><a name="p8439828207"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p1629816553190"><a name="p1629816553190"></a><a name="p1629816553190"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1239054951910"><a name="p1239054951910"></a><a name="p1239054951910"></a><strong id="b1050425181018"><a name="b1050425181018"></a><a name="b1050425181018"></a>truststore</strong> file containing the public CA certificates</p>
</td>
</tr>
<tr id="row656754451819"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4666543191910"><a name="p4666543191910"></a><a name="p4666543191910"></a>security.ssl.internal.truststore-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p94393212012"><a name="p94393212012"></a><a name="p94393212012"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p1329811556193"><a name="p1329811556193"></a><a name="p1329811556193"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p193904495195"><a name="p193904495195"></a><a name="p193904495195"></a>Password used to decrypt the truststore file</p>
</td>
</tr>
<tr id="row3567114491814"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p186661643151916"><a name="p186661643151916"></a><a name="p186661643151916"></a>security.ssl.protocol</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p7440423206"><a name="p7440423206"></a><a name="p7440423206"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p62991555201916"><a name="p62991555201916"></a><a name="p62991555201916"></a>TLSv1.2</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1039010497199"><a name="p1039010497199"></a><a name="p1039010497199"></a>SSL protocol version to be supported for the ssl transport</p>
</td>
</tr>
<tr id="row656817442185"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19666443201915"><a name="p19666443201915"></a><a name="p19666443201915"></a>security.ssl.algorithms</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p14440923204"><a name="p14440923204"></a><a name="p14440923204"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p1829955515198"><a name="p1829955515198"></a><a name="p1829955515198"></a>The default value is <strong id="b182131645123515"><a name="b182131645123515"></a><a name="b182131645123515"></a>TLS_RSA_WITH_AES_128_CBC_SHA256,TLS_DHE_RSA_WITH_AES_128_CBC_SHA256,TLS_DHE_DSS_WITH_AES_128_CBC_SHA256</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1139018493198"><a name="p1139018493198"></a><a name="p1139018493198"></a>Comma-separated list of standard SSL algorithms to be supported. For more information, visit the Java official website at <a href="http://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#ciphersuites" target="_blank" rel="noopener noreferrer">http://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#ciphersuites</a>.</p>
</td>
</tr>
<tr id="row136382191219"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6600113810141"><a name="p6600113810141"></a><a name="p6600113810141"></a>security.ssl.rest.enabled</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p1260013818147"><a name="p1260013818147"></a><a name="p1260013818147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p56001538111419"><a name="p56001538111419"></a><a name="p56001538111419"></a>The value is automatically configured based on the cluster installation mode.</p>
<a name="ul760019381146"></a><a name="ul760019381146"></a><ul id="ul760019381146"><li>Security mode: The default value is <strong id="b2931837103816"><a name="b2931837103816"></a><a name="b2931837103816"></a>true</strong>.</li><li>Normal mode: The default value is <strong id="b7715428382"><a name="b7715428382"></a><a name="b7715428382"></a>false</strong>.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p19600123817149"><a name="p19600123817149"></a><a name="p19600123817149"></a>Turns on SSL for external network communication</p>
</td>
</tr>
<tr id="row1243418413138"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2601638181411"><a name="p2601638181411"></a><a name="p2601638181411"></a>security.ssl.rest.keystore</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p1560117384142"><a name="p1560117384142"></a><a name="p1560117384142"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p8601193811419"><a name="p8601193811419"></a><a name="p8601193811419"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1660117384144"><a name="p1660117384144"></a><a name="p1660117384144"></a>Java keystore file</p>
</td>
</tr>
<tr id="row44761023191416"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1660115387148"><a name="p1660115387148"></a><a name="p1660115387148"></a>security.ssl.rest.keystore-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p6601203811145"><a name="p6601203811145"></a><a name="p6601203811145"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p18601103811142"><a name="p18601103811142"></a><a name="p18601103811142"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p6601133812144"><a name="p6601133812144"></a><a name="p6601133812144"></a>Password used to decrypt the keystore file</p>
</td>
</tr>
<tr id="row9427926201417"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p76012386145"><a name="p76012386145"></a><a name="p76012386145"></a>security.ssl.rest.key-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p3601183801413"><a name="p3601183801413"></a><a name="p3601183801413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p12601103819146"><a name="p12601103819146"></a><a name="p12601103819146"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p106013387143"><a name="p106013387143"></a><a name="p106013387143"></a>Password used to decrypt the server key in the keystore file</p>
</td>
</tr>
<tr id="row4324153081417"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1760193861412"><a name="p1760193861412"></a><a name="p1760193861412"></a>security.ssl.rest.truststore</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p8602438191412"><a name="p8602438191412"></a><a name="p8602438191412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p7602338161418"><a name="p7602338161418"></a><a name="p7602338161418"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p19602938161410"><a name="p19602938161410"></a><a name="p19602938161410"></a><strong id="b654622111012"><a name="b654622111012"></a><a name="b654622111012"></a>truststore</strong> file containing the public CA certificates</p>
</td>
</tr>
<tr id="row2245183321413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19602438111420"><a name="p19602438111420"></a><a name="p19602438111420"></a>security.ssl.rest.truststore-password</p>
</td>
<td class="cellrowborder" valign="top" width="15.02%" headers="mcps1.2.5.1.2 "><p id="p96021738151412"><a name="p96021738151412"></a><a name="p96021738151412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.979999999999999%" headers="mcps1.2.5.1.3 "><p id="p1760233813148"><a name="p1760233813148"></a><a name="p1760233813148"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p560283812149"><a name="p560283812149"></a><a name="p560283812149"></a>Password used to decrypt the truststore file</p>
</td>
</tr>
</tbody>
</table>

## Configuring Network Communication \(via Netty\)<a name="section510792792019"></a>

When Flink runs a job, data transmission and backpressure detection between tasks depend on the Netty. In some environments, the Netty parameters may need to be configured.

For advanced optimization, you can modify the following Netty configuration items. The default configuration can meet the requirements of tasks of large-scale clusters with high concurrent throughput. For details about the parameters, visit the Netty official website at  [http://netty.io/](http://netty.io/).

**Table  5**  Parameter description

<a name="table151072027112015"></a>
<table><thead align="left"><tr id="row2010720276207"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p910842792012"><a name="p910842792012"></a><a name="p910842792012"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p9108827162020"><a name="p9108827162020"></a><a name="p9108827162020"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p1410817274200"><a name="p1410817274200"></a><a name="p1410817274200"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p410822712203"><a name="p410822712203"></a><a name="p410822712203"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1310811274206"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1631132952313"><a name="p1631132952313"></a><a name="p1631132952313"></a>taskmanager.network.netty.num-arenas</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1527516483234"><a name="p1527516483234"></a><a name="p1527516483234"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p10785114014230"><a name="p10785114014230"></a><a name="p10785114014230"></a>taskmanager.numberOfTaskSlots</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p6703520234"><a name="p6703520234"></a><a name="p6703520234"></a>Number of Netty arenas</p>
</td>
</tr>
<tr id="row7108142712013"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1311142982317"><a name="p1311142982317"></a><a name="p1311142982317"></a>taskmanager.network.netty.server.numThreads</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p227510486230"><a name="p227510486230"></a><a name="p227510486230"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p18785154020239"><a name="p18785154020239"></a><a name="p18785154020239"></a>taskmanager.numberOfTaskSlots</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8743518232"><a name="p8743518232"></a><a name="p8743518232"></a>Number of Netty server threads</p>
</td>
</tr>
<tr id="row31091127192018"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p731113291231"><a name="p731113291231"></a><a name="p731113291231"></a>taskmanager.network.netty.client.numThreads</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1275134862316"><a name="p1275134862316"></a><a name="p1275134862316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p117851840132310"><a name="p117851840132310"></a><a name="p117851840132310"></a>taskmanager.numberOfTaskSlots</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p117935112317"><a name="p117935112317"></a><a name="p117935112317"></a>Number of Netty client threads</p>
</td>
</tr>
<tr id="row171101227202014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1731132914235"><a name="p1731132914235"></a><a name="p1731132914235"></a>taskmanager.network.netty.client.connectTimeoutSec</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p82757488236"><a name="p82757488236"></a><a name="p82757488236"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p678504015230"><a name="p678504015230"></a><a name="p678504015230"></a>120</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1871435172310"><a name="p1871435172310"></a><a name="p1871435172310"></a>Netty client connection timeout. The unit is <strong id="b3258131761410"><a name="b3258131761410"></a><a name="b3258131761410"></a>s</strong>.</p>
</td>
</tr>
<tr id="row11103272204"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p113111629152317"><a name="p113111629152317"></a><a name="p113111629152317"></a>taskmanager.network.netty.sendReceiveBufferSize</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p327511480236"><a name="p327511480236"></a><a name="p327511480236"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13785104010235"><a name="p13785104010235"></a><a name="p13785104010235"></a>4096</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p471335152318"><a name="p471335152318"></a><a name="p471335152318"></a>Netty send and receive buffer size. This defaults to the system buffer size (<strong id="b14606181618314"><a name="b14606181618314"></a><a name="b14606181618314"></a>cat /proc/sys/net/ipv4/tcp_[rw]mem</strong>) and is 4 MB in modern Linux. The unit is bytes.</p>
</td>
</tr>
<tr id="row1111011279201"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9159164718209"><a name="p9159164718209"></a><a name="p9159164718209"></a>taskmanager.network.netty.transport</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p51581947152015"><a name="p51581947152015"></a><a name="p51581947152015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1415717478209"><a name="p1415717478209"></a><a name="p1415717478209"></a>nio</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p18156147182016"><a name="p18156147182016"></a><a name="p18156147182016"></a>Netty transport type, either <strong id="b125187421225"><a name="b125187421225"></a><a name="b125187421225"></a>nio</strong> or <strong id="b68268448221"><a name="b68268448221"></a><a name="b68268448221"></a>epoll</strong></p>
</td>
</tr>
</tbody>
</table>

## Configuring the JobManager Web Frontend<a name="section51271561248"></a>

When the JobManager is started, the Web server will be started in the same process.

-   You can access the web server to obtain information about the current Flink cluster, including JobManager, TaskManager, and jobs running in the cluster.
-   You can set the parameters of the web server.

The configuration includes ports, temporary directories, display items, error redirection, and security.

**Table  6**  Parameter description

<a name="table812755682411"></a>
<table><thead align="left"><tr id="row161286561240"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p7128556192419"><a name="p7128556192419"></a><a name="p7128556192419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1128856122419"><a name="p1128856122419"></a><a name="p1128856122419"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p19128125602412"><a name="p19128125602412"></a><a name="p19128125602412"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p4128185610247"><a name="p4128185610247"></a><a name="p4128185610247"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1712865672420"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3627925202618"><a name="p3627925202618"></a><a name="p3627925202618"></a>jobmanager.web.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1539124613267"><a name="p1539124613267"></a><a name="p1539124613267"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1886718402267"><a name="p1886718402267"></a><a name="p1886718402267"></a>32261-32325</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p175673412618"><a name="p175673412618"></a><a name="p175673412618"></a>Web port. Value range: 32261-32325</p>
</td>
</tr>
<tr id="row055212279"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11873743142718"><a name="p11873743142718"></a><a name="p11873743142718"></a>jobmanager.web.allow-access-address</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p7997172192820"><a name="p7997172192820"></a><a name="p7997172192820"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p166814569275"><a name="p166814569275"></a><a name="p166814569275"></a>*</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p165032515277"><a name="p165032515277"></a><a name="p165032515277"></a>Web access whitelist. IP addresses are separated by commas (,). Only IP addresses in the whitelist can access the web.</p>
</td>
</tr>
</tbody>
</table>

## Configuring the File Systems<a name="section795833918285"></a>

Result files are created when tasks are running. Flink enables you to configure parameters for file creation.

The configuration items include file overwriting policies and directory creation.

**Table  7**  Parameter description

<a name="table1454185635918"></a>
<table><thead align="left"><tr id="row1455656185916"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p34551256165913"><a name="p34551256165913"></a><a name="p34551256165913"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p34555565596"><a name="p34555565596"></a><a name="p34555565596"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p545515561598"><a name="p545515561598"></a><a name="p545515561598"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p194551656135914"><a name="p194551656135914"></a><a name="p194551656135914"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15455175618598"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p544415222017"><a name="p544415222017"></a><a name="p544415222017"></a>fs.overwrite-files</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p127041545101"><a name="p127041545101"></a><a name="p127041545101"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p25288391705"><a name="p25288391705"></a><a name="p25288391705"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17182103111012"><a name="p17182103111012"></a><a name="p17182103111012"></a>Whether to overwrite existing files</p>
</td>
</tr>
<tr id="row12456145615593"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p154444221002"><a name="p154444221002"></a><a name="p154444221002"></a>fs.output.always-create-directory</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1670474517014"><a name="p1670474517014"></a><a name="p1670474517014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p145291039803"><a name="p145291039803"></a><a name="p145291039803"></a>false</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1918219311905"><a name="p1918219311905"></a><a name="p1918219311905"></a>File writers running with a parallelism larger than one create a directory for the output file path and put the different result files (one per parallel writer task) into that directory.</p>
<a name="ul618213311903"></a><a name="ul618213311903"></a><ul id="ul618213311903"><li>If this option is set to <strong id="b138164512516"><a name="b138164512516"></a><a name="b138164512516"></a>true</strong>, writers with a parallelism of 1 will also create a directory and place a single result file into it.</li><li>If the option is set to <strong id="b10981122516266"><a name="b10981122516266"></a><a name="b10981122516266"></a>false</strong>, writers with a parallelism of 1 will directly create the file directly at the output path, without creating a containing directory.</li></ul>
</td>
</tr>
</tbody>
</table>

## Configuring the State Backend<a name="section5704059307"></a>

Flink provides HA and job recovery upon exceptions, as well as job suspension and recovery during version upgrade. For the storage of the job status, Flink depends on the state backend, and job restart depends on restart policies. You can configure the two parts.

The configuration items include the state backend type, storage path, and restart policy.

**Table  8**  Parameter description

<a name="table8462851313"></a>
<table><thead align="left"><tr id="row134629518113"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p14637519120"><a name="p14637519120"></a><a name="p14637519120"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p164631451519"><a name="p164631451519"></a><a name="p164631451519"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p204638511515"><a name="p204638511515"></a><a name="p204638511515"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p2463105116117"><a name="p2463105116117"></a><a name="p2463105116117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row84631251613"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p98851230425"><a name="p98851230425"></a><a name="p98851230425"></a>state.checkpoints.dir</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p6871152924"><a name="p6871152924"></a><a name="p6871152924"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p119898471928"><a name="p119898471928"></a><a name="p119898471928"></a>hdfs:///flink/checkpoints</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p17673339522"><a name="p17673339522"></a><a name="p17673339522"></a>Path when the backend is set to <strong id="b16159457163519"><a name="b16159457163519"></a><a name="b16159457163519"></a>filesystem</strong>. The path must be accessible from JobManagers. A local path supports only the local mode. In cluster mode, use an HDFS path.</p>
</td>
</tr>
<tr id="row94242586114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1885130424"><a name="p1885130424"></a><a name="p1885130424"></a>state.savepoints.dir</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p198714527216"><a name="p198714527216"></a><a name="p198714527216"></a>Mandatory in security mode</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p698954711215"><a name="p698954711215"></a><a name="p698954711215"></a>hdfs:///flink/savepoint</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p5673439123"><a name="p5673439123"></a><a name="p5673439123"></a>Path for storing savepoints.</p>
<p id="p367393917212"><a name="p367393917212"></a><a name="p367393917212"></a>If you have not specified an HDFS path when storing savepoints, you can use the parameter to configure a path. </p>
</td>
</tr>
<tr id="row1876205820115"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p188513016214"><a name="p188513016214"></a><a name="p188513016214"></a>restart-strategy</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p887116521022"><a name="p887116521022"></a><a name="p887116521022"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p139897471726"><a name="p139897471726"></a><a name="p139897471726"></a>fixed-delay</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p9673113910214"><a name="p9673113910214"></a><a name="p9673113910214"></a>Restart policy. The options are as follows:</p>
<a name="ul8673193914215"></a><a name="ul8673193914215"></a><ul id="ul8673193914215"><li>fixed-delay</li><li>failure-rate</li><li>none</li></ul>
</td>
</tr>
<tr id="row1549591112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16324157315"><a name="p16324157315"></a><a name="p16324157315"></a>restart-strategy.fixed-delay.attempts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p673913286318"><a name="p673913286318"></a><a name="p673913286318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><a name="ul58332197311"></a><a name="ul58332197311"></a><ul id="ul58332197311"><li>If the checkpoint is enabled in a job, the default value is <strong id="b17762194943917"><a name="b17762194943917"></a><a name="b17762194943917"></a>Integer.MAX_VALUE</strong>.</li><li>If the checkpoint is not enabled in the job, the default value is <strong id="b1930976124120"><a name="b1930976124120"></a><a name="b1930976124120"></a>3</strong>.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p92519141730"><a name="p92519141730"></a><a name="p92519141730"></a>Number of retries of the fixed-delay policy. For details about the policy, see <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.7/dev/restart_strategies.html" target="_blank" rel="noopener noreferrer">https://ci.apache.org/projects/flink/flink-docs-release-1.7/dev/restart_strategies.html</a>.</p>
</td>
</tr>
<tr id="row1923419591214"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4324145937"><a name="p4324145937"></a><a name="p4324145937"></a>restart-strategy.fixed-delay.delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p77394288319"><a name="p77394288319"></a><a name="p77394288319"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><a name="ul88331119535"></a><a name="ul88331119535"></a><ul id="ul88331119535"><li>If the checkpoint is enabled in the job, the default value is <strong id="b2059613216314"><a name="b2059613216314"></a><a name="b2059613216314"></a>10s</strong>.</li><li>If the checkpoint is not enabled in a job, the default value is the same as the value of <strong id="b5293175913112"><a name="b5293175913112"></a><a name="b5293175913112"></a>akka.ask.timeout</strong>.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p11256149316"><a name="p11256149316"></a><a name="p11256149316"></a>Interval of fixed-delay policy retries. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row1450111592012"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1310116478313"><a name="p1310116478313"></a><a name="p1310116478313"></a>restart-strategy.failure-rate.max-failures-per-interval</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p145273412418"><a name="p145273412418"></a><a name="p145273412418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17012581631"><a name="p17012581631"></a><a name="p17012581631"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p167541529313"><a name="p167541529313"></a><a name="p167541529313"></a>Number of retries of the failure-rate policy. For details about the policy, see <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.7/dev/restart_strategies.html" target="_blank" rel="noopener noreferrer">https://ci.apache.org/projects/flink/flink-docs-release-1.7/dev/restart_strategies.html</a>.</p>
</td>
</tr>
<tr id="row18825135911114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61019473311"><a name="p61019473311"></a><a name="p61019473311"></a>restart-strategy.failure-rate.failure-rate-interval</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1352716411413"><a name="p1352716411413"></a><a name="p1352716411413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3701105815310"><a name="p3701105815310"></a><a name="p3701105815310"></a>60s</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p87549525314"><a name="p87549525314"></a><a name="p87549525314"></a>Retry time of the failure-rate policy. The unit is ms/s/m/h/d.</p>
</td>
</tr>
<tr id="row9116018216"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19101124719315"><a name="p19101124719315"></a><a name="p19101124719315"></a>restart-strategy.failure-rate.delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p15527174542"><a name="p15527174542"></a><a name="p15527174542"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4701858431"><a name="p4701858431"></a><a name="p4701858431"></a>The default value is the same as the value of <strong id="b16360183953719"><a name="b16360183953719"></a><a name="b16360183953719"></a>akka.ask.timeout</strong>. For details, see <strong id="b1746223118384"><a name="b1746223118384"></a><a name="b1746223118384"></a>Configuring the Distributed Coordination (via Akka)</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1754105217318"><a name="p1754105217318"></a><a name="p1754105217318"></a>Interval of failure-rate policy retries. The unit is ms/s/m/h/d.</p>
</td>
</tr>
</tbody>
</table>

## Configuring the Kerberos-based Security<a name="section28916381843"></a>

Flink Kerberos configuration items must be configured in security mode.

The configuration items include the keytab and principal of Kerberos.

**Table  9**  Parameter description

<a name="table454519361652"></a>
<table><thead align="left"><tr id="row8545163613511"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p105451236759"><a name="p105451236759"></a><a name="p105451236759"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p6546103620517"><a name="p6546103620517"></a><a name="p6546103620517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p165468361352"><a name="p165468361352"></a><a name="p165468361352"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p85461362512"><a name="p85461362512"></a><a name="p85461362512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19546193617518"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p65961071165"><a name="p65961071165"></a><a name="p65961071165"></a>security.kerberos.login.keytab</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p123904324616"><a name="p123904324616"></a><a name="p123904324616"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1283812241612"><a name="p1283812241612"></a><a name="p1283812241612"></a>Configure the parameter based on actual service requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p25071175618"><a name="p25071175618"></a><a name="p25071175618"></a>Keytab file path. This parameter is a client parameter.</p>
</td>
</tr>
<tr id="row13655647852"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25961574615"><a name="p25961574615"></a><a name="p25961574615"></a>security.kerberos.login.principal</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1039014322616"><a name="p1039014322616"></a><a name="p1039014322616"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p48380241264"><a name="p48380241264"></a><a name="p48380241264"></a>Configure the parameter based on actual service requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p550719171963"><a name="p550719171963"></a><a name="p550719171963"></a>This parameter is a client parameter. If both the keytab and principal are set, keytab authentication is used by default.</p>
</td>
</tr>
<tr id="row171251748952"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1759620710614"><a name="p1759620710614"></a><a name="p1759620710614"></a>security.kerberos.login.contexts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p739033214612"><a name="p739033214612"></a><a name="p739033214612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p13838152413617"><a name="p13838152413617"></a><a name="p13838152413617"></a>Client, KafkaClient</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1150811171061"><a name="p1150811171061"></a><a name="p1150811171061"></a>Contexts of the jass file generated by Flink. This parameter is a server parameter.</p>
</td>
</tr>
</tbody>
</table>

## Configure the HA<a name="section83813381560"></a>

The HA mode of Flink depends on ZooKeeper. Therefore, ZooKeeper must be configured.

The configuration items include the ZooKeeper address, path, and security authentication.

**Table  10**  Parameter description

<a name="table4784519778"></a>
<table><thead align="left"><tr id="row1278513191176"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p197856191671"><a name="p197856191671"></a><a name="p197856191671"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p167856191970"><a name="p167856191970"></a><a name="p167856191970"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p107855191478"><a name="p107855191478"></a><a name="p107855191478"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p197855197713"><a name="p197855197713"></a><a name="p197855197713"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row978514194716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7379201120813"><a name="p7379201120813"></a><a name="p7379201120813"></a>high-availability</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p22382361986"><a name="p22382361986"></a><a name="p22382361986"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p124818301813"><a name="p124818301813"></a><a name="p124818301813"></a>zookeeper</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p186533228815"><a name="p186533228815"></a><a name="p186533228815"></a>Whether to enable HA. Two modes are supported:</p>
<a name="ul2091118445817"></a><a name="ul2091118445817"></a><ul id="ul2091118445817"><li>none: Only a single jobManager is running. The checkpoint is disabled for the jobManager.</li><li>ZooKeeper<a name="ul51738558335"></a><a name="ul51738558335"></a><ul id="ul51738558335"><li>In non-YARN mode, multiple jobManagers are supported and a leader is elected.</li><li>In YARN mode, only one jobManager exists.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row825818427718"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p0379611188"><a name="p0379611188"></a><a name="p0379611188"></a>high-availability.zookeeper.quorum</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p112381363818"><a name="p112381363818"></a><a name="p112381363818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17481153012810"><a name="p17481153012810"></a><a name="p17481153012810"></a>Automatic configuration</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p11653322981"><a name="p11653322981"></a><a name="p11653322981"></a>ZooKeeper quorum address</p>
</td>
</tr>
<tr id="row2906042970"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p6379161116813"><a name="p6379161116813"></a><a name="p6379161116813"></a>high-availability.zookeeper.path.root</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p02380361487"><a name="p02380361487"></a><a name="p02380361487"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p144811830688"><a name="p144811830688"></a><a name="p144811830688"></a>/flink</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p9653162216819"><a name="p9653162216819"></a><a name="p9653162216819"></a>Root directory created by Flink on ZooKeeper for storing metadata required by the HA mode</p>
</td>
</tr>
<tr id="row1351924312719"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3379611984"><a name="p3379611984"></a><a name="p3379611984"></a>high-availability.storageDir</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p52425361486"><a name="p52425361486"></a><a name="p52425361486"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1248113305810"><a name="p1248113305810"></a><a name="p1248113305810"></a>hdfs:///flink/recovery</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p76531522889"><a name="p76531522889"></a><a name="p76531522889"></a>Directory for storing JobManager metadata in the state backend. ZooKeeper stores only the pointers of the actual data.</p>
</td>
</tr>
<tr id="row139515447717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16230721193"><a name="p16230721193"></a><a name="p16230721193"></a>high-availability.zookeeper.client.session-timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1562132416915"><a name="p1562132416915"></a><a name="p1562132416915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1354717157915"><a name="p1354717157915"></a><a name="p1354717157915"></a>60000</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p575619818917"><a name="p575619818917"></a><a name="p575619818917"></a>ZooKeeper client session timeout interval The unit is ms.</p>
</td>
</tr>
<tr id="row076834410710"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14230421991"><a name="p14230421991"></a><a name="p14230421991"></a>high-availability.zookeeper.client.connection-timeout</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p56219247917"><a name="p56219247917"></a><a name="p56219247917"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p105478153910"><a name="p105478153910"></a><a name="p105478153910"></a>15000</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1375712814910"><a name="p1375712814910"></a><a name="p1375712814910"></a>ZooKeeper client connection timeout interval The unit is ms.</p>
</td>
</tr>
<tr id="row5459645276"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12305214915"><a name="p12305214915"></a><a name="p12305214915"></a>high-availability.zookeeper.client.retry-wait</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p20620248911"><a name="p20620248911"></a><a name="p20620248911"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p854771510917"><a name="p854771510917"></a><a name="p854771510917"></a>5000</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p27571385913"><a name="p27571385913"></a><a name="p27571385913"></a>ZooKeeper client retry wait time. The unit is ms.</p>
</td>
</tr>
<tr id="row910517461873"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p02301621910"><a name="p02301621910"></a><a name="p02301621910"></a>high-availability.zookeeper.client.max-retry-attempts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p862824792"><a name="p862824792"></a><a name="p862824792"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p185507159916"><a name="p185507159916"></a><a name="p185507159916"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8757981996"><a name="p8757981996"></a><a name="p8757981996"></a>Maximum number of ZooKeeper client retries</p>
</td>
</tr>
<tr id="row178612191574"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p923042798"><a name="p923042798"></a><a name="p923042798"></a>high-availability.zookeeper.client.acl</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p196292410911"><a name="p196292410911"></a><a name="p196292410911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9550101512910"><a name="p9550101512910"></a><a name="p9550101512910"></a>The value is automatically configured based on the cluster installation mode.</p>
<a name="ul9550111519914"></a><a name="ul9550111519914"></a><ul id="ul9550111519914"><li>Security mode: <strong id="b94059310315"><a name="b94059310315"></a><a name="b94059310315"></a>creator</strong></li><li>Normal mode: <strong id="b1086241520314"><a name="b1086241520314"></a><a name="b1086241520314"></a>open</strong></li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1575719812919"><a name="p1575719812919"></a><a name="p1575719812919"></a>ACL (open creator) of the ZooKeeper node</p>
</td>
</tr>
<tr id="row278715191572"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1824116366914"><a name="p1824116366914"></a><a name="p1824116366914"></a>zookeeper.sasl.disable</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p148821570104"><a name="p148821570104"></a><a name="p148821570104"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p181010212104"><a name="p181010212104"></a><a name="p181010212104"></a>The value is automatically configured based on the cluster installation mode.</p>
<a name="ul11101172101018"></a><a name="ul11101172101018"></a><ul id="ul11101172101018"><li>Security mode: <strong id="b1867872493715"><a name="b1867872493715"></a><a name="b1867872493715"></a>false</strong></li><li>Normal mode: <strong id="b814353115378"><a name="b814353115378"></a><a name="b814353115378"></a>true</strong></li></ul>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p872016421092"><a name="p872016421092"></a><a name="p872016421092"></a>Whether to enable SASL authentication</p>
</td>
</tr>
<tr id="row2788201914715"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p192413361898"><a name="p192413361898"></a><a name="p192413361898"></a>zookeeper.sasl.service-name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p788217751010"><a name="p788217751010"></a><a name="p788217751010"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1210120211018"><a name="p1210120211018"></a><a name="p1210120211018"></a>zookeeper</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><a name="ul107205421091"></a><a name="ul107205421091"></a><ul id="ul107205421091"><li>If a service name different from the ZooKeeper service name is configured on the ZooKeeper server, you can set this parameter.</li><li>If the service names on the client and server are different, the authentication fails.</li></ul>
</td>
</tr>
</tbody>
</table>

## Configuring the Environment<a name="section481819171312"></a>

If the JVM configuration has special requirements, the JVM parameters can be transferred to the client, JobMananger, and TaskManager using configuration items.

You can configure the following JVM parameters

**Table  11**  Parameter description

<a name="table10693153613148"></a>
<table><thead align="left"><tr id="row18694103691419"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1869453691411"><a name="p1869453691411"></a><a name="p1869453691411"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p46941836171419"><a name="p46941836171419"></a><a name="p46941836171419"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p15694636151418"><a name="p15694636151418"></a><a name="p15694636151418"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p0694436171411"><a name="p0694436171411"></a><a name="p0694436171411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13695153614147"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1386535331416"><a name="p1386535331416"></a><a name="p1386535331416"></a>env.java.opts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2923918153"><a name="p2923918153"></a><a name="p2923918153"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p19865105315141"><a name="p19865105315141"></a><a name="p19865105315141"></a>-Xloggc:&lt;LOG_DIR&gt;/gc.log -XX:+PrintGCDetails -XX:-OmitStackTraceInFastThrow -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=20 -XX:GCLogFileSize=20M</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p19865553181411"><a name="p19865553181411"></a><a name="p19865553181411"></a>JVM parameter, which is transferred to the startup script, JobManager, TaskManager, and YARN client. For example, transfer remote debugging parameters.</p>
</td>
</tr>
</tbody>
</table>

## Configuring YARN<a name="section1217131071812"></a>

When Flink runs on a YARN cluster, the JobManager runs on the ApplicationMaster. Some configuration parameters of the JobManager depend on YARN. Therefore, you can configure YARN to improve Flink performance on YARN.

The configuration items include the memory, virtual kernel, and port of the YARN container.

**Table  12**  Parameter description

<a name="table1797925013183"></a>
<table><thead align="left"><tr id="row20979135015183"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5979350121819"><a name="p5979350121819"></a><a name="p5979350121819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1297975061820"><a name="p1297975061820"></a><a name="p1297975061820"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p2098085012184"><a name="p2098085012184"></a><a name="p2098085012184"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p10980165010189"><a name="p10980165010189"></a><a name="p10980165010189"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row69809503189"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p342974316269"><a name="p342974316269"></a><a name="p342974316269"></a>yarn.maximum-failed-containers</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p76935918274"><a name="p76935918274"></a><a name="p76935918274"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p767833162719"><a name="p767833162719"></a><a name="p767833162719"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p16466185216262"><a name="p16466185216262"></a><a name="p16466185216262"></a>Maximum number of containers the system is going to reallocate in case of a container failure of the TaskManager. The default value is the number of TaskManagers when the Flink cluster is started.</p>
</td>
</tr>
<tr id="row1841814588188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p84299434261"><a name="p84299434261"></a><a name="p84299434261"></a>yarn.application-attempts</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p8693119162710"><a name="p8693119162710"></a><a name="p8693119162710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p136781238278"><a name="p136781238278"></a><a name="p136781238278"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p74671152102616"><a name="p74671152102616"></a><a name="p74671152102616"></a>Number of ApplicationMaster restarts. The value is the maximum value in the validity interval that is set to Akka's timeout in Flink. After the restart, the IP address and port number of the ApplicationMaster will change and you will need to connect to the client manually.</p>
</td>
</tr>
<tr id="row89261659181819"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1842904322616"><a name="p1842904322616"></a><a name="p1842904322616"></a>yarn.heartbeat-delay</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p176932982716"><a name="p176932982716"></a><a name="p176932982716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p56781239275"><a name="p56781239275"></a><a name="p56781239275"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p44671852152612"><a name="p44671852152612"></a><a name="p44671852152612"></a>Time between heartbeats with the ApplicationMaster and YARN ResourceManager in seconds </p>
</td>
</tr>
<tr id="row93514010191"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1142920435267"><a name="p1142920435267"></a><a name="p1142920435267"></a>yarn.containers.vcores</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2069339142711"><a name="p2069339142711"></a><a name="p2069339142711"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p567833112710"><a name="p567833112710"></a><a name="p567833112710"></a>The default value is the number of TaskManager slots.</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p94671852152617"><a name="p94671852152617"></a><a name="p94671852152617"></a>Number of virtual cores (vcores) per YARN container</p>
</td>
</tr>
<tr id="row91325011919"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1013211041917"><a name="p1013211041917"></a><a name="p1013211041917"></a>yarn.application-master.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p146931094272"><a name="p146931094272"></a><a name="p146931094272"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p14679193202714"><a name="p14679193202714"></a><a name="p14679193202714"></a>32586-32650</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1213217012199"><a name="p1213217012199"></a><a name="p1213217012199"></a>ApplicationMaster port number setting. A port number range is supported.</p>
</td>
</tr>
</tbody>
</table>

