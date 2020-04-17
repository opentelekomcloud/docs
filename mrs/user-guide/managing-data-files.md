# Managing Data Files<a name="EN-US_TOPIC_0125375327"></a>

After Kerberos authentication is disabled, you can create directories, delete directories, and import, export, or delete files on the  **Files**  page.

## Background<a name="section37468229155639"></a>

Data to be processed by MRS is stored in either OBS or HDFS. OBS provides you with massive, highly reliable, and secure data storage capabilities at a low cost. You can view, manage, and use data through OBS Console or OBS Browser. In addition, you can use the REST APIs to manage or access data. The REST APIs can be used alone or it can be integrated with service programs.

Before creating jobs, upload the local data to OBS for computing and analysis. MRS allows data to be exported from OBS to HDFS for computing and analysis. After the analysis and computing are complete, you can either store the data in HDFS or export it to OBS. HDFS and OBS can store compressed data in the format of bz2 or gz.

## Importing Data<a name="section5674212155752"></a>

MRS supports data import from the OBS system to HDFS. This function is recommended if the data size is small, because the upload speed reduces as the file size increases.

Both files and folders containing files can be imported. The operations are as follows:

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a cluster, and click its name to switch to the cluster details page.
4.  Click  **Files** and go to the  **Files**  tab page.
5.  Select  **HDFS File List**.
6.  Click the data storage directory, for example,  **bd\_app1**.

    **bd\_app1** is just an example. The storage directory can be any directory on the page. You can create a directory by clicking **Create Folder**.

    The name of the created directory must meet the following requirements:

    -   Contains a maximum of 255 characters, and the full path contains a maximum of 1023 characters.
    -   Cannot be empty.
    -   Cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
    -   Cannot start or end with a period \(**.**\).

7.  Click  **Import Data**  to configure the paths for HDFS and OBS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When configuring the OBS or HDFS path, click  **Browse**, select the file path, and click **OK**.  

    -   The path for OBS
        -   Must start with  **s3a://**.  **s3a://**  is used by default.
        -   Files and programs encrypted by the KMS cannot be imported.
        -   Empty folders cannot be imported.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with spaces, but can have spaces between other characters.
        -   The full path of OBS contains a maximum of 1023 characters.

    -   The path for HDFS
        -   It starts with **/user**  by default.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with spaces, but can have spaces between other characters.
        -   The full path of HDFS contains a maximum of 1023 characters.
        -   The parent HDFS directory in  **HDFS File List**  is displayed in the textbox for the HDFS path by default when data is imported.

8.  Click  **OK**.

    View the upload progress in  **File Operation Records**. The data import operation is operated as a Distcp job by MRS. You can check whether the Distcp job is successfully executed in **Jobs**  page.


## Exporting Data<a name="section9982368155810"></a>

After data is processed and analyzed, you can either store the data in HDFS or export it to the OBS system.

Both files and folders containing files can be exported. The operations are as follows:

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a cluster, and click its name to switch to the cluster details page.
4.  Click  **Files** and go to the **Files**  tab page.
5.  Select  **HDFS File List**.
6.  Click the data storage directory, for example,  **bd\_app1**.
7.  Click  **Export Data**  and configure the paths for HDFS and OBS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When configuring the OBS or HDFS path, click  **Browse**, select the file path, and click **OK**.  

    -   The path for OBS
        -   Must start with  **s3a://**. **s3a://**  is used by default.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with spaces, but can have spaces between other characters.
        -   The full path of OBS contains a maximum of 1023 characters.

    -   The path for HDFS
        -   It starts with **/user**  by default.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with spaces, but can have spaces between other characters.
        -   The full path of HDFS contains a maximum of 1023 characters.
        -   The parent HDFS directory in  **HDFS File List**  is displayed in the textbox for the HDFS path by default when data is exported.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Ensure that the exported folder is not empty. If an empty folder is exported to the OBS system, the folder is exported as a file. After the folder is exported, its name is changed, for example, from  **test** to **test-$folder$**, and its type is file.  

8.  Click  **OK**.

    View the upload progress in  **File Operation Records**. The data export operation is operated as a Distcp job by MRS. You can check whether the Distcp job is successfully executed in **Jobs**  page.


## Viewing File Operation Records<a name="section14278550102310"></a>

When importing or exporting data on the MRS management console, you can choose  **Files \> File Operation Records**  to view the import or export progress.

[Table 1](#table59621065102929)  lists the parameters in file operation records.

**Table  1**  Parameters in file operation records

<a name="table59621065102929"></a>
<table><thead align="left"><tr id="row30921286102929"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p60148761102929"><a name="p60148761102929"></a><a name="p60148761102929"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p40211485102929"><a name="p40211485102929"></a><a name="p40211485102929"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26359045102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p54707896102929"><a name="p54707896102929"></a><a name="p54707896102929"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2154600102929"><a name="p2154600102929"></a><a name="p2154600102929"></a>Time when data import or export is started</p>
</td>
</tr>
<tr id="row19391402102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p27199711102929"><a name="p27199711102929"></a><a name="p27199711102929"></a>Source Path</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p55692997102929"><a name="p55692997102929"></a><a name="p55692997102929"></a>Source path of data</p>
<a name="ul29001071103850"></a><a name="ul29001071103850"></a><ul id="ul29001071103850"><li>In data import, <span class="parmname" id="parmname15194122104023"><a name="parmname15194122104023"></a><a name="parmname15194122104023"></a><b>Source Path</b></span> is the OBS path.</li><li>In data export, <span class="parmname" id="parmname38110106104029"><a name="parmname38110106104029"></a><a name="parmname38110106104029"></a><b>Source Path</b></span> is the HDFS path.</li></ul>
</td>
</tr>
<tr id="row31474930102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p66441379102929"><a name="p66441379102929"></a><a name="p66441379102929"></a>Target Path</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p13042650102929"><a name="p13042650102929"></a><a name="p13042650102929"></a>Target path of data</p>
<a name="ul5041459410402"></a><a name="ul5041459410402"></a><ul id="ul5041459410402"><li>In data import, <span class="parmname" id="parmname50483631104032"><a name="parmname50483631104032"></a><a name="parmname50483631104032"></a><b>Target Path</b></span> is the HDFS path.</li><li>In data export, <span class="parmname" id="parmname40748148104035"><a name="parmname40748148104035"></a><a name="parmname40748148104035"></a><b>Target Path</b></span> is the OBS path.</li></ul>
</td>
</tr>
<tr id="row50274986102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p45742050102929"><a name="p45742050102929"></a><a name="p45742050102929"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><div class="p" id="p14118546102929"><a name="p14118546102929"></a><a name="p14118546102929"></a>Status of the data import or export operation<a name="ul805096292920"></a><a name="ul805096292920"></a><ul id="ul805096292920"><li>Running</li><li>Completed</li><li>Terminated</li><li>Abnormal</li></ul>
</div>
</td>
</tr>
<tr id="row59958055102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p24764287102929"><a name="p24764287102929"></a><a name="p24764287102929"></a>Duration (min)</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p59750244102929"><a name="p59750244102929"></a><a name="p59750244102929"></a>Total time used by data import or export</p>
<p id="p54926906103710"><a name="p54926906103710"></a><a name="p54926906103710"></a>Unit: minute</p>
</td>
</tr>
<tr id="row881286102929"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p4275369102929"><a name="p4275369102929"></a><a name="p4275369102929"></a>Result</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p10760588102929"><a name="p10760588102929"></a><a name="p10760588102929"></a>Data import or export result</p>
<a name="ul27678081115333"></a><a name="ul27678081115333"></a><ul id="ul27678081115333"><li>Successful</li><li>Failed</li></ul>
</td>
</tr>
<tr id="row1412857995349"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p50207374102846"><a name="p50207374102846"></a><a name="p50207374102846"></a>Operation</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2162891911113"><a name="p2162891911113"></a><a name="p2162891911113"></a>View Log: You can click <span class="uicontrol" id="uicontrol3647802411815"><a name="uicontrol3647802411815"></a><a name="uicontrol3647802411815"></a><b>View Log</b></span> to view log information of a job.&nbsp;For details, see&nbsp;<a href="viewing-job-configurations-and-logs.md">Viewing Job Configurations and Logs</a>.</p>
</td>
</tr>
</tbody>
</table>

