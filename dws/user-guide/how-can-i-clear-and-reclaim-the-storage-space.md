# How Can I Clear and Reclaim the Storage Space?<a name="dws_03_0033"></a>

After you delete data stored in DWS data warehouses, dirty data may be generated possibly because the disk space is not released. This results in disk space waste and deteriorates snapshot creation and restoration performance. The following describes the impact on the system and subsequent operation to clear the disk space:

The impact on the system is as follows:

-   Unnecessary data needs to be deleted to release the storage space.
-   Frequent read and write operations may affect proper database use. Therefore, it is good practice to clear and reclaim the storage space when not in peak hours.
-   The data clearing time depends on the data stored in the database.

Perform the following steps to clear and reclaim the storage space:

1.  Connect to the database. For details, see section  [Connecting to a Cluster](connecting-to-a-cluster.md).
2.  Run the following command to clear and reclaim the storage space:

    **VACUUM FULL;**

    By default, tables of which the current user has the permission are deleted. For tables that the current user does not have permissions, skip reclamation.

    The storage space is cleared when the following information is displayed:

    ```
    VACUUM
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The statistical information will be lost if you use the  **Full**  parameter. To collect the statistics, add keyword  **ANALYZE**  ahead of the command. For example, run the  **VACUUM FULL ANALYZE;**  command. For more information about VACUUM, see  **VACUUM**  in the  _Data Warehouse Service Database Developer Guide_.  


