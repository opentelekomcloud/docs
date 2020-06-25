# Querying Information About a Job<a name="EN-US_TOPIC_0176790808"></a>

## Function<a name="section4408504619327"></a>

This API is used to query information about a specified job in an MRS cluster.

## URI<a name="section10186656193217"></a>

-   Format

    GET /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions/\{job\_execution\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39786771142917"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1503055142917"><a name="p1503055142917"></a><a name="p1503055142917"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p54638598142917"><a name="p54638598142917"></a><a name="p54638598142917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63650338142917"><a name="p63650338142917"></a><a name="p63650338142917"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row3457216201210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p194589160122"><a name="p194589160122"></a><a name="p194589160122"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p045813165125"><a name="p045813165125"></a><a name="p045813165125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1845891641218"><a name="p1845891641218"></a><a name="p1845891641218"></a>Cluster ID. For details on how to obtain the cluster ID, see <a href="obtain-mrs-cluster-information.md#section177891315153619">Obtaining a Cluster ID</a>.</p>
    </td>
    </tr>
    <tr id="row121835121146"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p218419125412"><a name="p218419125412"></a><a name="p218419125412"></a>job_execution_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16184161212420"><a name="p16184161212420"></a><a name="p16184161212420"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p121844121440"><a name="p121844121440"></a><a name="p121844121440"></a>Job ID. For details on how to obtain the job ID, see <a href="obtain-mrs-cluster-information.md#section247234143612">Obtaining a Job ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section673761354213"></a>

**Request parameters**

None

## Response<a name="section775516131425"></a>

**Table  2**  Response parameter description

<a name="table196481619161412"></a>
<table><thead align="left"><tr id="row1564911199147"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p38002029181415"><a name="p38002029181415"></a><a name="p38002029181415"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p1580062910148"><a name="p1580062910148"></a><a name="p1580062910148"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p1580082971414"><a name="p1580082971414"></a><a name="p1580082971414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11649141915141"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3649101914144"><a name="p3649101914144"></a><a name="p3649101914144"></a>job_detail</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p136493195149"><a name="p136493195149"></a><a name="p136493195149"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p136497196148"><a name="p136497196148"></a><a name="p136497196148"></a>Job details. For details about the parameter, see <a href="#table12040613193927">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Job parameter description

<a name="table12040613193927"></a>
<table><thead align="left"><tr id="row8843854193927"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p45263556193927"><a name="p45263556193927"></a><a name="p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p1907984993927"><a name="p1907984993927"></a><a name="p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17473879193927"><a name="p17473879193927"></a><a name="p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8387056194027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p52943541117"><a name="p52943541117"></a><a name="p52943541117"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12125168101212"><a name="p12125168101212"></a><a name="p12125168101212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p6329191671215"><a name="p6329191671215"></a><a name="p6329191671215"></a>Job ID.</p>
</td>
</tr>
<tr id="row19100834201113"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1029418549112"><a name="p1029418549112"></a><a name="p1029418549112"></a>user</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p512508201214"><a name="p512508201214"></a><a name="p512508201214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p183294166123"><a name="p183294166123"></a><a name="p183294166123"></a>Name of the user who submits a job.</p>
</td>
</tr>
<tr id="row1850318495114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12294125416119"><a name="p12294125416119"></a><a name="p12294125416119"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p191251789127"><a name="p191251789127"></a><a name="p191251789127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p153291516111218"><a name="p153291516111218"></a><a name="p153291516111218"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
</tr>
<tr id="row1910618551609"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1341817597018"><a name="p1341817597018"></a><a name="p1341817597018"></a>job_result</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p12418185915018"><a name="p12418185915018"></a><a name="p12418185915018"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p741885912014"><a name="p741885912014"></a><a name="p741885912014"></a>Final result of a job.</p>
<a name="ul141131420762"></a><a name="ul141131420762"></a><ul id="ul141131420762"><li><strong id="en-us_topic_0177065249_b5962144484014"><a name="en-us_topic_0177065249_b5962144484014"></a><a name="en-us_topic_0177065249_b5962144484014"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="en-us_topic_0177065249_b220555515416"><a name="en-us_topic_0177065249_b220555515416"></a><a name="en-us_topic_0177065249_b220555515416"></a>KILLED</strong>: indicates that the job is manually terminated during execution.</li><li><strong id="en-us_topic_0177065249_b15303108425"><a name="en-us_topic_0177065249_b15303108425"></a><a name="en-us_topic_0177065249_b15303108425"></a>UNDEFINED</strong>: indicates that the job is being executed.</li><li><strong id="en-us_topic_0177065249_b5686110134310"><a name="en-us_topic_0177065249_b5686110134310"></a><a name="en-us_topic_0177065249_b5686110134310"></a>SUCCEEDED</strong>: indicates that the job has been successfully executed.</li></ul>
</td>
</tr>
<tr id="row128711949131111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16294105413112"><a name="p16294105413112"></a><a name="p16294105413112"></a>job_state</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p11261885121"><a name="p11261885121"></a><a name="p11261885121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p232941614125"><a name="p232941614125"></a><a name="p232941614125"></a>Execution status of a job.</p>
<a name="ul83814473515"></a><a name="ul83814473515"></a><ul id="ul83814473515"><li><strong id="en-us_topic_0177065249_b595914457375"><a name="en-us_topic_0177065249_b595914457375"></a><a name="en-us_topic_0177065249_b595914457375"></a>FAILED</strong>: indicates that the job fails to be executed.</li><li><strong id="en-us_topic_0177065249_b16527105443719"><a name="en-us_topic_0177065249_b16527105443719"></a><a name="en-us_topic_0177065249_b16527105443719"></a>KILLED</strong>: indicates that the job is terminated.</li><li><strong id="en-us_topic_0177065249_b164941157183711"><a name="en-us_topic_0177065249_b164941157183711"></a><a name="en-us_topic_0177065249_b164941157183711"></a>New</strong>: indicates that the job is created.</li><li><strong id="en-us_topic_0177065249_b9727551382"><a name="en-us_topic_0177065249_b9727551382"></a><a name="en-us_topic_0177065249_b9727551382"></a>NEW_SAVING</strong>: indicates that the job has been created and is being saved.</li><li><strong id="en-us_topic_0177065249_b12002317395"><a name="en-us_topic_0177065249_b12002317395"></a><a name="en-us_topic_0177065249_b12002317395"></a>SUBMITTED</strong>: indicates that the job is submitted.</li><li><strong id="en-us_topic_0177065249_b171161926113914"><a name="en-us_topic_0177065249_b171161926113914"></a><a name="en-us_topic_0177065249_b171161926113914"></a>ACCEPTED</strong>: indicates that the job is accepted.</li><li><strong id="en-us_topic_0177065249_b132630124316"><a name="en-us_topic_0177065249_b132630124316"></a><a name="en-us_topic_0177065249_b132630124316"></a>RUNNING</strong>: indicates that the job is running.</li><li><strong id="en-us_topic_0177065249_b510618694011"><a name="en-us_topic_0177065249_b510618694011"></a><a name="en-us_topic_0177065249_b510618694011"></a>FINISHED</strong>: indicates that the job is completed.</li></ul>
</td>
</tr>
<tr id="row11227205011116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16294105418112"><a name="p16294105418112"></a><a name="p16294105418112"></a>job_progress</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p612614821210"><a name="p612614821210"></a><a name="p612614821210"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p832915169122"><a name="p832915169122"></a><a name="p832915169122"></a>Job execution progress.</p>
</td>
</tr>
<tr id="row11400175061120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p729415401114"><a name="p729415401114"></a><a name="p729415401114"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p13126198181216"><a name="p13126198181216"></a><a name="p13126198181216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p532941620128"><a name="p532941620128"></a><a name="p532941620128"></a>Type of a job.</p>
<a name="ul58695132184"></a><a name="ul58695132184"></a><ul id="ul58695132184"><li>MapReduce</li><li>SparkSubmit</li><li>HiveScript</li><li>HiveSql</li><li>DistCp, importing and exporting data</li><li>SparkScript</li><li>SparkSql</li><li>Flink</li></ul>
</td>
</tr>
<tr id="row12272193451118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1629585451114"><a name="p1629585451114"></a><a name="p1629585451114"></a>started_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1612698121215"><a name="p1612698121215"></a><a name="p1612698121215"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1433061611218"><a name="p1433061611218"></a><a name="p1433061611218"></a>Start time to run a job. Unit: ms.</p>
</td>
</tr>
<tr id="row139751543313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p169751343516"><a name="p169751343516"></a><a name="p169751343516"></a>submitted_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1497516434114"><a name="p1497516434114"></a><a name="p1497516434114"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p169754431714"><a name="p169754431714"></a><a name="p169754431714"></a>Time when a job is submitted. Unit: ms.</p>
</td>
</tr>
<tr id="row24471734181115"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p13295554131120"><a name="p13295554131120"></a><a name="p13295554131120"></a>finished_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1012618817121"><a name="p1012618817121"></a><a name="p1012618817121"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1333011651212"><a name="p1333011651212"></a><a name="p1333011651212"></a>End time to run a job. Unit: ms.</p>
</td>
</tr>
<tr id="row186142034131118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p8295135413112"><a name="p8295135413112"></a><a name="p8295135413112"></a>elapsed_time</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1612617841214"><a name="p1612617841214"></a><a name="p1612617841214"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p733061610128"><a name="p733061610128"></a><a name="p733061610128"></a>Running duration of a job. Unit: ms.</p>
</td>
</tr>
<tr id="row6780123481117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p62951654141119"><a name="p62951654141119"></a><a name="p62951654141119"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p51269812128"><a name="p51269812128"></a><a name="p51269812128"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p93301716191220"><a name="p93301716191220"></a><a name="p93301716191220"></a>Running parameter. The parameter contains a maximum of 4,096 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
</td>
</tr>
<tr id="row4950134131116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18295154101116"><a name="p18295154101116"></a><a name="p18295154101116"></a>properties</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p181261986126"><a name="p181261986126"></a><a name="p181261986126"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1133020163121"><a name="p1133020163121"></a><a name="p1133020163121"></a>Configuration parameter, which is used to configure <strong id="b4449156204014"><a name="b4449156204014"></a><a name="b4449156204014"></a>-d</strong> parameters. The parameter contains a maximum of 2,048 characters, excluding special characters such as &gt;&lt;|'`&amp;!\, and can be left blank.</p>
</td>
</tr>
<tr id="row34573461227"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p103136481121"><a name="p103136481121"></a><a name="p103136481121"></a>launcher_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p139311522020"><a name="p139311522020"></a><a name="p139311522020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20244195418212"><a name="p20244195418212"></a><a name="p20244195418212"></a>Launcher job ID</p>
</td>
</tr>
<tr id="row1687919461120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p031334815212"><a name="p031334815212"></a><a name="p031334815212"></a>app_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p149310528220"><a name="p149310528220"></a><a name="p149310528220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1624412541822"><a name="p1624412541822"></a><a name="p1624412541822"></a>Actual job ID.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    None

-   Example response
    -   Example of a successful response

        ```
        {
            "job_detail": {
                "job_id": "431b135e-c090-489f-b1db-0abe3822b855",
                "user": "xxxx",
                "job_name": "pyspark1",
                "job_result": "SUCCEEDED",
                "job_state": "FINISHED",
                "job_progress": 100,
                "job_type": "SparkSubmit",
                "started_time": 1564626578817,
                "submitted_time": 1564626561541,
                "finished_time": 1564626664930,
                "elapsed_time": 86113,
                "queue": "default",
                "arguments": "[--class, org.apache.spark.examples.SparkPi, --driver-memory, 512MB, --num-executors, 1, --executor-cores, 1, --master, yarn-cluster, s3a://obs-test/jobs/spark/spark-examples_2.11-2.1.0.jar, 10000]",
                "launcher_id": "application_1564622673393_0006",
                "app_id": "application_1564622673393_0007",
                "properties": "{}"
            }
        }
        ```

    -   Example of a failed response

        ```
        {
        "error_msg": Failed to query the job.
        "error_code":"0162"
        }
        ```



## Status Code<a name="section4391766619434"></a>

For details about status codes, see  [Status Codes](status-codes.md).

