# Running a HiveSql Job<a name="EN-US_TOPIC_0221415047"></a>

You can submit programs developed by yourself to MRS to execute them, and obtain the results. This section describes how to submit a HiveSql job on the MRS management console. HiveSql jobs are used to submit SQL statements and script files for data query and analysis. Both SQL statements and scripts are supported. If SQL statements contain sensitive information, use SparkScript to submit them.

## Prerequisites<a name="section2335951116026"></a>

You have uploaded the program packages and data files required for running jobs to OBS or HDFS.

## Submitting a Job on the GUI<a name="section75299125395"></a>

1.  Log in to the MRS management console.
2.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
3.  If Kerberos authentication is enabled for the cluster, perform the following steps. If Kerberos authentication is not enabled for the cluster, skip this step.

    In the  **Basic Information**  area on the  **Dashboard**  tab page, click  ![](figures/en-us_image_0226013449.png)  on the right side of  **IAM User Sync**  to synchronize IAM users. For details, see  [Synchronizing IAM Users to MRS](synchronizing-iam-users-to-mrs.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   In the versions earlier than MRS 1.9.2, the job management function is unavailable in a cluster with Kerberos authentication enabled. You need to submit a job in the background.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS Viewer to MRS User, MRS Admin, or MRS Administrator, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated. Then, submit a job. Otherwise, the job may fail to be submitted.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS User, MRS Admin, or MRS Administrator to MRS Viewer, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated.  

4.  Click the  **Jobs**  tab.
5.  Click  **Create**. The  **Create Job**  page is displayed.
6.  Configure job information. 

    -   If the cluster version is MRS 1.9.2 or later, select  **HiveSql**  in  **Type**. Configure other parameters of the SparkSubmit job by referring to  [Table 1](#tf38a01bf69f34c29a25317555fc32b92).
    -   If the cluster version is earlier than MRS 1.9.2, select  **Hive Script**  in  **Type**. Configure Spark job information by referring to  [Table 2](#table19597131417176).

    **Table  1**  Job configuration information

    <a name="tf38a01bf69f34c29a25317555fc32b92"></a>
    <table><thead align="left"><tr id="rfd2a08fd0ba94517ba01e4ded7454cac"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="af11d9c3dce6c499d8eec0a138b99d392"><a name="af11d9c3dce6c499d8eec0a138b99d392"></a><a name="af11d9c3dce6c499d8eec0a138b99d392"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ab83f3f06c8cc46369dd5073ae93c3b97"><a name="ab83f3f06c8cc46369dd5073ae93c3b97"></a><a name="ab83f3f06c8cc46369dd5073ae93c3b97"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r683b3168dd8341798f260d75ab24909c"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="ad2841a7eecfd48b6bc3e616a68292c71"><a name="ad2841a7eecfd48b6bc3e616a68292c71"></a><a name="ad2841a7eecfd48b6bc3e616a68292c71"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p18545319122216"><a name="p18545319122216"></a><a name="p18545319122216"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    <div class="note" id="note163999410228"><a name="note163999410228"></a><a name="note163999410228"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173264852_p123692397276"><a name="en-us_topic_0173264852_p123692397276"></a><a name="en-us_topic_0173264852_p123692397276"></a>You are advised to set different names for different jobs.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row196696374412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1867063114410"><a name="p1867063114410"></a><a name="p1867063114410"></a>SQL Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p06701364418"><a name="p06701364418"></a><a name="p06701364418"></a>Submission type of the SQL statement</p>
    <a name="ul2672431204511"></a><a name="ul2672431204511"></a><ul id="ul2672431204511"><li>SQL</li><li>Script</li></ul>
    </td>
    </tr>
    <tr id="row146350174618"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1863208460"><a name="p1863208460"></a><a name="p1863208460"></a>SQL Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p36370194614"><a name="p36370194614"></a><a name="p36370194614"></a>This parameter is valid only when <span class="parmname" id="parmname1481912464617"><a name="parmname1481912464617"></a><a name="parmname1481912464617"></a><b>SQL Type</b></span> is set to <span class="parmvalue" id="parmvalue17647183144620"><a name="parmvalue17647183144620"></a><a name="parmvalue17647183144620"></a><b>SQL</b></span>. Enter the SQL statement to be executed, and then click <span class="parmvalue" id="parmvalue10920547498"><a name="parmvalue10920547498"></a><a name="parmvalue10920547498"></a><b>Check</b></span> to check whether the SQL statement is correct. If you want to submit and execute multiple statements at the same time, use semicolons (;) to separate them.</p>
    </td>
    </tr>
    <tr id="rbd79ceb2feb141ff9cb37ffde9e08ed7"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a4e9842e891a449118c2e3811caa071d9"><a name="a4e9842e891a449118c2e3811caa071d9"></a><a name="a4e9842e891a449118c2e3811caa071d9"></a>SQL File</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p11270101864711"><a name="p11270101864711"></a><a name="p11270101864711"></a>This parameter is valid only when <span class="parmname" id="parmname112719181471"><a name="parmname112719181471"></a><a name="parmname112719181471"></a><b>SQL Type</b></span> is set to <span class="parmvalue" id="parmvalue12296102615473"><a name="parmvalue12296102615473"></a><a name="parmvalue12296102615473"></a><b>Script</b></span>. The path of the SQL file to be executed must meet the following requirements:</p>
    <a name="ul1375493195654"></a><a name="ul1375493195654"></a><ul id="ul1375493195654"><li>Contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The parameter value cannot be empty or full of spaces.</li><li>The path of the program to be executed can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul193701439132718"></a><a name="en-us_topic_0173264852_ul193701439132718"></a><ul id="en-us_topic_0173264852_ul193701439132718"><li>OBS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue31990530182"><a name="en-us_topic_0173264852_parmvalue31990530182"></a><a name="en-us_topic_0173264852_parmvalue31990530182"></a><b>s3a://</b></span>. Example: <strong id="en-us_topic_0173264852_b050143852311"><a name="en-us_topic_0173264852_b050143852311"></a><a name="en-us_topic_0173264852_b050143852311"></a>s3a://wordcount/program/<em id="en-us_topic_0173264852_i2021313439231"><a name="en-us_topic_0173264852_i2021313439231"></a><a name="en-us_topic_0173264852_i2021313439231"></a>xxx</em>.jar</strong></li><li>HDFS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue828144432312"><a name="en-us_topic_0173264852_parmvalue828144432312"></a><a name="en-us_topic_0173264852_parmvalue828144432312"></a><b>/user</b></span>.</li></ul>
    </li><li>For SparkScript and HiveScript, the path must end with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue037073911277"><a name="en-us_topic_0173264852_parmvalue037073911277"></a><a name="en-us_topic_0173264852_parmvalue037073911277"></a><b>.sql</b></span>. For MapReduce, the path must end with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue3370173972716"><a name="en-us_topic_0173264852_parmvalue3370173972716"></a><a name="en-us_topic_0173264852_parmvalue3370173972716"></a><b>.jar</b></span>. For Flink and SparkSubmit, the path must end with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue0370123910279"><a name="en-us_topic_0173264852_parmvalue0370123910279"></a><a name="en-us_topic_0173264852_parmvalue0370123910279"></a><b>.jar</b></span> or <span class="parmvalue" id="en-us_topic_0173264852_parmvalue6370739122720"><a name="en-us_topic_0173264852_parmvalue6370739122720"></a><a name="en-us_topic_0173264852_parmvalue6370739122720"></a><b>.py</b></span>. The <strong id="en-us_topic_0173264852_b1035885403218"><a name="en-us_topic_0173264852_b1035885403218"></a><a name="en-us_topic_0173264852_b1035885403218"></a>.sql</strong>, <strong id="en-us_topic_0173264852_b1236010543320"><a name="en-us_topic_0173264852_b1236010543320"></a><a name="en-us_topic_0173264852_b1236010543320"></a>.jar</strong>, and <strong id="en-us_topic_0173264852_b5194114113312"><a name="en-us_topic_0173264852_b5194114113312"></a><a name="en-us_topic_0173264852_b5194114113312"></a>.py</strong> are case-insensitive.</li></ul>
    </td>
    </tr>
    <tr id="row7582163653214"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1527715406327"><a name="p1527715406327"></a><a name="p1527715406327"></a>Service Parameter</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p0595819249"><a name="p0595819249"></a><a name="p0595819249"></a>This parameter is optional. It is used to modify service parameters for the job. The parameter modification applies only to the current job. To make the modification take effect permanently for the cluster, follow instructions in <a href="configuring-service-parameters.md">Configuring Service Parameters</a>.</p>
    <p id="p1793619348256"><a name="p1793619348256"></a><a name="p1793619348256"></a>To add multiple parameters, click <a name="image2755173901018"></a><a name="image2755173901018"></a><span><img id="image2755173901018" src="figures/en-us_image_0226013700.png"></span> on the right. To delete a parameter, click <span class="parmvalue" id="en-us_topic_0173264852_parmvalue163711139122718"><a name="en-us_topic_0173264852_parmvalue163711139122718"></a><a name="en-us_topic_0173264852_parmvalue163711139122718"></a><b>Delete</b></span> on the right.</p>
    </td>
    </tr>
    <tr id="row17661172893316"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p10661142818337"><a name="p10661142818337"></a><a name="p10661142818337"></a>Command Reference</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p204063412410"><a name="p204063412410"></a><a name="p204063412410"></a>Command submitted to the background for execution when a job is submitted</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Job configuration information

    <a name="table19597131417176"></a>
    <table><thead align="left"><tr id="en-us_topic_0173264852_rfd2a08fd0ba94517ba01e4ded7454cac"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="en-us_topic_0173264852_af11d9c3dce6c499d8eec0a138b99d392"><a name="en-us_topic_0173264852_af11d9c3dce6c499d8eec0a138b99d392"></a><a name="en-us_topic_0173264852_af11d9c3dce6c499d8eec0a138b99d392"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="en-us_topic_0173264852_ab83f3f06c8cc46369dd5073ae93c3b97"><a name="en-us_topic_0173264852_ab83f3f06c8cc46369dd5073ae93c3b97"></a><a name="en-us_topic_0173264852_ab83f3f06c8cc46369dd5073ae93c3b97"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0173264852_row16309131791918"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_p1931011715198"><a name="en-us_topic_0173264852_p1931011715198"></a><a name="en-us_topic_0173264852_p1931011715198"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_p1267051812192"><a name="en-us_topic_0173264852_p1267051812192"></a><a name="en-us_topic_0173264852_p1267051812192"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    <div class="note" id="en-us_topic_0173264852_note067018184197"><a name="en-us_topic_0173264852_note067018184197"></a><a name="en-us_topic_0173264852_note067018184197"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173264852_p1167017186195"><a name="en-us_topic_0173264852_p1167017186195"></a><a name="en-us_topic_0173264852_p1167017186195"></a>You are advised to set different names for different jobs.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0173264852_rbd79ceb2feb141ff9cb37ffde9e08ed7"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_a4e9842e891a449118c2e3811caa071d9"><a name="en-us_topic_0173264852_a4e9842e891a449118c2e3811caa071d9"></a><a name="en-us_topic_0173264852_a4e9842e891a449118c2e3811caa071d9"></a>Program Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_p655627719565"><a name="en-us_topic_0173264852_p655627719565"></a><a name="en-us_topic_0173264852_p655627719565"></a>Path of the program package to be executed. The following requirements must be met:</p>
    <a name="en-us_topic_0173264852_ul1375493195654"></a><a name="en-us_topic_0173264852_ul1375493195654"></a><ul id="en-us_topic_0173264852_ul1375493195654"><li>Contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The parameter value cannot be empty or full of spaces.</li><li>The path of the program to be executed can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul56833471484"></a><a name="en-us_topic_0173264852_ul56833471484"></a><ul id="en-us_topic_0173264852_ul56833471484"><li>OBS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue169753526119"><a name="en-us_topic_0173264852_parmvalue169753526119"></a><a name="en-us_topic_0173264852_parmvalue169753526119"></a><b>s3a://</b></span>. Example: <strong id="en-us_topic_0173264852_b520316541210"><a name="en-us_topic_0173264852_b520316541210"></a><a name="en-us_topic_0173264852_b520316541210"></a>s3a://wordcount/program/<em id="en-us_topic_0173264852_i1620265419116"><a name="en-us_topic_0173264852_i1620265419116"></a><a name="en-us_topic_0173264852_i1620265419116"></a>xxx</em>.jar</strong></li><li>HDFS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue2097714552014"><a name="en-us_topic_0173264852_parmvalue2097714552014"></a><a name="en-us_topic_0173264852_parmvalue2097714552014"></a><b>/user</b></span>.</li></ul>
    </li><li>For SparkScript, the path must end with <strong id="en-us_topic_0173264852_b4516016217"><a name="en-us_topic_0173264852_b4516016217"></a><a name="en-us_topic_0173264852_b4516016217"></a>.sql</strong>. For MapReduce and Spark, the path must end with <strong id="en-us_topic_0173264852_b8517191929"><a name="en-us_topic_0173264852_b8517191929"></a><a name="en-us_topic_0173264852_b8517191929"></a>.jar</strong>. The <strong id="en-us_topic_0173264852_b8623134020214"><a name="en-us_topic_0173264852_b8623134020214"></a><a name="en-us_topic_0173264852_b8623134020214"></a>.sql</strong> and <strong id="en-us_topic_0173264852_b6625540626"><a name="en-us_topic_0173264852_b6625540626"></a><a name="en-us_topic_0173264852_b6625540626"></a>.jar</strong> are case-insensitive.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0173264852_r7dcde55c00da4bc88afb2b022bce0abd"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_a61afb54329564e458086d7622bda3b89"><a name="en-us_topic_0173264852_a61afb54329564e458086d7622bda3b89"></a><a name="en-us_topic_0173264852_a61afb54329564e458086d7622bda3b89"></a>Parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_ad6f1110b8e38456193949182f7a05980"><a name="en-us_topic_0173264852_ad6f1110b8e38456193949182f7a05980"></a><a name="en-us_topic_0173264852_ad6f1110b8e38456193949182f7a05980"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter. Multiple parameters are separated by space.</p>
    <p id="en-us_topic_0173264852_p163988156203"><a name="en-us_topic_0173264852_p163988156203"></a><a name="en-us_topic_0173264852_p163988156203"></a>Configuration method: <em id="en-us_topic_0173264852_i19190195834"><a name="en-us_topic_0173264852_i19190195834"></a><a name="en-us_topic_0173264852_i19190195834"></a>Package name</em>.<em id="en-us_topic_0173264852_i171411411336"><a name="en-us_topic_0173264852_i171411411336"></a><a name="en-us_topic_0173264852_i171411411336"></a>Class name</em></p>
    <p id="en-us_topic_0173264852_a6c44712b37c74651afe354f3cbf9e02f"><a name="en-us_topic_0173264852_a6c44712b37c74651afe354f3cbf9e02f"></a><a name="en-us_topic_0173264852_a6c44712b37c74651afe354f3cbf9e02f"></a>The parameter contains a maximum of 2,047 characters, excluding special characters such as ;|&amp;&gt;&lt;'$, and can be left blank.</p>
    <div class="note" id="en-us_topic_0173264852_note62371709174814"><a name="en-us_topic_0173264852_note62371709174814"></a><a name="en-us_topic_0173264852_note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173264852_p20521095174814"><a name="en-us_topic_0173264852_p20521095174814"></a><a name="en-us_topic_0173264852_p20521095174814"></a>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. When you view job information on the MRS management console, the sensitive information is displayed as <strong id="en-us_topic_0173264852_b4931524432"><a name="en-us_topic_0173264852_b4931524432"></a><a name="en-us_topic_0173264852_b4931524432"></a>*</strong>.</p>
    <p id="en-us_topic_0173264852_p1265001117571"><a name="en-us_topic_0173264852_p1265001117571"></a><a name="en-us_topic_0173264852_p1265001117571"></a>Example: <strong id="en-us_topic_0173264852_b67512611320"><a name="en-us_topic_0173264852_b67512611320"></a><a name="en-us_topic_0173264852_b67512611320"></a>username=admin @password=admin_123</strong></p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0173264852_r3bdfdc9102e8416492da92bb5912306e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_a93b1caabf748429b887fe55580d1db95"><a name="en-us_topic_0173264852_a93b1caabf748429b887fe55580d1db95"></a><a name="en-us_topic_0173264852_a93b1caabf748429b887fe55580d1db95"></a>Import from</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_a52221b5791d44544af1d6daf2bb57612"><a name="en-us_topic_0173264852_a52221b5791d44544af1d6daf2bb57612"></a><a name="en-us_topic_0173264852_a52221b5791d44544af1d6daf2bb57612"></a>Path for inputting data</p>
    <div class="p" id="en-us_topic_0173264852_p6028322915823"><a name="en-us_topic_0173264852_p6028322915823"></a><a name="en-us_topic_0173264852_p6028322915823"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul1668690715439"></a><a name="en-us_topic_0173264852_ul1668690715439"></a><ul id="en-us_topic_0173264852_ul1668690715439"><li>OBS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue79225162123"><a name="en-us_topic_0173264852_parmvalue79225162123"></a><a name="en-us_topic_0173264852_parmvalue79225162123"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue20387040111217"><a name="en-us_topic_0173264852_parmvalue20387040111217"></a><a name="en-us_topic_0173264852_parmvalue20387040111217"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="en-us_topic_0173264852_a8c411087de5a4952a0a0763536c2fd4a"><a name="en-us_topic_0173264852_a8c411087de5a4952a0a0763536c2fd4a"></a><a name="en-us_topic_0173264852_a8c411087de5a4952a0a0763536c2fd4a"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0173264852_r26ccf29d38884d09b5b2c445f49e3f0a"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_en-us_topic_0012807343_p752552114273"><a name="en-us_topic_0173264852_en-us_topic_0012807343_p752552114273"></a><a name="en-us_topic_0173264852_en-us_topic_0012807343_p752552114273"></a>Export to</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_af95377875ef1449db585f0d23bdc5096"><a name="en-us_topic_0173264852_af95377875ef1449db585f0d23bdc5096"></a><a name="en-us_topic_0173264852_af95377875ef1449db585f0d23bdc5096"></a>Path for outputting data</p>
    <div class="note" id="en-us_topic_0173264852_note12918618161337"><a name="en-us_topic_0173264852_note12918618161337"></a><a name="en-us_topic_0173264852_note12918618161337"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0173264852_ul1637410244522"></a><a name="en-us_topic_0173264852_ul1637410244522"></a><ul id="en-us_topic_0173264852_ul1637410244522"><li>When setting this parameter, select <strong id="en-us_topic_0173264852_b68401030101311"><a name="en-us_topic_0173264852_b68401030101311"></a><a name="en-us_topic_0173264852_b68401030101311"></a>OBS</strong> or <strong id="en-us_topic_0173264852_b584263061315"><a name="en-us_topic_0173264852_b584263061315"></a><a name="en-us_topic_0173264852_b584263061315"></a>HDFS</strong>. Select a file directory or manually enter a file directory, and click <strong id="en-us_topic_0173264852_b58462030191317"><a name="en-us_topic_0173264852_b58462030191317"></a><a name="en-us_topic_0173264852_b58462030191317"></a>OK</strong>.</li><li>If you add the <strong id="en-us_topic_0173264852_b1059351631410"><a name="en-us_topic_0173264852_b1059351631410"></a><a name="en-us_topic_0173264852_b1059351631410"></a>hadoop-mapreduce-examples-x.x.x.jar</strong> sample program or a program similar to <strong id="en-us_topic_0173264852_b19594191681417"><a name="en-us_topic_0173264852_b19594191681417"></a><a name="en-us_topic_0173264852_b19594191681417"></a>hadoop-mapreduce-examples-x.x.x.jar</strong>, enter a directory that does not exist.</li></ul>
    </div></div>
    <div class="p" id="en-us_topic_0173264852_p60582415151053"><a name="en-us_topic_0173264852_p60582415151053"></a><a name="en-us_topic_0173264852_p60582415151053"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul8370831151053"></a><a name="en-us_topic_0173264852_ul8370831151053"></a><ul id="en-us_topic_0173264852_ul8370831151053"><li>OBS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue1206143641411"><a name="en-us_topic_0173264852_parmvalue1206143641411"></a><a name="en-us_topic_0173264852_parmvalue1206143641411"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue380018372148"><a name="en-us_topic_0173264852_parmvalue380018372148"></a><a name="en-us_topic_0173264852_parmvalue380018372148"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="en-us_topic_0173264852_aece1cf44e4734f94b3196ff9e9bf38e8"><a name="en-us_topic_0173264852_aece1cf44e4734f94b3196ff9e9bf38e8"></a><a name="en-us_topic_0173264852_aece1cf44e4734f94b3196ff9e9bf38e8"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0173264852_rff1753bde96f4e81a0631197ac349003"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0173264852_en-us_topic_0012807343_p287101489174"><a name="en-us_topic_0173264852_en-us_topic_0012807343_p287101489174"></a><a name="en-us_topic_0173264852_en-us_topic_0012807343_p287101489174"></a>Log Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0173264852_a2bcc88a179f346448d93d0da091aa47f"><a name="en-us_topic_0173264852_a2bcc88a179f346448d93d0da091aa47f"></a><a name="en-us_topic_0173264852_a2bcc88a179f346448d93d0da091aa47f"></a>Path for storing job logs that record job running status.</p>
    <div class="p" id="en-us_topic_0173264852_p52515849151155"><a name="en-us_topic_0173264852_p52515849151155"></a><a name="en-us_topic_0173264852_p52515849151155"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul2880601151155"></a><a name="en-us_topic_0173264852_ul2880601151155"></a><ul id="en-us_topic_0173264852_ul2880601151155"><li>OBS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue7427033171520"><a name="en-us_topic_0173264852_parmvalue7427033171520"></a><a name="en-us_topic_0173264852_parmvalue7427033171520"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="en-us_topic_0173264852_parmvalue12222237111519"><a name="en-us_topic_0173264852_parmvalue12222237111519"></a><a name="en-us_topic_0173264852_parmvalue12222237111519"></a><b>/user</b></span>.</li></ul>
    </div>
    <p id="en-us_topic_0173264852_en-us_topic_0012807343_p438206609174"><a name="en-us_topic_0173264852_en-us_topic_0012807343_p438206609174"></a><a name="en-us_topic_0173264852_en-us_topic_0012807343_p438206609174"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Confirm job configuration information and click  **OK**.

    After the job is created, you can manage it.


