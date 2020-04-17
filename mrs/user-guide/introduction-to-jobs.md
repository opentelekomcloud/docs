# Introduction to Jobs<a name="EN-US_TOPIC_0221415044"></a>

A job is a program execution platform provided by MRS for users to process and analyze user data. After a job is created, all job information is displayed on the  **Jobs**  tab page. You can view a list of all jobs and create and manage jobs. If the  **Jobs**  tab is not displayed on the cluster details page, submit a job in the background.

Data sources processed by MRS are from OBS or HDFS. OBS is an object-based storage service that provides customers with massive, secure, reliable, and cost-effective data storage capabilities. MRS can process data in OBS directly. You can view, manage, and use data by using the web page of the management console or OBS Client. In addition, you can use REST APIs independently or integrate APIs to service applications to manage and access data.

Before creating a job, you need to upload local data to OBS so that MRS can use data in OBS for computing and analysis. You can also import data from OBS to HDFS for computing and analysis. After data is processed and analyzed, you can store the data in HDFS or export the data from the cluster to OBS. Both HDFS and OBS can also store compressed data in  **bz2**  and  **gz**  formats.

## **Job Types**<a name="section992317541770"></a>

MRS clusters enable you to create and manage the following types of jobs. If a cluster in the  **Running**  state fails to create a job, check the health status of related components on the cluster management page. For details, see  [Viewing the System Overview](viewing-the-system-overview.md).

-   MapReduce: a distributed data processing framework that implements rapid, parallel processing of massive amounts of data MRS supports the submission of MapReduce JAR programs.
-   Spark: a distributed in-memory computing framework. MRS supports SparkSubmit, Spark Script, and Spark SQL jobs.
    -   SparkSubmit: submits Spark JAR and Python programs, executes Spark applications, and computes and processes user data.
    -   Spark Script: submits the Spark Script scripts and batch executes Spark SQL statements.
    -   Spark SQL: uses Spark SQL statements \(similar to SQL statements\) to query and analyze user data in real time.

-   Hive: an open source data warehouse based on Hadoop MRS allows you to submit Hive Script scripts and execute Hive SQL statements.
-   Flink: a distributed big data processing engine that can perform stateful computations over both finite and infinite data streams.

## Job List<a name="section767813216424"></a>

Jobs are listed in chronological order by default in the job list, with the most recent jobs displayed at the top.  [Table 1](#table38822211162654)  describes parameters of the job list.

**Table  1**  Parameters of the job list

<a name="table38822211162654"></a>
<table><thead align="left"><tr id="row34098764162654"><th class="cellrowborder" valign="top" width="20.14%" id="mcps1.2.3.1.1"><p id="p27719311162654"><a name="p27719311162654"></a><a name="p27719311162654"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="79.86%" id="mcps1.2.3.1.2"><p id="p30671727162654"><a name="p30671727162654"></a><a name="p30671727162654"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5133774811331"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p6471688511331"><a name="p6471688511331"></a><a name="p6471688511331"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p630823112430"><a name="p630823112430"></a><a name="p630823112430"></a>Job name</p>
<p id="p757632711331"><a name="p757632711331"></a><a name="p757632711331"></a>This parameter is set when a job is added.</p>
</td>
</tr>
<tr id="row7610089162654"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p12437454162654"><a name="p12437454162654"></a><a name="p12437454162654"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p38190428112449"><a name="p38190428112449"></a><a name="p38190428112449"></a>Unique identifier of a job</p>
<p id="p800868162654"><a name="p800868162654"></a><a name="p800868162654"></a>This parameter is automatically assigned when a job is added.</p>
</td>
</tr>
<tr id="row5485151310383"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p15486313183812"><a name="p15486313183812"></a><a name="p15486313183812"></a>User Name</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p448711316381"><a name="p448711316381"></a><a name="p448711316381"></a>Name of the user who submits a job</p>
</td>
</tr>
<tr id="row6153362791419"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p1816792591419"><a name="p1816792591419"></a><a name="p1816792591419"></a>Type</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p20181386103913"><a name="p20181386103913"></a><a name="p20181386103913"></a>Job type</p>
<p id="p3529406111256"><a name="p3529406111256"></a><a name="p3529406111256"></a>Possible types include:</p>
<a name="ul48223439103955"></a><a name="ul48223439103955"></a><ul id="ul48223439103955"><li>Distcp (data import and export)</li><li>MapReduce</li><li>Spark</li><li>SparkSubmit</li><li>SparkScript</li><li>SparkSQL</li><li>HiveSQL</li><li>HiveScript</li><li>Flink</li></ul>
<div class="note" id="note1880140112120"><a name="note1880140112120"></a><a name="note1880140112120"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul18242201511307"></a><a name="ul18242201511307"></a><ul id="ul18242201511307"><li>After importing and exporting files on the <strong id="b1528751143319"><a name="b1528751143319"></a><a name="b1528751143319"></a>Files</strong> tab page, you can view the DistCp job on the <strong id="b15657011348"><a name="b15657011348"></a><a name="b15657011348"></a>Jobs</strong> tab page.</li><li>Spark, Hive, and Flink jobs can be added only when the Spark, Hive, and Flink components are selected during cluster creation and the cluster is running.</li></ul>
</div></div>
</td>
</tr>
<tr id="row44482813113250"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p46338114113250"><a name="p46338114113250"></a><a name="p46338114113250"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p62399739113250"><a name="p62399739113250"></a><a name="p62399739113250"></a>Job status</p>
<a name="ul805096292920"></a><a name="ul805096292920"></a><ul id="ul805096292920"><li>Accepted</li><li>Running</li><li>Completed</li><li>Terminated</li><li>Abnormal</li></ul>
</td>
</tr>
<tr id="row494107911332"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p6468315011332"><a name="p6468315011332"></a><a name="p6468315011332"></a>Result</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p484376011332"><a name="p484376011332"></a><a name="p484376011332"></a>Execution result of a job</p>
<a name="ul181311052133412"></a><a name="ul181311052133412"></a><ul id="ul181311052133412"><li>Undefined: job that is being executed</li><li>Successful: job that has been successfully executed</li><li>Terminated: job that is manually terminated during execution</li><li>Failed: job that fails to be executed</li></ul>
<div class="note" id="note23001598114642"><a name="note23001598114642"></a><a name="note23001598114642"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5687796114642"><a name="p5687796114642"></a><a name="p5687796114642"></a>You cannot execute a successful or failed job, but can add or copy the job. After setting job parameters, you can submit the job again.</p>
</div></div>
</td>
</tr>
<tr id="row10398735103918"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p33981535103914"><a name="p33981535103914"></a><a name="p33981535103914"></a>Submit Time</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p1839813350391"><a name="p1839813350391"></a><a name="p1839813350391"></a>Time when a job is submitted</p>
</td>
</tr>
<tr id="row5015631210823"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p3612949610823"><a name="p3612949610823"></a><a name="p3612949610823"></a>Duration (min)</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><p id="p80592499273"><a name="p80592499273"></a><a name="p80592499273"></a>Duration of executing a job, specifically from the time when a job is started to the time when the job is completed or stopped.</p>
<p id="p46107106194735"><a name="p46107106194735"></a><a name="p46107106194735"></a>Unit: minute</p>
</td>
</tr>
<tr id="row65463200102813"><td class="cellrowborder" valign="top" width="20.14%" headers="mcps1.2.3.1.1 "><p id="p918993102813"><a name="p918993102813"></a><a name="p918993102813"></a>Operation</p>
</td>
<td class="cellrowborder" valign="top" width="79.86%" headers="mcps1.2.3.1.2 "><a name="ul32902424102818"></a><a name="ul32902424102818"></a><ul id="ul32902424102818"><li>View Log: You can click <span class="uicontrol" id="uicontrol18395883141358"><a name="uicontrol18395883141358"></a><a name="uicontrol18395883141358"></a><b>View Log</b></span>&nbsp;to view job details. For details, see&nbsp;<a href="viewing-job-configurations-and-logs.md">Viewing Job Configurations and Logs</a>.</li><li>View Details: You can click <span class="uicontrol" id="uicontrol58686534131324"><a name="uicontrol58686534131324"></a><a name="uicontrol58686534131324"></a><b>View Details</b></span> to view job configuration details. For details, see <a href="viewing-job-configurations-and-logs.md">Viewing Job Configurations and Logs</a>.</li><li>More<a name="ul442089152448"></a><a name="ul442089152448"></a><ul id="ul442089152448"><li>Stop: You can click <span class="uicontrol" id="uicontrol35324187141428"><a name="uicontrol35324187141428"></a><a name="uicontrol35324187141428"></a><b>Stop</b></span>&nbsp;to stop a running job. For details, see&nbsp;<a href="stopping-jobs.md">Stopping Jobs</a>.</li><li>Copy: You can click <span class="uicontrol" id="uicontrol4290319114458"><a name="uicontrol4290319114458"></a><a name="uicontrol4290319114458"></a><b>Copy</b></span>&nbsp;to copy and add a job. For details, see&nbsp;<a href="copying-jobs.md">Copying Jobs</a>.</li><li>Delete: You can click <span class="uicontrol" id="uicontrol3871999111454"><a name="uicontrol3871999111454"></a><a name="uicontrol3871999111454"></a><b>Delete</b></span>&nbsp;to delete a job. For details, see&nbsp;<a href="deleting-jobs.md">Deleting Jobs</a>.</li><li>View Result: Click <strong id="b9333104583613"><a name="b9333104583613"></a><a name="b9333104583613"></a>View Result</strong> to view the execution results of SparkSql and SparkScript jobs whose status is <strong id="b73331545103617"><a name="b73331545103617"></a><a name="b73331545103617"></a>Completed</strong> and result is <strong id="b2333144514364"><a name="b2333144514364"></a><a name="b2333144514364"></a>Successful</strong>.</li></ul>
<div class="note" id="note51800213103051"><a name="note51800213103051"></a><a name="note51800213103051"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul66515382134835"></a><a name="ul66515382134835"></a><ul id="ul66515382134835"><li>Spark SQL jobs cannot be stopped.</li><li>Deleted jobs cannot be recovered. Therefore, exercise caution when deleting a job.</li><li>If you configure the system to save job logs to an HDFS or OBS path, the system compresses the logs and saves them to the specified path after job execution is complete. In this case, the job remains in the <strong id="b143411119195614"><a name="b143411119195614"></a><a name="b143411119195614"></a>Running</strong> state after execution is complete and changes to the&nbsp;<strong id="b0532202535611"><a name="b0532202535611"></a><a name="b0532202535611"></a>Completed</strong> state after the logs are successfully saved. The time required for saving the logs depends on the log size. The process generally takes a few minutes.</li></ul>
</div></div>
</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  2**  Button description

<a name="table3011042510139"></a>
<table><thead align="left"><tr id="row708755810139"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p6655665410139"><a name="p6655665410139"></a><a name="p6655665410139"></a>Button</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p2237991710139"><a name="p2237991710139"></a><a name="p2237991710139"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39542281513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p204811203334"><a name="p204811203334"></a><a name="p204811203334"></a><a name="image12594184913311"></a><a name="image12594184913311"></a><span><img id="image12594184913311" src="figures/icon_mrs_time.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p154811720123319"><a name="p154811720123319"></a><a name="p154811720123319"></a>Select a time range for job submission to filter jobs submitted in the time range.</p>
</td>
</tr>
<tr id="row9266410139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p750586110139"><a name="p750586110139"></a><a name="p750586110139"></a><a name="image6147517310551"></a><a name="image6147517310551"></a><span><img id="image6147517310551" src="figures/icon_mrs_cluster_state.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5344702710412"><a name="p5344702710412"></a><a name="p5344702710412"></a>In the drop-down list, select a job state to filter jobs.</p>
<a name="ul1294383513519"></a><a name="ul1294383513519"></a><ul id="ul1294383513519"><li>All (<em id="i5208025513850"><a name="i5208025513850"></a><a name="i5208025513850"></a>Num</em>): displays all jobs.</li><li>Completed (<em id="i1076234213926"><a name="i1076234213926"></a><a name="i1076234213926"></a>Num</em>): displays jobs in the&nbsp;<span class="parmvalue" id="parmvalue43001197135329"><a name="parmvalue43001197135329"></a><a name="parmvalue43001197135329"></a><b>Completed</b></span> state.</li><li>Running (<em id="i57294438135056"><a name="i57294438135056"></a><a name="i57294438135056"></a>Num</em>): displays jobs in the&nbsp;<span class="parmvalue" id="parmvalue2226683135335"><a name="parmvalue2226683135335"></a><a name="parmvalue2226683135335"></a><b>Running</b></span> state.</li><li>Terminated (<em id="i6612885013928"><a name="i6612885013928"></a><a name="i6612885013928"></a>Num</em>): displays jobs in the&nbsp;<span class="parmvalue" id="parmvalue38572679135341"><a name="parmvalue38572679135341"></a><a name="parmvalue38572679135341"></a><b>Terminated</b></span> state.</li><li>Abnormal (<em id="i741281013931"><a name="i741281013931"></a><a name="i741281013931"></a>Num</em>): displays jobs in the&nbsp;<span class="parmvalue" id="parmvalue19485886135347"><a name="parmvalue19485886135347"></a><a name="parmvalue19485886135347"></a><b>Abnormal</b></span> state.</li></ul>
</td>
</tr>
<tr id="row525993935113"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p5460565357"><a name="p5460565357"></a><a name="p5460565357"></a><a name="image84625693514"></a><a name="image84625693514"></a><span><img id="image84625693514" src="figures/icon_mrs_cluster_state.jpg"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p6780114713464"><a name="p6780114713464"></a><a name="p6780114713464"></a>Select a job type from the drop-down list to filter jobs of the type.</p>
<a name="ul4111131216471"></a><a name="ul4111131216471"></a><ul id="ul4111131216471"><li>MapReduce</li><li>HiveScript</li><li>Distcp</li><li>SparkScript</li><li>SparkSql</li><li>SparkSubmit</li><li>Flink</li><li>HiveSql</li></ul>
</td>
</tr>
<tr id="row3595494810139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2666966910139"><a name="p2666966910139"></a><a name="p2666966910139"></a><a name="image4216691415377"></a><a name="image4216691415377"></a><span><img id="image4216691415377" src="figures/icon_mrs_search_l.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1275954610139"><a name="p1275954610139"></a><a name="p1275954610139"></a>Enter a job name in the search bar and click <a name="image39798271153710"></a><a name="image39798271153710"></a><span><img id="image39798271153710" src="figures/icon_mrs_search_l.png"></span> to search for a job.</p>
</td>
</tr>
<tr id="row4772705110139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4068596210139"><a name="p4068596210139"></a><a name="p4068596210139"></a><a name="image37927300153746"></a><a name="image37927300153746"></a><span><img id="image37927300153746" src="figures/icon_mrs_fresh_r.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p722865810139"><a name="p722865810139"></a><a name="p722865810139"></a>Click <a name="image45988224153748"></a><a name="image45988224153748"></a><span><img id="image45988224153748" src="figures/icon_mrs_fresh_r.png"></span> to manually refresh the job list.</p>
</td>
</tr>
</tbody>
</table>

