# Managing a Tenant Directory<a name="EN-US_TOPIC_0125375448"></a>

## Scenario<a name="section20357089194250"></a>

You can  manage the HDFS storage directory used by a specific tenant on MRS Manager. The management operations include adding a tenant directory, modifying the quotas for directory file quantity and storage space, and deleting a directory.

## Prerequisites<a name="section4564761919437"></a>

A tenant with HDFS storage resources has been added.

## Procedure<a name="section59639241194316"></a>

-   View a tenant directory.
    1.  On MRS Manager, click  **Tenant**.
    2.  In the tenant list on the left, click the target tenant.
    3.  Click the  **Resource**  tab.
    4.  View the  **HDFS Storage**  table.
        -   The  **Quota** column indicates the quotas for the  file and directory quantity of the tenant directory.
        -   The  **Space Quota**  column indicates the storage space size of the tenant directory.


-   Add a tenant directory.
    1.  On MRS Manager, click  **Tenant**.
    2.  In the tenant list on the left, click the tenant whose HDFS storage directory needs to be added.
    3.  Click the  **Resource**  tab.
    4.  In the  **HDFS Storage** table, click **Create Directory**.
        -   In  **Parent Directory**, select a storage directory of a parent tenant.

            This parameter is valid for sub-tenants only. If the parent tenant has multiple directories, select any one of them.

        -   Set  **Path**  to a tenant directory path.

            >![](/images/icon-note.gif) **NOTE:**   
            >-   If the current tenant is not a sub-tenant, the new path is created in the HDFS root directory.  
            >-   If the current tenant is a sub-tenant, the new path is created in the specified parent directory.  

            A complete HDFS storage path contains a maximum of 1023 characters. An HDFS directory name can contain digits, letters, spaces, and underscores \(\_\). The name cannot start or end with a space.

        -   Set  **Quota** to the quotas for  file and directory quantity.

            **Quota**  is optional. Its value ranges from 1 to 9223372036854775806.

        -   Set  **Space Quota**  to the storage space size of the tenant directory.

            The value of  **Space Quota**  ranges from 1 to 8796093022208.

            >![](/images/icon-note.gif) **NOTE:**   
            >To ensure data reliability, two more copies of a file are automatically generated when the file is stored in HDFS. That is, three copies of the same file are stored by default. The HDFS storage space indicates the total disk space occupied by all these copies. For example, if  **Space Quota** is set to **500**, the actual space for storing files is about 166 MB \(500/3 = 166\).  


    5.  Click  **OK**. The system creates the tenant directory in the HDFS root directory.

-   Modify tenant directory attributes.
    1.  On MRS Manager, click  **Tenant**.
    2.  In the tenant list on the left, click the tenant whose HDFS storage directory needs to be modified.
    3.  Click the  **Resource**  tab.
    4.  In the  **HDFS Storage** table, click **Modify** in the **Operation**  column of the specified tenant directory.
        -   Set  **Quota** to the quotas for  file and directory quantity.

            **Quota**  is optional. Its value ranges from 1 to 9223372036854775806.

        -   Set  **Space Quota**  to the storage space size of the tenant directory.

            The value of  **Space Quota**  ranges from 1 to 8796093022208.

            >![](/images/icon-note.gif) **NOTE:**   
            >To ensure data reliability, two more copies of a file are automatically generated when the file is stored in HDFS. That is, three copies of the same file are stored by default. The HDFS storage space indicates the total disk space occupied by all these copies. For example, if  **Space Quota** is set to **500**, the actual space for storing files is about 166 MB \(500/3 = 166\).  


    5.  Click  **OK**.

-   Delete a tenant directory.
    1.  On MRS Manager, click  **Tenant**.
    2.  In the tenant list on the left, click the tenant whose HDFS storage directory needs to be deleted.
    3.  Click the  **Resource**  tab.
    4.  In the  **HDFS Storage** table, click **Delete** in the **Operation**  column of the specified tenant directory.

        The default HDFS storage directory configured during tenant creation cannot be deleted. Only new HDFS storage directories can be deleted.

    5.  Click  **OK**. The tenant directory is deleted.


