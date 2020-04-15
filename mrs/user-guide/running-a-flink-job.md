# Running a Flink Job<a name="EN-US_TOPIC_0221415049"></a>

You can submit programs developed by yourself to MRS to execute them, and obtain the results. This section describes how to submit a Flink job on the MRS management console. Flink jobs are used to submit JAR programs to process streaming data.

## Prerequisites<a name="section2335951116026"></a>

You have uploaded the program packages and data files required for running jobs to OBS or HDFS.

## Submitting a Job on the GUI<a name="section75299125395"></a>

1.  Log in to the MRS management console.
2.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
3.  If Kerberos authentication is enabled for the cluster, perform the following steps. If Kerberos authentication is not enabled for the cluster, skip this step.

    In the  **Basic Information**  area on the  **Dashboard**  tab page, click  ![](figures/en-us_image_0226013654.png)  on the right side of  **IAM User Sync**  to synchronize IAM users. For details, see  [Synchronizing IAM Users to MRS](synchronizing-iam-users-to-mrs.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   In the versions earlier than MRS 1.9.2, the job management function is unavailable in a cluster with Kerberos authentication enabled. You need to submit a job in the background.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS Viewer to MRS User, MRS Admin, or MRS Administrator, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated. Then, submit a job. Otherwise, the job may fail to be submitted.  
    >-   When the policy of the user group to which the IAM user belongs changes from MRS User, MRS Admin, or MRS Administrator to MRS Viewer, wait for 5 minutes until the new policy takes effect after the synchronization is complete because the  **sssd**  cache of cluster nodes needs time to be updated.  

4.  Click the  **Jobs**  tab.
5.  Click  **Create**. The  **Create Job**  page is displayed.
6.  Set  **Type**  to  **Flink**. Configure Flink job information by referring to  [Table 1](#tf38a01bf69f34c29a25317555fc32b92).

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
    <tr id="rbd79ceb2feb141ff9cb37ffde9e08ed7"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a4e9842e891a449118c2e3811caa071d9"><a name="a4e9842e891a449118c2e3811caa071d9"></a><a name="a4e9842e891a449118c2e3811caa071d9"></a>Program Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p655627719565"><a name="p655627719565"></a><a name="p655627719565"></a>Path of the program package to be executed. The following requirements must be met:</p>
    <a name="ul1375493195654"></a><a name="ul1375493195654"></a><ul id="ul1375493195654"><li>Contains a maximum of 1,023 characters, excluding special characters such as ;|&amp;&gt;&lt;'$. The parameter value cannot be empty or full of spaces.</li><li>The path of the program to be executed can be stored in HDFS or OBS. The path varies depending on the file system.<a name="en-us_topic_0173264852_ul56833471484"></a><a name="en-us_topic_0173264852_ul56833471484"></a><ul id="en-us_topic_0173264852_ul56833471484"><li>OBS: The path must start with <span class="parmvalue" id="parmvalue31990530182"><a name="parmvalue31990530182"></a><a name="parmvalue31990530182"></a><b>s3a://</b></span>. Example: <strong id="b050143852311"><a name="b050143852311"></a><a name="b050143852311"></a>s3a://wordcount/program/<em id="i2021313439231"><a name="i2021313439231"></a><a name="i2021313439231"></a>xxx</em>.jar</strong></li><li>HDFS: The path must start with <span class="parmvalue" id="parmvalue828144432312"><a name="parmvalue828144432312"></a><a name="parmvalue828144432312"></a><b>/user</b></span>.</li></ul>
    </li><li>For SparkScript, the path must end with <strong id="b4516016217"><a name="b4516016217"></a><a name="b4516016217"></a>.sql</strong>. For MapReduce and Spark, the path must end with <strong id="b8517191929"><a name="b8517191929"></a><a name="b8517191929"></a>.jar</strong>. The <strong id="b8623134020214"><a name="b8623134020214"></a><a name="b8623134020214"></a>.sql</strong> and <strong id="b6625540626"><a name="b6625540626"></a><a name="b6625540626"></a>.jar</strong> are case-insensitive.</li></ul>
    <div class="note" id="note37771150161214"><a name="note37771150161214"></a><a name="note37771150161214"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12108437424"><a name="p12108437424"></a><a name="p12108437424"></a>If you use an OBS path starting with <span class="parmvalue" id="parmvalue11701104312329"><a name="parmvalue11701104312329"></a><a name="parmvalue11701104312329"></a><b>s3a://</b></span>, configure permission for accessing OBS by referring to <a href="accessing-obs-using-obs.md">Accessing OBS Using obs</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row17824727141"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p482420210144"><a name="p482420210144"></a><a name="p482420210144"></a>Program Parameter</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1652632614145"><a name="p1652632614145"></a><a name="p1652632614145"></a>Used to configure optimization parameters such as threads, memory, and vCPUs for the job to optimize resource usage and improve job execution performance.</p>
    </td>
    </tr>
    <tr id="r7dcde55c00da4bc88afb2b022bce0abd"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a61afb54329564e458086d7622bda3b89"><a name="a61afb54329564e458086d7622bda3b89"></a><a name="a61afb54329564e458086d7622bda3b89"></a>Parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="ad6f1110b8e38456193949182f7a05980"><a name="ad6f1110b8e38456193949182f7a05980"></a><a name="ad6f1110b8e38456193949182f7a05980"></a>Key parameter for program execution. The parameter is specified by the function of the user's program. MRS is only responsible for loading the parameter. Multiple parameters are separated by space.</p>
    <p id="a6c44712b37c74651afe354f3cbf9e02f"><a name="a6c44712b37c74651afe354f3cbf9e02f"></a><a name="a6c44712b37c74651afe354f3cbf9e02f"></a>The parameter contains a maximum of 2,047 characters, excluding special characters such as ;|&amp;&gt;&lt;'$, and can be left blank.</p>
    <div class="note" id="note62371709174814"><a name="note62371709174814"></a><a name="note62371709174814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0173264852_p20521095174814"><a name="en-us_topic_0173264852_p20521095174814"></a><a name="en-us_topic_0173264852_p20521095174814"></a>When entering a parameter containing sensitive information (for example, login password), you can add an at sign (@) before the parameter name to encrypt the parameter value. This prevents the sensitive information from being persisted in plaintext. When you view job information on the MRS management console, the sensitive information is displayed as <strong id="en-us_topic_0173264852_b4931524432"><a name="en-us_topic_0173264852_b4931524432"></a><a name="en-us_topic_0173264852_b4931524432"></a>*</strong>.</p>
    <p id="en-us_topic_0173264852_p1265001117571"><a name="en-us_topic_0173264852_p1265001117571"></a><a name="en-us_topic_0173264852_p1265001117571"></a>Example: <strong id="en-us_topic_0173264852_b67512611320"><a name="en-us_topic_0173264852_b67512611320"></a><a name="en-us_topic_0173264852_b67512611320"></a>username=admin @password=admin_123</strong></p>
    </div></div>
    </td>
    </tr>
    <tr id="row7582163653214"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1527715406327"><a name="p1527715406327"></a><a name="p1527715406327"></a>Service Parameter</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p0595819249"><a name="p0595819249"></a><a name="p0595819249"></a>This parameter is optional. It is used to modify service parameters for the job. The parameter modification applies only to the current job. To make the modification take effect permanently for the cluster, follow instructions in <a href="configuring-service-parameters.md">Configuring Service Parameters</a>.</p>
    <p id="p1793619348256"><a name="p1793619348256"></a><a name="p1793619348256"></a>To add multiple parameters, click <a name="image19313313110"></a><a name="image19313313110"></a><span><img id="image19313313110" src="figures/en-us_image_0226013679.png"></span> on the right. To delete a parameter, click <span class="parmvalue" id="en-us_topic_0173264852_parmvalue163711139122718"><a name="en-us_topic_0173264852_parmvalue163711139122718"></a><a name="en-us_topic_0173264852_parmvalue163711139122718"></a><b>Delete</b></span> on the right.</p>
    </td>
    </tr>
    <tr id="row17661172893316"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p10661142818337"><a name="p10661142818337"></a><a name="p10661142818337"></a>Command Reference</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p204063412410"><a name="p204063412410"></a><a name="p204063412410"></a>Command submitted to the background for execution when a job is submitted</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Confirm job configuration information and click  **OK**.

    After the job is created, you can manage it.


