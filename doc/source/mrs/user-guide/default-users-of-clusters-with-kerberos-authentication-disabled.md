# Default Users of Clusters with Kerberos Authentication Disabled<a name="EN-US_TOPIC_0221415052"></a>

## User Classification<a name="section1350246891412"></a>

The MRS cluster provides the following two types of users.

>![](/images/icon-note.gif) **NOTE:**   
>Users are required to periodically change their passwords. It is not recommended to use the default passwords.  

<a name="table5775715391436"></a>
<table><thead align="left"><tr id="row1711617395159"><th class="cellrowborder" valign="top" width="21.5%" id="mcps1.1.3.1.1"><p id="p6615004295159"><a name="p6615004295159"></a><a name="p6615004295159"></a>User Type</p>
</th>
<th class="cellrowborder" valign="top" width="78.5%" id="mcps1.1.3.1.2"><p id="p1740607395159"><a name="p1740607395159"></a><a name="p1740607395159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2920896895159"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="p2608605395159"><a name="p2608605395159"></a><a name="p2608605395159"></a>System user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><p id="p42047670113639"><a name="p42047670113639"></a><a name="p42047670113639"></a>A user used to run OMS system processes.</p>
</td>
</tr>
<tr id="row2029769795159"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="p4429483295159"><a name="p4429483295159"></a><a name="p4429483295159"></a>Database user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><a name="ul1872352891436"></a><a name="ul1872352891436"></a><ul id="ul1872352891436"><li>Used to manage the OMS database and access data.</li><li>Used to run the database of service components (Hive<span id="ph1428663413147"><a name="ph1428663413147"></a><a name="ph1428663413147"></a>, Loader</span> and DBService).</li></ul>
</td>
</tr>
</tbody>
</table>

## System Users<a name="section4899716991522"></a>

>![](/images/icon-note.gif) **NOTE:**   
>-   User  **ldap**  of the OS is required in the MRS cluster. Do not delete the account. Otherwise, the cluster may not work properly. Password management policies are maintained by the users.  
>-   Reset the password when you change the passwords of user  **ommdba** and user **omm**  for the first time. Change the passwords regularly after you have retrieved them.  

<a name="table2048716191613"></a>
<table><thead align="left"><tr id="row4683794795430"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.1"><p id="p1228795895430"><a name="p1228795895430"></a><a name="p1228795895430"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.2"><p id="p2354800595430"><a name="p2354800595430"></a><a name="p2354800595430"></a>Username</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.1.5.1.3"><p id="p1385895395430"><a name="p1385895395430"></a><a name="p1385895395430"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.1.5.1.4"><p id="p6319369995430"><a name="p6319369995430"></a><a name="p6319369995430"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4111234124513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p60989730112132"><a name="en-us_topic_0039905375_p60989730112132"></a><a name="en-us_topic_0039905375_p60989730112132"></a>MRS cluster system user</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0039905375_p51034606112141"><a name="en-us_topic_0039905375_p51034606112141"></a><a name="en-us_topic_0039905375_p51034606112141"></a>admin</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p40162450112141"><a name="en-us_topic_0039905375_p40162450112141"></a><a name="en-us_topic_0039905375_p40162450112141"></a>Specified by the user when the cluster is created</p>
<a name="ul13495342204211"></a><a name="ul13495342204211"></a><ul id="ul13495342204211"><li>For versions earlier than MRS 1.9.2, the initial password is MIG2oAMCAQGhAw@IBAaIDAgwCAQGkgZ8@wgZwwVKAHMAWgAw@IBAKFJMEgABD4gA</li><li>For MRS 1.9.2 or later, specified by the user when the cluster is created.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.4 "><a name="ul9418182411432"></a><a name="ul9418182411432"></a><ul id="ul9418182411432"><li>For versions earlier than MRS 1.9.2, default user of MRS Manager. The user is used to record the cluster audit logs.</li><li>For MRS 1.9.2 or later, administrator of MRS Manager.<p id="p1830119316464"><a name="p1830119316464"></a><a name="p1830119316464"></a>This user also has the following rights:</p>
<a name="ul77702491530"></a><a name="ul77702491530"></a><ul id="ul77702491530"><li>Common HDFS and ZooKeeper user rights.</li><li>Rights to submit and query MapReduce and Yarn tasks, to manage Yarn queues, and to access the Yarn web UI.</li><li>Rights to submit, query, activate, deactivate, reassign, delete topologies, and operate all topologies of the Storm service.</li><li>Rights to create, delete, authenticate, reassign, consume, write, and query topics of the Kafka service.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row2675238595430"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p4882155219466"><a name="p4882155219466"></a><a name="p4882155219466"></a>MRS cluster node OS user</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="p3272498295430"><a name="p3272498295430"></a><a name="p3272498295430"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><p id="p2735260795430"><a name="p2735260795430"></a><a name="p2735260795430"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.4 "><p id="p1135567795430"><a name="p1135567795430"></a><a name="p1135567795430"></a>Internal running user of the MRS cluster system. This user is an OS user generated on all nodes and does not require a unified password.</p>
</td>
</tr>
<tr id="row4980193315711"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p37124171094"><a name="p37124171094"></a><a name="p37124171094"></a>MRS cluster node OS user</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="p1798153317720"><a name="p1798153317720"></a><a name="p1798153317720"></a>root</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.3 "><p id="p290881820369"><a name="p290881820369"></a><a name="p290881820369"></a>Password set by the user</p>
<div class="note" id="note3698172111377"><a name="note3698172111377"></a><a name="note3698172111377"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p26986210379"><a name="p26986210379"></a><a name="p26986210379"></a>This user is applicable only to MRS clusters of 1.6.2 or an later version.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.5.1.4 "><p id="p139811331973"><a name="p139811331973"></a><a name="p139811331973"></a>User used to log in to a node in the MRS cluster. This user is an OS user generated on all nodes.</p>
</td>
</tr>
</tbody>
</table>

## User Group Information<a name="section2451602294412"></a>

<a name="table4858345094426"></a>
<table><thead align="left"><tr id="row2146537095542"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p3990133295542"><a name="p3990133295542"></a><a name="p3990133295542"></a>Default User Group</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p96478795542"><a name="p96478795542"></a><a name="p96478795542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2453917316102"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p4151598216102"><a name="p4151598216102"></a><a name="p4151598216102"></a>supergroup</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p735138016102"><a name="p735138016102"></a><a name="p735138016102"></a>Primary group of user <span class="parmname" id="parmname5655540218537"><a name="parmname5655540218537"></a><a name="parmname5655540218537"></a><b>admin</b></span>. The primary group does not have additional permissions in the cluster where Kerberos authentication is disabled.</p>
</td>
</tr>
<tr id="row4187683195542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1020533295542"><a name="p1020533295542"></a><a name="p1020533295542"></a>check_sec_ldap</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p21225813212946"><a name="p21225813212946"></a><a name="p21225813212946"></a>Used to test whether the active LDAP works properly. This user group is generated randomly in a test and automatically deleted after the test is complete. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row6202335295542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p5417034895542"><a name="p5417034895542"></a><a name="p5417034895542"></a>Manager_tenant</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1876492818846"><a name="p1876492818846"></a><a name="p1876492818846"></a>Tenant system user group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row5098181595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p2111250095542"><a name="p2111250095542"></a><a name="p2111250095542"></a>System_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p642151095542"><a name="p642151095542"></a><a name="p642151095542"></a>MRS cluster system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row5038033795542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p3424211195542"><a name="p3424211195542"></a><a name="p3424211195542"></a>Manager_viewer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p4912728295542"><a name="p4912728295542"></a><a name="p4912728295542"></a>MRS Manager system viewer group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row1988690795542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1837033895542"><a name="p1837033895542"></a><a name="p1837033895542"></a>Manager_operator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p26828595542"><a name="p26828595542"></a><a name="p26828595542"></a>MRS Manager system operator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row2173111295542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p3860433595542"><a name="p3860433595542"></a><a name="p3860433595542"></a>Manager_auditor</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1419340395542"><a name="p1419340395542"></a><a name="p1419340395542"></a>MRS Manager system auditor group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row881498995542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p5441215695542"><a name="p5441215695542"></a><a name="p5441215695542"></a>Manager_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p4611097695542"><a name="p4611097695542"></a><a name="p4611097695542"></a>MRS Manager system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row4400159695542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p5925231695542"><a name="p5925231695542"></a><a name="p5925231695542"></a>compcommon</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p5990857795542"><a name="p5990857795542"></a><a name="p5990857795542"></a>MRS cluster internal group for accessing public cluster resources. All system users and system running users are added to this user group by default.</p>
</td>
</tr>
<tr id="row2075655595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p1987619595542"><a name="p1987619595542"></a><a name="p1987619595542"></a>default_1000</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1519838595542"><a name="p1519838595542"></a><a name="p1519838595542"></a>This group is created for tenants. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="row18425425161515"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p6660743316163"><a name="p6660743316163"></a><a name="p6660743316163"></a>kafka</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p2649299716163"><a name="p2649299716163"></a><a name="p2649299716163"></a>Kafka common user group. A user added to this user group can access a topic only when a user in the kafkaadmin group grants the read and write permission of the topic to the user.</p>
</td>
</tr>
<tr id="row62919529161518"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p5315117616163"><a name="p5315117616163"></a><a name="p5315117616163"></a>kafkasuperuser</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1027802016163"><a name="p1027802016163"></a><a name="p1027802016163"></a>Users added to this user group have the read and write permission of all topics.</p>
</td>
</tr>
<tr id="row46699625161521"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p4359333816163"><a name="p4359333816163"></a><a name="p4359333816163"></a>kafkaadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p4139945616163"><a name="p4139945616163"></a><a name="p4139945616163"></a>Kafka administrator group. Users added to this user group have the rights to create, delete, authorize, read, and write all topics.</p>
</td>
</tr>
<tr id="row13621888161524"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p4832384216163"><a name="p4832384216163"></a><a name="p4832384216163"></a>storm</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p2191713316163"><a name="p2191713316163"></a><a name="p2191713316163"></a>Users added to this user group can submit topologies and manage their own topologies.</p>
</td>
</tr>
<tr id="row52300902161527"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p568046316163"><a name="p568046316163"></a><a name="p568046316163"></a>stormadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p5746432816163"><a name="p5746432816163"></a><a name="p5746432816163"></a>Users added to this user group can have the storm administrator rights and can submit topologies and manage all topologies.</p>
</td>
</tr>
</tbody>
</table>

<a name="table211708839453"></a>
<table><thead align="left"><tr id="row6615973595611"><th class="cellrowborder" valign="top" width="35.449999999999996%" id="mcps1.1.3.1.1"><p id="p1389513595611"><a name="p1389513595611"></a><a name="p1389513595611"></a>OS User Group</p>
</th>
<th class="cellrowborder" valign="top" width="64.55%" id="mcps1.1.3.1.2"><p id="p3214485995611"><a name="p3214485995611"></a><a name="p3214485995611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4637249295611"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="p4544462795611"><a name="p4544462795611"></a><a name="p4544462795611"></a>wheel</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="p6462427095611"><a name="p6462427095611"></a><a name="p6462427095611"></a>Primary group of MRS internal running user <strong id="b1376962105451"><a name="b1376962105451"></a><a name="b1376962105451"></a>omm</strong>.</p>
</td>
</tr>
<tr id="row7450595611"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="p1907089695611"><a name="p1907089695611"></a><a name="p1907089695611"></a>ficommon</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="p3323036495611"><a name="p3323036495611"></a><a name="p3323036495611"></a>MRS cluster common group that corresponds to <strong id="b730495895611"><a name="b730495895611"></a><a name="b730495895611"></a>compcommon</strong> for accessing public cluster resource files stored in the OS.</p>
</td>
</tr>
</tbody>
</table>

## Database Users<a name="section4435701994533"></a>

MRS cluster system database users contain OMS database users and DBService database users.

>![](/images/icon-note.gif) **NOTE:**   
>Do not delete the following database users. Otherwise, the cluster or services may not work properly.  

<a name="table5909699494551"></a>
<table><thead align="left"><tr id="row1142646795648"><th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.1"><p id="p845453895648"><a name="p845453895648"></a><a name="p845453895648"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.2"><p id="p3830635895648"><a name="p3830635895648"></a><a name="p3830635895648"></a>Default User</p>
</th>
<th class="cellrowborder" valign="top" width="20.727927207279272%" id="mcps1.1.5.1.3"><p id="p532192795648"><a name="p532192795648"></a><a name="p532192795648"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="37.03629637036296%" id="mcps1.1.5.1.4"><p id="p2055510095648"><a name="p2055510095648"></a><a name="p2055510095648"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6356712795648"><td class="cellrowborder" rowspan="2" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="p4944294095648"><a name="p4944294095648"></a><a name="p4944294095648"></a>OMS database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="p5799178295648"><a name="p5799178295648"></a><a name="p5799178295648"></a>ommdba</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="p4393240495648"><a name="p4393240495648"></a><a name="p4393240495648"></a>dbChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="p793760895648"><a name="p793760895648"></a><a name="p793760895648"></a>OMS database administrator who performs maintenance operations, such as creating, starting, and stopping applications</p>
</td>
</tr>
<tr id="row2363231995648"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p3017065895648"><a name="p3017065895648"></a><a name="p3017065895648"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p4564730595648"><a name="p4564730595648"></a><a name="p4564730595648"></a>ChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p5222216695648"><a name="p5222216695648"></a><a name="p5222216695648"></a>User for accessing OMS database data</p>
</td>
</tr>
<tr id="row3844649595648"><td class="cellrowborder" rowspan="4" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="p5234370695648"><a name="p5234370695648"></a><a name="p5234370695648"></a>DBService database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="p3100402795648"><a name="p3100402795648"></a><a name="p3100402795648"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="p1045897795648"><a name="p1045897795648"></a><a name="p1045897795648"></a>dbserverAdmin@123</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="p3609226895648"><a name="p3609226895648"></a><a name="p3609226895648"></a>Administrator of the GaussDB database in the DBService component</p>
</td>
</tr>
<tr id="row5016024095648"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p6657988295648"><a name="p6657988295648"></a><a name="p6657988295648"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p1901402595648"><a name="p1901402595648"></a><a name="p1901402595648"></a>HiveUser@</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p6275127795648"><a name="p6275127795648"></a><a name="p6275127795648"></a>User for Hive to connect to the DBService database</p>
</td>
</tr>
<tr id="row5007927915519"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p12702391155119"><a name="p12702391155119"></a><a name="p12702391155119"></a>hue</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p22260713155119"><a name="p22260713155119"></a><a name="p22260713155119"></a>HueUser@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p58287344155119"><a name="p58287344155119"></a><a name="p58287344155119"></a>User for Hue to connect to the DBService database</p>
</td>
</tr>
<tr id="row14652288141612"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p33774791141612"><a name="p33774791141612"></a><a name="p33774791141612"></a><span id="ph45687739141645"><a name="ph45687739141645"></a><a name="ph45687739141645"></a>sqoop</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p51403535141612"><a name="p51403535141612"></a><a name="p51403535141612"></a><span id="ph8940219141636"><a name="ph8940219141636"></a><a name="ph8940219141636"></a>SqoopUser@</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p2936783141612"><a name="p2936783141612"></a><a name="p2936783141612"></a><span id="ph93799379121"><a name="ph93799379121"></a><a name="ph93799379121"></a>User for Loader to connect to the DBService database</span></p>
</td>
</tr>
</tbody>
</table>

