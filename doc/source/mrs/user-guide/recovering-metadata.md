# Recovering Metadata<a name="EN-US_TOPIC_0125376139"></a>

## Scenario<a name="section39668340104638"></a>

Metadata needs to be recovered in the following scenarios:

-   Data is modified or deleted unexpectedly and needs to be restored.
-   After a critical operation \(such as an upgrade or critical data adjustment\) is performed on metadata components, an exception occurs or the operation does not achieve the expected result. All modules are faulty and become unavailable.
-   Data is migrated to a new cluster.

Users can create a recovery task on MRS Manager to recover metadata. Only manual recovery tasks are supported.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   Data recovery can be performed only when the system version is consistent with that of data backup.  
>-   Before recovering data when the service is running properly, you are advised to manually back up the latest management data. Otherwise, the metadata that is generated after the data backup and before the data recovery will be lost.  
>-   Use the OMS data and LdapServer data that is backed up at the same point in time to recover the data. Otherwise, the service and operation may fail.  
>-   By default,  the MRS cluster uses DBService to save Hive metadata.  

## Impact on the System<a name="section50228946104945"></a>

-   Data generated between the backup time and restoration time is lost.
-   After the data is recovered, the configuration of the components that depend on DBService may expire and these components need to be restarted.

## Prerequisites<a name="section13354932105013"></a>

-   The data in the OMS and LdapServer backup files  has been  backed up at the same time.
-   The status of the OMS resources and the LdapServer instances is normal. If the status is abnormal, data recovery cannot be performed.
-   The status of the cluster hosts and services is normal. If the status is abnormal, data recovery cannot be performed.
-   The cluster host topologies during data recovery and data backup are the same. If the topologies are different, data recovery cannot be performed and you need to back up data again.
-   The services added to the cluster during data recovery and data backup are the same. If the services are different, data recovery cannot be performed and you need to back up data again.
-   The status of the active and standby DBService instances is normal. If the status is abnormal, data recovery cannot be performed.
-   The upper-layer applications that depend on the MRS cluster  have been  stopped.
-   On MRS Manager, all the NameNode role instances  with data being recovered have been stopped. Other HDFS role instances keep running. After data is recovered, the NameNode role instances need to be restarted and cannot be accessed before the restart.
-   You have checked whether the NameNode backup files  have been saved in the _Data save path_**/LocalBackup/**  directory on the active management node.

## Procedure<a name="section18111903105142"></a>

1.  Check the location of the backup data.
    1.  On MRS Manager, choose  **System**  \>  **Back Up Data**.
    2.  In the  **Operation** column of a specified task in the task list, choose **More**  \>  **View History** to view the records of historical backup tasks. In the window that is displayed, select a record and click **View** in the **Backup Path** column to view its backup path information. Find the following information:
        -   **Backup Object**: indicates the data source of the backup data.
        -   **Backup Path**: indicates the full path where the backup files are saved.

    3.  Select the correct item, and manually copy the full path of backup files in  **Backup Path**.

2.  Create a recovery task.
    1.  On MRS Manager, choose  **System**  \>  **Restore Data**.
    2.  Click  **Create Restoration Task**.
    3.  Set  **Name**  to the name of the recovery task.

3.  Select recovery sources.

    In  **Configuration**,  select the components whose metadata is to be recovered.

4.  Set recovery parameters.
    1.  Set  **Path Type**  to a backup directory type.
    2.  The settings vary according to backup directory types:
        -   **LocalDir**: indicates that backup files are stored on the local disk of the active management node. If you select this value, you need to set **Source Path** to the full path of the backup file. For example, **_Data path_/LocalBackup/_backup task name\_task creation time/data source\_task execution time/version\_data source\_task execution time.tar.gz_**.
        -   **LocalHDFS**: indicates that backup files are stored in the HDFS directory of the current cluster. If you select this value, you need to set the following parameters:
            -   **Source Path**: indicates the full path of the backup file in HDFS. For example, **_backup path/backup task name\_task creation time/version\_data source\_task execution time.tar.gz_**.
            -   **Source Instance Name**: indicates the name of the NameService instance that corresponds to the backup directory when the recovery task is executed. The default value is **hacluster**.

    3.  Click  **OK**  to save the settings.

5.  Execute the recovery task.

    In the  **Operation** column of the created task in the recovery task list, click **Start**  to execute the recovery task.

    -   If the recovery is successful, the progress bar is green.
    -   If  the recovery is successful, the recovery task cannot be executed again.
    -   If the recovery task fails during the first execution, rectify the fault and click  **Start**  to execute the task again.

6.  Determine what metadata  has been  recovered.
    -   If OMS and LdapServer metadata  has been recovered, go to [7](#li3654235411916).
    -   If DBService data  has been recovered, the task is complete.
    -   If NameNode data  has been recovered, choose **Service**  \>  **HDFS**  \>  **More**  \>  **Restart Service** on MRS Manager to complete the task.

7.  <a name="li3654235411916"></a>Restart Manager  for the recovered data to take effect.
    1.  On MRS Manager, choose  **LdapServer**  \>  **More**  \>  **Restart Service**, click **OK**, and wait for the LdapServer service to restart.
    2.  Log in to the active management node. For details, see  [Viewing Active and Standby Nodes](viewing-active-and-standby-nodes.md).
    3.  Run the following command to restart OMS:

        **sh $\{BIGDATA\_HOME\}/om-0.0.1/sbin/restart-oms.sh**

        The command is executed successfully if the following information is displayed:

        ```
        start HA successfully.
        ```

    4.  On MRS Manager, choose  **KrbServer**  \>  **More**  \>  **Synchronize Configuration**, deselect **Restart services or instances whose configurations have expired**, click **OK**, and wait for the KrbServer service configuration to synchronize and for the service to restart.
    5.  On MRS Manager, choose  **Service**  \>  **More**  \>  **Synchronize Configuration**, deselect **Restart services or instances whose configurations have expired**, click **OK**, and wait for the cluster configuration to synchronize.
    6.  Choose  **Service**  \>  **More**  \>  **Stop Cluster**. After the cluster has been stopped, choose **Service**  \>  **More**  \>  **Start Cluster**, and wait for the cluster to start.


