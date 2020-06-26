# Backing Up Metadata<a name="EN-US_TOPIC_0125375812"></a>

## Scenario<a name="section1680505393831"></a>

To ensure the security of metadata either on a routine basis or before and after performing critical metadata operations \(such as capacity expansion and reduction, patch installation, upgrades, or migration\), metadata must be backed up. The backup data can be used to recover the system if an exception occurs or if the operation has not achieved the expected result. This minimizes the adverse impact on services.

Metadata includes OMS data, LdapServer data, DBService data, and NameNode data. The Manager data to be backed up includes OMS data and LdapServer data.

By default, metadata backup is supported by the  **default** task. Users can create a backup task on MRS Manager to back up metadata. Both automatic and manual backup tasks are supported.

## Prerequisites<a name="section46714859456"></a>

-   A standby cluster for backing up data has been created and the network is connected. The inbound rules of the two security groups  in the peer cluster have been added to the two security groups in each cluster to allow all access requests of all ECS protocols and ports in the security groups.
-   The backup type, period, policy, and other specifications have been planned.
-   The _Data save path_**/LocalBackup/** directories on the active and standby management nodes have sufficient space.

## Procedure<a name="section6261219795321"></a>

1.  Create a backup task.
    1.  On MRS Manager, choose  **System**  \>  **Back Up Data**.
    2.  Click  **Create Backup Task**.

2.  Set backup policies.
    1.  Set  **Name**  to the name of the backup task.
    2.  Set  **Mode** to the type of the backup task. **Periodic** indicates that the backup task is periodically executed and **Manual**  indicates that the backup task is manually executed.

        To create a periodic backup task, set the following parameters in addition to the preceding parameters:

        -   **Start Time**: indicates the time when the task is started for the first time.
        -   **Period**: indicates a task execution interval. The options include **By hour** and **By day**.
        -   **Backup Policy**: indicates the volume of data to be backed up when each task is started. The options include **Full backup at the first time and subsequent incremental backup**, **Full backup every time**, and **Full backup once every n times**. When the parameter is set to **Full backup once every n times**, **n**  must be specified.

3.  Select backup sources.

    Set  **Configuration** to **OMS** and **LdapServer**.

4.  Set backup parameters.
    1.  Set  **Path Type** of **OMS** and **LdapServer**  to a backup directory type.

        The following backup directory types are supported:

        -   **LocalDir**: indicates that backup files are stored on the local disk of the active management node. The standby management node automatically synchronizes the backup files. The default save path is _Data save path_**/LocalBackup/**. If you select this value, you need to set **Max. Number of Backup Copies**  to specify the number of backup files that can be retained in the backup directory.
        -   **LocalHDFS**: indicates that backup files are stored in the HDFS directory of the current cluster. If you select this value, you need to set the following parameters:
            -   **Target Path**: indicates the backup file save path in HDFS. The save path cannot be a hidden HDFS directory, such as a snapshot or recycle bin directory, or a default system directory.
            -   **Max. Number of Backup Copies**: indicates the number of backup file sets that can be retained in the backup directory.
            -   **Target Instance Name**: indicates the name of the NameService instance that corresponds to the backup directory. The default value is **hacluster**.

    2.  Click  **OK**  to save the settings.

5.  Execute the backup task.

    In the  **Operation** column of the created task in the backup task list, click **More**  \>  **Run**  to execute the backup task.

    After the backup task is executed, the system automatically creates a subdirectory for each backup task in the backup directory. The subdirectory is used to save data source backup files. The format of the subdirectory name is _Backup task name_\__Task creation time_. The format of the backup file name is _Version_\__Data source_\__Task execution time_.tar.gz.


