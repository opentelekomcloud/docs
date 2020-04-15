# Introduction<a name="EN-US_TOPIC_0125375459"></a>

## Overview<a name="section390719392123"></a>

MRS Manager provides backup and recovery for user data and system data. The backup function is provided based on components to back up Manager data \(including OMS data and LdapServer data\), Hive user data, component metadata saved in DBService, and HDFS metadata.

Backup and recovery tasks are performed in the following scenarios:

-   Routine backup is performed to ensure the data security of the system and components.
-   If  the system is faulty, backup data can be used to restore the system.
-   If the active cluster is completely faulty, an image cluster identical to the active cluster needs to be created. Backup data can be used to perform restoration operations.

**Table  1**  Backing up metadata

<a name="table1654317792245"></a>
<table><thead align="left"><tr id="row2147592392245"><th class="cellrowborder" valign="top" width="30.17%" id="mcps1.2.3.1.1"><p id="p6182817592245"><a name="p6182817592245"></a><a name="p6182817592245"></a><strong id="b3705449392251"><a name="b3705449392251"></a><a name="b3705449392251"></a>Backup Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.83%" id="mcps1.2.3.1.2"><p id="p4202630492245"><a name="p4202630492245"></a><a name="p4202630492245"></a><strong id="b4862395192251"><a name="b4862395192251"></a><a name="b4862395192251"></a>Backup Content</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4868750292245"><td class="cellrowborder" valign="top" width="30.17%" headers="mcps1.2.3.1.1 "><p id="p5137360092245"><a name="p5137360092245"></a><a name="p5137360092245"></a>OMS</p>
</td>
<td class="cellrowborder" valign="top" width="69.83%" headers="mcps1.2.3.1.2 "><p id="p51209592245"><a name="p51209592245"></a><a name="p51209592245"></a>Back up database data (excluding alarm data) and configuration data in the cluster management system.</p>
</td>
</tr>
<tr id="row460885892245"><td class="cellrowborder" valign="top" width="30.17%" headers="mcps1.2.3.1.1 "><p id="p3777325592245"><a name="p3777325592245"></a><a name="p3777325592245"></a>LdapServer</p>
</td>
<td class="cellrowborder" valign="top" width="69.83%" headers="mcps1.2.3.1.2 "><p id="p3973480492245"><a name="p3973480492245"></a><a name="p3973480492245"></a>Back up user information, including the username, password, key, password policy, and group information.</p>
</td>
</tr>
<tr id="row6222204392933"><td class="cellrowborder" valign="top" width="30.17%" headers="mcps1.2.3.1.1 "><p id="p5160595392933"><a name="p5160595392933"></a><a name="p5160595392933"></a>DBService</p>
</td>
<td class="cellrowborder" valign="top" width="69.83%" headers="mcps1.2.3.1.2 "><p id="p1933265492933"><a name="p1933265492933"></a><a name="p1933265492933"></a>Back up metadata of the component (Hive) managed by DBService.</p>
</td>
</tr>
<tr id="row3673972292933"><td class="cellrowborder" valign="top" width="30.17%" headers="mcps1.2.3.1.1 "><p id="p5212520692933"><a name="p5212520692933"></a><a name="p5212520692933"></a>NameNode</p>
</td>
<td class="cellrowborder" valign="top" width="69.83%" headers="mcps1.2.3.1.2 "><p id="p6139213592933"><a name="p6139213592933"></a><a name="p6139213592933"></a>Back up HDFS metadata.</p>
</td>
</tr>
</tbody>
</table>

## Principles<a name="section286669379257"></a>

**Task**

Before backup or recovery, you need to create a backup or recovery task and set task parameters, such as the task name, backup data source, and type of directories for saving backup files. When Manager is used to recover the data of HDFS, Hive, and NameNode, the cluster cannot be accessed.

Each backup task can back up different data sources and generate independent backup files for each data source. All the backup files generated in each task form a backup file set, which can be used in recovery tasks. Backup files can be stored on Linux local disks, HDFS of the local cluster, and HDFS of the standby cluster. The backup task provides both full and incremental backup policies. HDFS and Hive backup tasks support the incremental backup policy, while OMS, LdapServer, DBService, and NameNode backup tasks support only the full backup policy.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The rules for task execution are as follows:  
>-   If a task is being executed,  it cannot be executed repeatedly and other tasks cannot be started at the same time.  
>-   The interval at which a periodic task is automatically executed must be greater than 120s; otherwise, the task is postponed and will be executed in the next period. Manual tasks can be executed at any interval.  
>-   When a periodic task is to be automatically executed, the current time cannot be 120s later than the task start time; otherwise, the task is postponed and will be executed in the next period.  
>-   When a periodic task is locked, it cannot be automatically executed and needs to be manually unlocked.  
>-   Before an OMS, LdapServer, DBService, or NameNode backup task starts, ensure that the  **LocalBackup**  partition on the active management node has more than 20 GB available space; otherwise, the backup task cannot be started.  
>-   When planning backup and recovery tasks, select the data you want to back up or recover according to the service logic, data storage structure, and database or table association. By default, the system creates periodic backup task **default** that has an execution interval of  24 hours to perform full backup of OMS, LdapServer, DBService, and NameNode data to the Linux local disk.  

**Snapshot**

The system adopts the snapshot technology to quickly back up data. Snapshots include HDFS snapshots.

An HDFS snapshot is a read-only backup of HDFS at a specified time point.  It is used in data backup, misoperation protection, and disaster recovery.

The snapshot function can be enabled for any HDFS directory to create the related snapshot file. Before creating a snapshot for a directory, the system automatically enables the snapshot function for the directory. Snapshot creation does not affect HDFS operations. A maximum of 65,536 snapshots can be created for each HDFS directory.

When a snapshot has been created for an HDFS directory, the directory cannot be deleted and the directory name cannot be modified before the snapshot is deleted. Snapshots cannot be created for the upper-layer directories or subdirectories of the directory.

**DistCp**

Distributed copy \(DistCp\) is a tool used to replicate large amounts of data  within a cluster HDFS or between HDFSs of different clusters. In HBase, HDFS, or Hive backup or recovery tasks, if the data is backed up in HDFS of the standby cluster, the system invokes DistCp to perform the operation. You need to install the same version of MRS in the active and standby clusters.

DistCp uses MapReduce to implement data distribution, troubleshooting, recovery, and report. DistCp specifies different Map jobs for various source files and directories in the specified list. Each Map job copies the data in the partition that corresponds to the specified file in the list.

To use DistCp to perform data replication between HDFSs of two clusters, configure the cross-cluster trust relationship and enable the cross-cluster replication function for both clusters.

**Local quick recovery**

After using DistCp to back up the HDFS and Hive data of the local cluster to HDFS of the standby cluster, HDFS of the local cluster retains the backup data snapshots. Users can create local quick recovery tasks to recover data by using the snapshot files in HDFS of the local cluster.

## Specifications<a name="section1862623892756"></a>

**Table  2**  Backup and recovery feature specifications

<a name="table3449032192758"></a>
<table><thead align="left"><tr id="row6630409692758"><th class="cellrowborder" valign="top" width="50.05%" id="mcps1.2.3.1.1"><p id="p192271092758"><a name="p192271092758"></a><a name="p192271092758"></a><strong id="b2340042992813"><a name="b2340042992813"></a><a name="b2340042992813"></a>Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.95%" id="mcps1.2.3.1.2"><p id="p2152182892758"><a name="p2152182892758"></a><a name="p2152182892758"></a><strong id="b27841309163135"><a name="b27841309163135"></a><a name="b27841309163135"></a>Specifications</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6554654792758"><td class="cellrowborder" valign="top" width="50.05%" headers="mcps1.2.3.1.1 "><p id="p767012392758"><a name="p767012392758"></a><a name="p767012392758"></a>Maximum number of backup or recovery tasks</p>
</td>
<td class="cellrowborder" valign="top" width="49.95%" headers="mcps1.2.3.1.2 "><p id="p1730021192758"><a name="p1730021192758"></a><a name="p1730021192758"></a>100</p>
</td>
</tr>
<tr id="row2148417292758"><td class="cellrowborder" valign="top" width="50.05%" headers="mcps1.2.3.1.1 "><p id="p6249640092758"><a name="p6249640092758"></a><a name="p6249640092758"></a>Number of concurrent running tasks</p>
</td>
<td class="cellrowborder" valign="top" width="49.95%" headers="mcps1.2.3.1.2 "><p id="p2904364092758"><a name="p2904364092758"></a><a name="p2904364092758"></a>1</p>
</td>
</tr>
<tr id="row6006617392758"><td class="cellrowborder" valign="top" width="50.05%" headers="mcps1.2.3.1.1 "><p id="p3352187992758"><a name="p3352187992758"></a><a name="p3352187992758"></a>Maximum number of waiting tasks</p>
</td>
<td class="cellrowborder" valign="top" width="49.95%" headers="mcps1.2.3.1.2 "><p id="p3091770692758"><a name="p3091770692758"></a><a name="p3091770692758"></a>199</p>
</td>
</tr>
<tr id="row982390092758"><td class="cellrowborder" valign="top" width="50.05%" headers="mcps1.2.3.1.1 "><p id="p5753840692758"><a name="p5753840692758"></a><a name="p5753840692758"></a>Maximum size of backup files on a Linux local disk (GB)</p>
</td>
<td class="cellrowborder" valign="top" width="49.95%" headers="mcps1.2.3.1.2 "><p id="p3009929292758"><a name="p3009929292758"></a><a name="p3009929292758"></a>600</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Specifications of the  **default**  task

<a name="table1436149992850"></a>
<table><thead align="left"><tr id="row1979004392850"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.1"><p id="p5948962692850"><a name="p5948962692850"></a><a name="p5948962692850"></a><strong id="b4026873292855"><a name="b4026873292855"></a><a name="b4026873292855"></a>Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="p5393039092850"><a name="p5393039092850"></a><a name="p5393039092850"></a><strong id="b4054182292855"><a name="b4054182292855"></a><a name="b4054182292855"></a>OMS</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.3"><p id="p628543092850"><a name="p628543092850"></a><a name="p628543092850"></a><strong id="b6266216592855"><a name="b6266216592855"></a><a name="b6266216592855"></a>LdapServer</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.4"><p id="p3935779492850"><a name="p3935779492850"></a><a name="p3935779492850"></a><strong id="b4247063392855"><a name="b4247063392855"></a><a name="b4247063392855"></a>DBService</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.5"><p id="p3386477192850"><a name="p3386477192850"></a><a name="p3386477192850"></a><strong id="b1756924992855"><a name="b1756924992855"></a><a name="b1756924992855"></a>NameNode</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5869196992850"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5642905992850"><a name="p5642905992850"></a><a name="p5642905992850"></a>Backup period</p>
</td>
<td class="cellrowborder" colspan="4" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 mcps1.2.6.1.5 "><p id="p735109092850"><a name="p735109092850"></a><a name="p735109092850"></a>1 hour</p>
</td>
</tr>
<tr id="row6615981392850"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5734467492850"><a name="p5734467492850"></a><a name="p5734467492850"></a>Maximum number of backups</p>
</td>
<td class="cellrowborder" colspan="4" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 mcps1.2.6.1.5 "><p id="p1440700792850"><a name="p1440700792850"></a><a name="p1440700792850"></a>2</p>
</td>
</tr>
<tr id="row3372551492850"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p4741207992850"><a name="p4741207992850"></a><a name="p4741207992850"></a>Maximum size of a backup file</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p1517316892850"><a name="p1517316892850"></a><a name="p1517316892850"></a>10 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p2106712792850"><a name="p2106712792850"></a><a name="p2106712792850"></a>20 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p2871568992850"><a name="p2871568992850"></a><a name="p2871568992850"></a>100 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p4426948892850"><a name="p4426948892850"></a><a name="p4426948892850"></a>1.5 GB</p>
</td>
</tr>
<tr id="row6288107992850"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.1 "><p id="p6020264892850"><a name="p6020264892850"></a><a name="p6020264892850"></a>Maximum size of disk space used</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="p4457632192850"><a name="p4457632192850"></a><a name="p4457632192850"></a>20 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.3 "><p id="p5391228392850"><a name="p5391228392850"></a><a name="p5391228392850"></a>40 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.4 "><p id="p481883092850"><a name="p481883092850"></a><a name="p481883092850"></a>200 MB</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.5 "><p id="p5478092992850"><a name="p5478092992850"></a><a name="p5478092992850"></a>3 GB</p>
</td>
</tr>
<tr id="row2326631492850"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p552326492850"><a name="p552326492850"></a><a name="p552326492850"></a>Save path of backup data</p>
</td>
<td class="cellrowborder" colspan="4" valign="top" headers="mcps1.2.6.1.2 mcps1.2.6.1.3 mcps1.2.6.1.4 mcps1.2.6.1.5 "><p id="p4473127692850"><a name="p4473127692850"></a><a name="p4473127692850"></a><em id="i6703716492850"><a name="i6703716492850"></a><a name="i6703716492850"></a>Data save path</em><span class="filepath" id="filepath6483252817554"><a name="filepath6483252817554"></a><a name="filepath6483252817554"></a><b>/LocalBackup/</b></span> on active and standby management nodes</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The administrator must regularly transfer the backup data of the  **default**  task to an external cluster based on the enterprise's O&M requirements.  

