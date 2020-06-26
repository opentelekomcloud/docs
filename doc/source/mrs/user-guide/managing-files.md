# Managing Files<a name="EN-US_TOPIC_0125375754"></a>

You can create directories, delete directories, and import, export, or delete files on the  **Files**  page in an analysis cluster with Kerberos authentication disabled.

## Background<a name="s7f9d67568078498c844ac10ad72259dc"></a>

Data to be processed by MRS is stored in either OBS or HDFS. OBS provides you with massive, highly reliable, and secure data storage capabilities at a low cost. You can view, manage, and use data through OBS Console or OBS Browser.

## Importing Data<a name="sd440bbc37a254f4f9a8c05e976c10ae7"></a>

MRS supports data import from the OBS system to HDFS. This function is recommended if the data size is small, because the upload speed reduces as the file size increases.

Both files and folders containing files can be imported. The operations are as follows:

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Cluster**  \>  **Active Cluster**, select a cluster, and click its name to switch to the cluster details page.
4.  Click  **Files** and go to the **Files**  tab page.
5.  Select  **HDFS File List**.
6.  Click the data storage directory, for example,  **bd\_app1**.

    **bd\_app1** is just an example. The storage directory can be any directory on the page. You can create a directory by clicking **Create Folder**.

7.  Click  **Import Data**  to configure the paths for HDFS and OBS.

    >![](/images/icon-note.gif) **NOTE:**   
    >When configuring the OBS or HDFS path, click  **Browse**, select the file path, and click **OK**.  

    -   The path for OBS
        -   Must start with  **s3a://**. **s3a://**  is used by default.
        -   Files and programs encrypted by the KMS cannot be imported.
        -   Empty folders cannot be imported.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with a period \(**.**\).
        -   Directories and file names cannot be empty.
        -   The full path of OBS contains a maximum of 1023 characters.

    -   The path for HDFS
        -   It starts with **/user**  by default.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with a period \(**.**\).
        -   Directories and file names cannot be empty.
        -   The full path of HDFS contains a maximum of 1023 characters.
        -   The parent HDFS directory in  **HDFS File List**  is displayed in the textbox for the HDFS path by default when data is imported.

8.  Click  **OK**.

    View the upload progress in  **File Operation Records**. The data import operation is operated as a Distcp job by MRS. You can check whether the Distcp job is successfully executed on the **Jobs**  tab page.


## Exporting Data<a name="s5df850a66ea64b1db70ff4fcf02f9e4b"></a>

After data is processed and analyzed, you can either store the data in HDFS or export it to the OBS system.

Both files and folders containing files can be exported. The operations are as follows:

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Cluster**  \>  **Active Cluster**, select a cluster, and click its name to switch to the cluster details page.
4.  Click  **Files** and go to the Files tab page.
5.  Select  **HDFS File List**.
6.  Click the data storage directory, for example,  **bd\_app1**.
7.  Click  **Export Data**  and configure the paths for HDFS and OBS.

    >![](/images/icon-note.gif) **NOTE:**   
    >When configuring the OBS or HDFS path, click  **Browse**, select the file path, and click **OK**.  

    -   The path for OBS
        -   Must start with  **s3a://**. **s3a://**  is used by default.
        -   Empty folders cannot be imported.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with a period \(**.**\).
        -   Directories and file names cannot be empty.
        -   The full path of OBS contains a maximum of 1023 characters.

    -   The path for HDFS
        -   It starts with **/user**  by default.
        -   Directories and file names can contain letters, Chinese characters, digits, hyphens \(-\), or underscores \(\_\), but cannot contain special characters \(/:\*?"<\>|\\;&,'\`!\{\}\[\]$\).
        -   Directories and file names cannot start or end with a period \(**.**\).
        -   Directories and file names cannot be empty.
        -   The full path of HDFS contains a maximum of 1023 characters.
        -   The parent HDFS directory in  **HDFS File List**  is displayed in the textbox for the HDFS path by default when data is imported.

    >![](/images/icon-note.gif) **NOTE:**   
    >Ensure that the exported folder is not empty. If an empty folder is exported to the OBS system, the folder is exported as a file. After the folder is exported, its name is changed, for example, from test to  **test-$folder$**, and its type is file.  

8.  Click  **OK**.

    View the upload progress in  **File Operation Records**. The data export operation is operated as a Distcp job by MRS. You can check whether the Distcp job is successfully executed in **Jobs**  page.


