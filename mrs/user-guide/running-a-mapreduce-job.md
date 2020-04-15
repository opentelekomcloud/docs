# Running a MapReduce Job<a name="EN-US_TOPIC_0221415045"></a>

You can submit programs developed by yourself to MRS to execute them, and obtain the results. This section describes how to submit a MapReduce job on the MRS management console. MapReduce jobs are used to submit JAR programs to quickly process massive amounts of data in parallel and create a distributed data processing and execution environment.

If the job and file management functions are not supported on the cluster details page, submit the jobs in the background.

## Prerequisites<a name="section2335951116026"></a>

You have uploaded the program packages and data files required for running jobs to OBS or HDFS.

## Submitting a Job on the GUI<a name="section75299125395"></a>

1.  Log in to the MRS management console.
2.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
3.  If Kerberos authentication is enabled for the cluster, perform the following steps. If Kerberos authentication is not enabled for the cluster, skip this step.

    In the  **Basic Information**  area on the  **Dashboard**  tab page, click  ![](figures/en-us_image_0226013652.png)  on the right side of  **IAM User Sync**  to synchronize IAM users. For details, see  [Synchronizing IAM Users to MRS](synchronizing-iam-users-to-mrs.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   In the versions earlier than MRS 1.9.2, the job management function is unavailable in a cluster with Kerberos authentication enabled. You need to submit a job in the background.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS Viewer to MRS User, MRS Admin, or MRS Administrator, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated. Then, submit a job. Otherwise, the job may fail to be submitted.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS User, MRS Admin, or MRS Administrator to MRS Viewer, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated.  

4.  Click the  **Jobs**  tab.
5.  Click  **Create**. The  **Create Job**  page is displayed.
6.  In  **Type**, select  **MapReduce**. Configure other job information.
    -   If the cluster version is MRS 1.9.2 or later, configure MapReduce job information by referring to  [Table 1](#table2037463920278).
    -   If the cluster version is earlier than MRS 1.9.2, configure MapReduce job information by referring to  [Table 2](#tf38a01bf69f34c29a25317555fc32b92).

        **Table  1**  Job configuration information

        <a name="table2037463920278"></a>
        <table><thead align="left"><tr id="row8368193916278"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p83681839192713"><a name="p83681839192713"></a><a name="p83681839192713"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p18368639102711"><a name="p18368639102711"></a><a name="p18368639102711"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row6369739112710"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p203691739132714"><a name="p203691739132714"></a><a name="p203691739132714"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1936983952719"><a name="p1936983952719"></a><a name="p1936983952719"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
        <div class="note" id="note1736953911274"><a name="note1736953911274"></a><a name="note1736953911274"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p123692397276"><a name="p123692397276"></a><a name="p123692397276"></a>You are advised to set different names for different jobs.</p>
        </div></div>
        </td>
        </tr>
        <tr id="row1837003922716"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p237013952717"><a name="p237013952717"></a><a name="p237013952717"></a>Program Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p137013972712"><a name="p137013972712"></a><a name="p137013972712"></a>Path of the program package to be executed. The following requirements must be met:</p>
        <a name="ul33700396271"></a><a name="ul33700396271"></a><ul id="ul33700396271"><li>Contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The parameter value cannot be empty or full of spaces.</li><li>The path of the program to be executed can be stored in HDFS or OBS. The path varies depending on the file system.<a name="ul193701439132718"></a><a name="ul193701439132718"></a><ul id="ul193701439132718"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue31990530182"><a name="parmvalue31990530182"></a><a name="parmvalue31990530182"></a><b>s3a://</b></span>. Example: <strong id="b050143852311"><a name="b050143852311"></a><a name="b050143852311"></a>s3a://wordcount/program/<em id="i2021313439231"><a name="i2021313439231"></a><a name="i2021313439231"></a>xxx</em>.jar</strong></li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue828144432312"><a name="parmvalue828144432312"></a><a name="parmvalue828144432312"></a><b>/user</b></span>.</li></ul>
        </li><li>For SparkScript and HiveScript, the path must end with <span class="parmvalue" id="parmvalue037073911277"><a name="parmvalue037073911277"></a><a name="parmvalue037073911277"></a><b>.sql</b></span>. For MapReduce, the path must end with <span class="parmvalue" id="parmvalue3370173972716"><a name="parmvalue3370173972716"></a><a name="parmvalue3370173972716"></a><b>.jar</b></span>. For Flink and SparkSubmit, the path must end with <span class="parmvalue" id="parmvalue0370123910279"><a name="parmvalue0370123910279"></a><a name="parmvalue0370123910279"></a><b>.jar</b></span> or <span class="parmvalue" id="parmvalue6370739122720"><a name="parmvalue6370739122720"></a><a name="parmvalue6370739122720"></a><b>.py</b></span>. The <strong id="b1035885403218"><a name="b1035885403218"></a><a name="b1035885403218"></a>.sql</strong>, <strong id="b1236010543320"><a name="b1236010543320"></a><a name="b1236010543320"></a>.jar</strong>, and <strong id="b5194114113312"><a name="b5194114113312"></a><a name="b5194114113312"></a>.py</strong> are case-insensitive.</li></ul>
        </td>
        </tr>
        <tr id="row43711339142713"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p33700398274"><a name="p33700398274"></a><a name="p33700398274"></a>Parameters</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p237043962711"><a name="p237043962711"></a><a name="p237043962711"></a>Key parameters for program execution. Multiple parameters are separated by space.</p>
        <p id="p93716393271"><a name="p93716393271"></a><a name="p93716393271"></a>Configuration method: <em id="i202952404363"><a name="i202952404363"></a><a name="i202952404363"></a>Program class name</em> <em id="i1317184610366"><a name="i1317184610366"></a><a name="i1317184610366"></a>Data input path</em> <em id="i1644475013617"><a name="i1644475013617"></a><a name="i1644475013617"></a>Data output path</em></p>
        <a name="ul63716398279"></a><a name="ul63716398279"></a><ul id="ul63716398279"><li>Program class name: It is specified by a function in your program. MRS is responsible for transferring parameters only.</li><li>Data input path: Click HDFS or OBS to select a path.</li><li>Data output path: Enter a directory that does not exist.</li></ul>
        <p id="p12371113910275"><a name="p12371113910275"></a><a name="p12371113910275"></a>The parameter contains a maximum of 2,047 characters, excluding special characters such as ;|&amp;&gt;&lt;'$, and can be left blank.</p>
        <div class="note" id="note1437118396278"><a name="note1437118396278"></a><a name="note1437118396278"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p13371153962714"><a name="p13371153962714"></a><a name="p13371153962714"></a>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. When you view job information on the MRS management console, the sensitive information is displayed as <strong id="b44915446407"><a name="b44915446407"></a><a name="b44915446407"></a>*</strong>.</p>
        <p id="p33712039172711"><a name="p33712039172711"></a><a name="p33712039172711"></a>Example: <strong id="b217811412417"><a name="b217811412417"></a><a name="b217811412417"></a>username=admin @password=admin_123</strong></p>
        </div></div>
        </td>
        </tr>
        <tr id="row203713398279"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p17371939172710"><a name="p17371939172710"></a><a name="p17371939172710"></a>Service Parameter</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4371163914272"><a name="p4371163914272"></a><a name="p4371163914272"></a>This parameter is optional. It is used to modify service parameters for the job. The parameter modification applies only to the current job. To make the modification take effect permanently for the cluster, follow instructions in <a href="configuring-service-parameters.md">Configuring Service Parameters</a>.</p>
        <p id="p15371139132712"><a name="p15371139132712"></a><a name="p15371139132712"></a>To add multiple parameters, click <a name="image177776216108"></a><a name="image177776216108"></a><span><img id="image177776216108" src="figures/en-us_image_0226013676.png"></span> on the right. To delete a parameter, click <span class="parmvalue" id="parmvalue163711139122718"><a name="parmvalue163711139122718"></a><a name="parmvalue163711139122718"></a><b>Delete</b></span> on the right.</p>
        </td>
        </tr>
        <tr id="row9373839142712"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p12373339132716"><a name="p12373339132716"></a><a name="p12373339132716"></a>Command Reference</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p7373193992711"><a name="p7373193992711"></a><a name="p7373193992711"></a>Command submitted to the background for execution when a job is submitted</p>
        </td>
        </tr>
        </tbody>
        </table>

        **Table  2**  Job configuration information

        <a name="tf38a01bf69f34c29a25317555fc32b92"></a>
        <table><thead align="left"><tr id="rfd2a08fd0ba94517ba01e4ded7454cac"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="af11d9c3dce6c499d8eec0a138b99d392"><a name="af11d9c3dce6c499d8eec0a138b99d392"></a><a name="af11d9c3dce6c499d8eec0a138b99d392"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ab83f3f06c8cc46369dd5073ae93c3b97"><a name="ab83f3f06c8cc46369dd5073ae93c3b97"></a><a name="ab83f3f06c8cc46369dd5073ae93c3b97"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row16309131791918"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1931011715198"><a name="p1931011715198"></a><a name="p1931011715198"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1267051812192"><a name="p1267051812192"></a><a name="p1267051812192"></a>Job name. It contains 1 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
        <div class="note" id="note067018184197"><a name="note067018184197"></a><a name="note067018184197"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1167017186195"><a name="p1167017186195"></a><a name="p1167017186195"></a>You are advised to set different names for different jobs.</p>
        </div></div>
        </td>
        </tr>
        <tr id="rbd79ceb2feb141ff9cb37ffde9e08ed7"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a4e9842e891a449118c2e3811caa071d9"><a name="a4e9842e891a449118c2e3811caa071d9"></a><a name="a4e9842e891a449118c2e3811caa071d9"></a>Program Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p655627719565"><a name="p655627719565"></a><a name="p655627719565"></a>Path of the program package to be executed. The following requirements must be met:</p>
        <a name="ul1375493195654"></a><a name="ul1375493195654"></a><ul id="ul1375493195654"><li>Contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The parameter value cannot be empty or full of spaces.</li><li>The path of the program to be executed can be stored in HDFS or OBS. The path varies depending on the file system.<a name="ul56833471484"></a><a name="ul56833471484"></a><ul id="ul56833471484"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue169753526119"><a name="parmvalue169753526119"></a><a name="parmvalue169753526119"></a><b>s3a://</b></span>. Example: <strong id="b520316541210"><a name="b520316541210"></a><a name="b520316541210"></a>s3a://wordcount/program/<em id="i1620265419116"><a name="i1620265419116"></a><a name="i1620265419116"></a>xxx</em>.jar</strong></li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue2097714552014"><a name="parmvalue2097714552014"></a><a name="parmvalue2097714552014"></a><b>/user</b></span>.</li></ul>
        </li><li>For SparkScript, the path must end with <strong id="b4516016217"><a name="b4516016217"></a><a name="b4516016217"></a>.sql</strong>. For MapReduce and Spark, the path must end with <strong id="b8517191929"><a name="b8517191929"></a><a name="b8517191929"></a>.jar</strong>. The <strong id="b8623134020214"><a name="b8623134020214"></a><a name="b8623134020214"></a>.sql</strong> and <strong id="b6625540626"><a name="b6625540626"></a><a name="b6625540626"></a>.jar</strong> are case-insensitive.</li></ul>
        </td>
        </tr>
        <tr id="r7dcde55c00da4bc88afb2b022bce0abd"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a61afb54329564e458086d7622bda3b89"><a name="a61afb54329564e458086d7622bda3b89"></a><a name="a61afb54329564e458086d7622bda3b89"></a>Parameters</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="ad6f1110b8e38456193949182f7a05980"><a name="ad6f1110b8e38456193949182f7a05980"></a><a name="ad6f1110b8e38456193949182f7a05980"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter. Multiple parameters are separated by space.</p>
        <p id="p163988156203"><a name="p163988156203"></a><a name="p163988156203"></a>Configuration method: <em id="i19190195834"><a name="i19190195834"></a><a name="i19190195834"></a>Package name</em>.<em id="i171411411336"><a name="i171411411336"></a><a name="i171411411336"></a>Class name</em></p>
        <p id="a6c44712b37c74651afe354f3cbf9e02f"><a name="a6c44712b37c74651afe354f3cbf9e02f"></a><a name="a6c44712b37c74651afe354f3cbf9e02f"></a>The parameter contains a maximum of 2,047 characters, excluding special characters such as ;|&amp;&gt;&lt;'$, and can be left blank.</p>
        <div class="note" id="note62371709174814"><a name="note62371709174814"></a><a name="note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p20521095174814"><a name="p20521095174814"></a><a name="p20521095174814"></a>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. When you view job information on the MRS management console, the sensitive information is displayed as <strong id="b4931524432"><a name="b4931524432"></a><a name="b4931524432"></a>*</strong>.</p>
        <p id="p1265001117571"><a name="p1265001117571"></a><a name="p1265001117571"></a>Example: <strong id="b67512611320"><a name="b67512611320"></a><a name="b67512611320"></a>username=admin @password=admin_123</strong></p>
        </div></div>
        </td>
        </tr>
        <tr id="r3bdfdc9102e8416492da92bb5912306e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a93b1caabf748429b887fe55580d1db95"><a name="a93b1caabf748429b887fe55580d1db95"></a><a name="a93b1caabf748429b887fe55580d1db95"></a>Import from</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a52221b5791d44544af1d6daf2bb57612"><a name="a52221b5791d44544af1d6daf2bb57612"></a><a name="a52221b5791d44544af1d6daf2bb57612"></a>Path for inputting data</p>
        <div class="p" id="p6028322915823"><a name="p6028322915823"></a><a name="p6028322915823"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="ul1668690715439"></a><a name="ul1668690715439"></a><ul id="ul1668690715439"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue79225162123"><a name="parmvalue79225162123"></a><a name="parmvalue79225162123"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue20387040111217"><a name="parmvalue20387040111217"></a><a name="parmvalue20387040111217"></a><b>/user</b></span>.</li></ul>
        </div>
        <p id="a8c411087de5a4952a0a0763536c2fd4a"><a name="a8c411087de5a4952a0a0763536c2fd4a"></a><a name="a8c411087de5a4952a0a0763536c2fd4a"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
        </td>
        </tr>
        <tr id="r26ccf29d38884d09b5b2c445f49e3f0a"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0012807343_p752552114273"><a name="en-us_topic_0012807343_p752552114273"></a><a name="en-us_topic_0012807343_p752552114273"></a>Export to</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="af95377875ef1449db585f0d23bdc5096"><a name="af95377875ef1449db585f0d23bdc5096"></a><a name="af95377875ef1449db585f0d23bdc5096"></a>Path for outputting data</p>
        <div class="note" id="note12918618161337"><a name="note12918618161337"></a><a name="note12918618161337"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1637410244522"></a><a name="ul1637410244522"></a><ul id="ul1637410244522"><li>When setting this parameter, select <strong id="b68401030101311"><a name="b68401030101311"></a><a name="b68401030101311"></a>OBS</strong> or <strong id="b584263061315"><a name="b584263061315"></a><a name="b584263061315"></a>HDFS</strong>. Select a file directory or manually enter a file directory, and click <strong id="b58462030191317"><a name="b58462030191317"></a><a name="b58462030191317"></a>OK</strong>.</li><li>If you add the <strong id="b1059351631410"><a name="b1059351631410"></a><a name="b1059351631410"></a>hadoop-mapreduce-examples-x.x.x.jar</strong> sample program or a program similar to <strong id="b19594191681417"><a name="b19594191681417"></a><a name="b19594191681417"></a>hadoop-mapreduce-examples-x.x.x.jar</strong>, enter a directory that does not exist.</li></ul>
        </div></div>
        <div class="p" id="p60582415151053"><a name="p60582415151053"></a><a name="p60582415151053"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="ul8370831151053"></a><a name="ul8370831151053"></a><ul id="ul8370831151053"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue1206143641411"><a name="parmvalue1206143641411"></a><a name="parmvalue1206143641411"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue380018372148"><a name="parmvalue380018372148"></a><a name="parmvalue380018372148"></a><b>/user</b></span>.</li></ul>
        </div>
        <p id="aece1cf44e4734f94b3196ff9e9bf38e8"><a name="aece1cf44e4734f94b3196ff9e9bf38e8"></a><a name="aece1cf44e4734f94b3196ff9e9bf38e8"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
        </td>
        </tr>
        <tr id="rff1753bde96f4e81a0631197ac349003"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0012807343_p287101489174"><a name="en-us_topic_0012807343_p287101489174"></a><a name="en-us_topic_0012807343_p287101489174"></a>Log Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a2bcc88a179f346448d93d0da091aa47f"><a name="a2bcc88a179f346448d93d0da091aa47f"></a><a name="a2bcc88a179f346448d93d0da091aa47f"></a>Path for storing job logs that record job running status.</p>
        <div class="p" id="p52515849151155"><a name="p52515849151155"></a><a name="p52515849151155"></a>Data can be stored in HDFS or OBS. The path varies depending on the file system.<a name="ul2880601151155"></a><a name="ul2880601151155"></a><ul id="ul2880601151155"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue7427033171520"><a name="parmvalue7427033171520"></a><a name="parmvalue7427033171520"></a><b>s3a://</b></span>.</li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue12222237111519"><a name="parmvalue12222237111519"></a><a name="parmvalue12222237111519"></a><b>/user</b></span>.</li></ul>
        </div>
        <p id="en-us_topic_0012807343_p438206609174"><a name="en-us_topic_0012807343_p438206609174"></a><a name="en-us_topic_0012807343_p438206609174"></a>The parameter contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;,&lt;'$, and can be left blank.</p>
        </td>
        </tr>
        </tbody>
        </table>

7.  Confirm job configuration information and click  **OK**.

    After the job is created, you can manage it.


## Submitting a Job in the Background<a name="section12299175615451"></a>

1.  Log in to any Master node. For details, see  [Logging In to a Master Node](logging-in-to-a-master-node.md).
2.  Run the following command to initialize environment variables:

    **source /opt/client/bigdata\_env**

3.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If the Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    Example:  **kinit admin**

4.  Run the following command to copy the program in the OBS bucket to the Master node in the cluster:

    **hadoop fs -Dfs.s3a.access.key=AK -Dfs.s3a.secret.key=SK -copyToLocal source\_path.jar target\_path.jar**

    Example:  **hadoop fs -Dfs.s3a.access.key=XXXX -Dfs.s3a.secret.key=XXXX -copyToLocal "s3a://mrs-word/program/hadoop-mapreduce-examples-XXX.jar" "/home/omm/hadoop-mapreduce-examples-XXX.jar"**

    You can log in to OBS Console using AK/SK. To obtain AK/SK information, click the username in the upper right corner of the management console and choose  **My Credentials**  \>  **Access Keys**.

5.  Run the following command to submit a wordcount job. If data needs to be read from OBS or outputted to OBS, the AK/SK parameters need to be added.

    **source /opt/client/bigdata\_env;hadoop jar execute\_jar wordcount input\_path output\_path**

    Example:  **source /opt/client/bigdata\_env;hadoop jar /home/omm/hadoop-mapreduce-examples-XXX.jar wordcount -Dfs.s3a.access.key=XXXX -Dfs.s3a.secret.key=XXXX "s3a://mrs-word/input/\*" "s3a://mrs-word/output/"**

    In the preceding command,  **input\_path**  indicates a path for storing job input files on OBS.  **output\_path**  indicates a path for storing job output files on OBS and needs to be set to a directory that does not exist


