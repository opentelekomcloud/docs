# Example: Using Loader to Import Data from OBS to HDFS<a name="EN-US_TOPIC_0125375248"></a>

## Scenario<a name="s15ee70ec71a04ec99eaf1f5f598d13fe"></a>

If you need to import a large volume of data from the external cluster to the internal cluster, import it from OBS to HDFS.

## Prerequisites<a name="sfd5cc32a61a746fb843b023a2c026062"></a>

-   You have prepared service data.
-   You have created an analysis cluster.

## Procedure<a name="sb55c5dc8e4d9487ca4186dbbb8835748"></a>

1.  Upload service data to your OBS bucket.
2.  Obtain AK/SK information and create an OBS link and an HDFS link.

    For details, see  [Loader Link Configuration](loader-link-configuration.md).

3.  Access the Loader page. For details, see  [Loader Page](introduction_loader.md#s49ec1e4eeb254b4d97c98caf69fa110f).

    If Kerberos authentication is enabled in the analysis cluster, follow instructions in  [Accessing the Hue WebUI](accessing-the-hue-webui.md).

4.  Click  **New Job**.
5.  In  **Information**, set parameters.
    1.  In  **Name**, enter a job name, for example, **obs2hdfs**.
    2.  In  **From link**, select the OBS link you create.
    3.  In  **To link**, select the HDFS link you create.

6.  In  **From**, set source link parameters.

    1.  In  **Bucket Name**, enter a name of the bucket storing service data.
    2.  In  **Input directory or file**, enter a detailed location of service data in the bucket.

        If it is a single file, enter a complete path containing the file name. If it is a directory, enter the complete path of the directory.

    3.  <a name="l1ccbe49b8b4b438d9a929e5920ba2451"></a>In  **File format**, enter the type of the service data file.

    For details, see  [Table 1](source-link-configurations-of-loader-jobs.md#tc09a1f1fd20c4ea6aec386e69b72383f).

7.  In  **To**, set destination link parameters.

    1.  In  **Output directory**, enter the directory for storing service data in HDFS.

        If Kerberos authentication is enabled in the cluster, the current user who accesses Loader needs to have permission to write data to the directory.

    2.  In  **File format**, enter the type of the service data file.

        The type must correspond to the type in  [6.c](#l1ccbe49b8b4b438d9a929e5920ba2451).

    3.  In  **Compression codec**, enter a compression algorithm. For example, if you do not compress data, select **NONE**.
    4.  In  **Overwrite**, select **True**.
    5.  Click  **Show Senior Parameter** and set **Line Separator**.
    6.  Set  **Field Separator**.

    For details, see  [Table 5](destination-link-configurations-of-loader-jobs.md#tdaf4dde5df8c47a298cd4b3cd83a72aa).

8.  In  **Task Config**, set job running parameters.
    1.  In  **Extractors**, enter the number of map tasks.
    2.  In  **Loaders**, enter the number of reduce tasks.

        When the destination link is an HDFS link,  **Loaders**  is hidden. 

    3.  In  **Max error records in single split**, enter an error record threshold.
    4.  In  **Dirty data directory**, enter a directory for saving dirty data, for example, **/user/sqoop/obs2hdfs-dd**.

9.  Click  **Save and execute**.

    On the  **Manage jobs** page, view the job running result. You can click **Refresh**  to obtain the latest job status.


