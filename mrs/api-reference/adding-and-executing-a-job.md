# Adding and Executing a Job<a name="EN-US_TOPIC_0176713997"></a>

## Function<a name="section4408504619327"></a>

This API is used to add and submit a job in an MRS cluster.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   If Kerberos authentication is enabled for a cluster, on the  **Dashboard**  tab page of the cluster details page, click  ![](figures/en-us_image_0218832430.png)  on the right side of  **IAM User Sync**  to synchronize IAM users, and then submit a job through this API.  

## URI<a name="section10186656193217"></a>

-   Format

    POST /v2/\{project\_id\}/clusters/\{cluster\_id\}/job-executions

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
    </tbody>
    </table>


## Request<a name="section673761354213"></a>

**Table  2**  Request parameter description

<a name="table46210785193317"></a>
<table><thead align="left"><tr id="row34262165193317"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12621391193317"><a name="p12621391193317"></a><a name="p12621391193317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p15699711193317"><a name="p15699711193317"></a><a name="p15699711193317"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p562413019313"><a name="p562413019313"></a><a name="p562413019313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p63717051193317"><a name="p63717051193317"></a><a name="p63717051193317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36582554193317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10396884193317"><a name="p10396884193317"></a><a name="p10396884193317"></a>job_type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p36841295193317"><a name="p36841295193317"></a><a name="p36841295193317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p346461129313"><a name="p346461129313"></a><a name="p346461129313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p32476122205057"><a name="p32476122205057"></a><a name="p32476122205057"></a>Type of a job.</p>
<a name="ul5947149515590"></a><a name="ul5947149515590"></a><ul id="ul5947149515590"><li>MapReduce</li><li>SparkSubmit</li><li>HiveScript</li><li>HiveSql</li><li>DistCp, importing and exporting data</li><li>SparkScript</li><li>SparkSql</li><li>Flink</li></ul>
<div class="note" id="note1585635820136"><a name="note1585635820136"></a><a name="note1585635820136"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p18564580135"><a name="p18564580135"></a><a name="p18564580135"></a>Spark, Hive, and Flink jobs can be added to only clusters that include Spark, Hive, and Flink components.</p>
</div></div>
</td>
</tr>
<tr id="row57932449102743"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62016791102743"><a name="p62016791102743"></a><a name="p62016791102743"></a>job_name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p57304145102743"><a name="p57304145102743"></a><a name="p57304145102743"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p277864793547"><a name="p277864793547"></a><a name="p277864793547"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p29070416105535"><a name="p29070416105535"></a><a name="p29070416105535"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
<div class="note" id="note60307154105535"><a name="note60307154105535"></a><a name="note60307154105535"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5893482105535"><a name="p5893482105535"></a><a name="p5893482105535"></a>Identical job names are allowed but not recommended.</p>
</div></div>
</td>
</tr>
<tr id="row4788257010284"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p881779095210"><a name="p881779095210"></a><a name="p881779095210"></a>arguments</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4315240795210"><a name="p4315240795210"></a><a name="p4315240795210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p412027909313"><a name="p412027909313"></a><a name="p412027909313"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p568404895210"><a name="p568404895210"></a><a name="p568404895210"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter.</p>
<p id="p5115643295210"><a name="p5115643295210"></a><a name="p5115643295210"></a>The parameter contains a maximum of 4,096 characters, excluding special characters such as ;|&amp;&gt;'&lt;$, and can be left blank.</p>
<div class="note" id="note62371709174814"><a name="note62371709174814"></a><a name="note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul142809267486"></a><a name="ul142809267486"></a><ul id="ul142809267486"><li>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. When you view job information, sensitive information is displayed as *.<p id="p1265001117571"><a name="p1265001117571"></a><a name="p1265001117571"></a>For example, <strong id="b10929134614184"><a name="b10929134614184"></a><a name="b10929134614184"></a>username=admin @password=admin_123</strong>.</p>
</li><li>For MRS 1.9.2 or later, a file path on OBS can start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue15615586113316"><a name="en-us_topic_0173264852_parmvalue15615586113316"></a><a name="en-us_topic_0173264852_parmvalue15615586113316"></a><b>obs://</b></span>. To use this format to submit HiveScript or HiveSQL jobs, choose <strong id="b2434220398"><a name="b2434220398"></a><a name="b2434220398"></a>Components</strong> &gt; <strong id="b1763919773919"><a name="b1763919773919"></a><a name="b1763919773919"></a>Hive</strong> &gt; <strong id="b196701611143918"><a name="b196701611143918"></a><a name="b196701611143918"></a>Service Configuration</strong> on the cluster details page, set <strong id="b1357785254612"><a name="b1357785254612"></a><a name="b1357785254612"></a>Type</strong> to <strong id="b1359625513464"><a name="b1359625513464"></a><a name="b1359625513464"></a>All</strong>, and search for <strong id="b9417113244716"><a name="b9417113244716"></a><a name="b9417113244716"></a>core.site.customized.configs</strong>. Add the endpoint configuration item (<strong id="b12305124813494"><a name="b12305124813494"></a><a name="b12305124813494"></a>fs.obs.endpoint</strong>) of OBS and enter the endpoint corresponding to OBS in <strong id="b128516045513"><a name="b128516045513"></a><a name="b128516045513"></a>Value</strong>. Obtain the value from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</li></ul>
</div></div>
</td>
</tr>
<tr id="row22945661205631"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p192601412102312"><a name="p192601412102312"></a><a name="p192601412102312"></a>properties</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1525891262313"><a name="p1525891262313"></a><a name="p1525891262313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1425691210231"><a name="p1425691210231"></a><a name="p1425691210231"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p79195218381"><a name="p79195218381"></a><a name="p79195218381"></a>Program system parameter.</p>
<p id="p1725310125238"><a name="p1725310125238"></a><a name="p1725310125238"></a>The parameter contains a maximum of 2,048 characters, excluding special characters such as &gt;&lt;|'`&amp;!\, and can be left blank.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section775516131425"></a>

**Table  3**  Response parameter description

<a name="table12040613193927"></a>
<table><thead align="left"><tr id="row8843854193927"><th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.1"><p id="p45263556193927"><a name="p45263556193927"></a><a name="p45263556193927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.94%" id="mcps1.2.4.1.2"><p id="p1907984993927"><a name="p1907984993927"></a><a name="p1907984993927"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17473879193927"><a name="p17473879193927"></a><a name="p17473879193927"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8387056194027"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p20048170121940"><a name="p20048170121940"></a><a name="p20048170121940"></a>job_submit_result</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p5273559121940"><a name="p5273559121940"></a><a name="p5273559121940"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p27667593121940"><a name="p27667593121940"></a><a name="p27667593121940"></a>Job execution result</p>
</td>
</tr>
<tr id="row124872226276"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p4550133292720"><a name="p4550133292720"></a><a name="p4550133292720"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p19550532162716"><a name="p19550532162716"></a><a name="p19550532162716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p7550132172718"><a name="p7550132172718"></a><a name="p7550132172718"></a>Job ID</p>
</td>
</tr>
<tr id="row81796441245"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p0180104419241"><a name="p0180104419241"></a><a name="p0180104419241"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p181801744152419"><a name="p181801744152419"></a><a name="p181801744152419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p01803442249"><a name="p01803442249"></a><a name="p01803442249"></a>Job submission status.</p>
<a name="ul667222419913"></a><a name="ul667222419913"></a><ul id="ul667222419913"><li>COMPLETE: The job is submitted.</li><li>JOBSTAT_SUBMIT_FAILED: Failed to submit the job.</li></ul>
</td>
</tr>
<tr id="row9408105472718"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p19212192513289"><a name="p19212192513289"></a><a name="p19212192513289"></a>error_msg</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p1540975432715"><a name="p1540975432715"></a><a name="p1540975432715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1040975411278"><a name="p1040975411278"></a><a name="p1040975411278"></a>Error message</p>
</td>
</tr>
<tr id="row893185418272"><td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.1 "><p id="p12931125415277"><a name="p12931125415277"></a><a name="p12931125415277"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.2.4.1.2 "><p id="p15931155452715"><a name="p15931155452715"></a><a name="p15931155452715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p993175492710"><a name="p993175492710"></a><a name="p993175492710"></a>Error code</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1210015461189"></a>

-   Example request

    The following is an example of an MapReduce job request:

    ```
    {
        "job_name":"MapReduceTest",
        "job_type":"MapReduce",
        "arguments":[
            "s3a://obs-test/program/hadoop-mapreduce-examples-x.x.x.jar",
            "wordcount",
            "s3a://obs-test/input/",
            "s3a://obs-test/job/mapreduce/output"
        ],
        "properties":{
            "fs.s3a.endpoint":"obs endpoint",
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

    The following is an example of a SparkSubmit job request:

    ```
    {
        "job_name":"SparkJobTest",
        "job_type":"SparkSubmit",
        "arguments":[
            "--master",
            "yarn",
            "--deploy-mode",
            "cluster",
            "--py-files",
            "s3a://obs-test/a.py",
            "--conf",
            "spark.yarn.appMasterEnv.PYTHONPATH=/tmp:$PYTHONPATH",
            "--conf",
            "spark.yarn.appMasterEnv.aaa=aaaa",
            "--conf",
            "spark.executorEnv.aaa=executoraaa",
            "--properties-file",
            "s3a://obs-test/test-spark.conf",
            "s3a://obs-test/pi.py",
            "100000"
        ],
        "properties":{
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

    The following is an example of a HiveScript job request:

    ```
    {
        "job_name":"HiveScriptTest",
        "job_type":"HiveScript",
        "arguments":[
            "s3a://obs-test/sql/test_script.sql"
        ],
        "properties":{
            "fs.s3a.endpoint":"obs endpoint",
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

    The following is an example of a HiveSQL job request:

    ```
    {
        "job_name":"HiveSqlTest",
        "job_type":"HiveSql",
        "arguments":[
            "DROP TABLE IF EXISTS src_wordcount;create external table src_wordcount(line string);insert into src_wordcount values('v1')"
        ],
        "properties":{
            "fs.s3a.endpoint":"obs endpoint",
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

    The following is an example of a DistCp job request:

    ```
    {
        "job_name":"DistCpTest",
        "job_type":"DistCp",
        "arguments":[
            "s3a://obs-test/DistcpJob/",
            "/user/test/sparksql/"
        ],
        "properties":{
            "fs.s3a.endpoint":"obs endpoint",
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

    The following is an example of a SparkScript job request:

    ```
    {
        "job_type":"SparkSql",
        "job_name":"SparkScriptTest",
        "arguments":[
            "op-key1",
            "op-value1",
            "op-key2",
            "op-value2",
            "s3a://obs-test/sql/test_script.sql"
        ],
        "properties":{
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    } 
    ```

    The following is an example of a SparkSQL job request:

    ```
    {
        "job_type":"SparkSql",
        "job_name":"SparkSqlTest",
        "arguments":[
            "op-key1",
            "op-value1",
            "op-key2",
            "op-value2",
            "create table student_info3 (id string,name string,gender string,age int,addr string);"
        ],
        "properties":{
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    } 
    ```

    The following is an example of a Flink job request:

    ```
    {
        "job_name":"flinkTest",
        "job_type":"Flink",
        "arguments":[
            "run",
            "-d",
            "-ynm",
            "testExcutorejobhdfsbatch",
            "-m",
            "yarn-cluster",
            "hdfs://test/examples/batch/WordCount.jar"
        ],
        "properties":{
            "fs.s3a.endpoint":"obs endpoint",
            "fs.s3a.access.key":"xxx",
            "fs.s3a.secret.key":"yyy"
        }
    }
    ```

-   Example response
    -   Example of a successful response

        ```
        {
          "job_submit_result":{
              "job_id":"44b37a20-ffe8-42b1-b42b-78a5978d7e40",
              "state":"COMPLETE"
          }
        }
        ```

    -   Example of a failed response

        ```
        {
        "error_msg": Hive jobs cannot be submitted.
        "error_code":"0168"
        }
        ```



## Status Code<a name="section4391766619434"></a>

For details about status codes, see  [Status Codes](status-codes.md).

