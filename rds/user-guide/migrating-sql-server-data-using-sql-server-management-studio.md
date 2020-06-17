# Migrating SQL Server Data Using SQL Server Management Studio<a name="en-us_topic_0053089723"></a>

## Preparing for Data Migration<a name="section13141548201816"></a>

You can access RDS DB instances through an EIP or ECS.

1.  <a name="l7c29b4daf0d74d7d9b47b173265d179d"></a>Prepare an ECS for accessing DB instances in the same VPC subnet or prepare a device for accessing RDS through a public network.
    -   To connect to a DB instance through an ECS, you must first create an ECS.

        For details about how to create and connect to an ECS, see  [How Can I Create and Connect to an ECS?](how-can-i-create-and-connect-to-an-ecs.md)

    -   To connect to a DB instance through an EIP, you must:
        1.  Bind the EIP to the DB instance. For details, see  [Binding an EIP](binding-and-unbinding-an-eip.md#section3199593620428).
        2.  Ensure that the local device can access the EIP that has been bound to the DB instance.

2.  Install the Microsoft SQL Server client on the ECS or device that was prepared in  [step 1](#l7c29b4daf0d74d7d9b47b173265d179d).

    For details, see  [How Can I Install SQL Server Management Studio?](how-can-i-install-sql-server-management-studio.md)

    >![](/images/icon-note.gif) **NOTE:**   
    >The SQL Server Management Studio version must be equal to or later than the Microsoft SQL Server DB engine version.  


## Exporting Data<a name="section14833151719191"></a>

Before migrating an existing Microsoft SQL Server database to RDS, you need to export the Microsoft SQL Server database.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   The export tool must match the DB engine version.  
>-   Database migration is performed offline. Before the migration, you must stop any applications using the source database.  

1.  Log in to the prepared ECS or device that can access RDS DB instances.
2.  Use SQL Server Management Studio to generate database object scripts such as tables and views.

    1.  Use SQL Server Management Studio to connect to the Microsoft SQL Server database.
    2.  On  **Object Explorer**, expand  **Databases**, right-click the database to be exported, and choose  **Tasks**  \>  **Generate Scripts**. The  **Generate and Publish Scripts**  window is displayed.
    3.  Choose  **Choose Objects**  in the navigation pane on the left, select database objects to be exported, and click  **Next**.
    4.  Choose  **Set Scripting Options**  in the navigation pane on the left, click  **Save script to a specific location**, and select a path for storing exported files from the  **File name**  drop-down list, and click  **Next**.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   If you select  **Single file**, all objects will be stored in the same file.  
        >-   If you select  **Single file per object**, each object will be stored in its own file.  

    5.  Click  **Next**.
    6.  Click  **Finish**.
    7.  Use SQL Server Management Studio to open the exported SQL file or SQL files.
    8.  Change  **USE \[DATABASE\]**  in the first line to  **USE \[_RDS database name_\]**  and save the change.

    >![](/images/icon-note.gif) **NOTE:**   
    >For details on generating scripts, see  [Generate and Publish Scripts Wizard](https://docs.microsoft.com/en-us/sql/ssms/scripting/generate-and-publish-scripts-wizard?view=sql-server-2017).  

3.  Use bcp to export data from the source database to a .txt file.

    Download and install the  [bcp](https://docs.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-2017)  first. The command for exporting data is as follows:

    **\>bcp **_dbname.schema\_name.table\_name_** out** _C:\\test\\table\_name.txt_ **-n** **-S**  localhost  **-U** _username_ **-b** _2000_

    -   **out**  indicates the directory from which the data is imported.
    -   **-n**  indicates that the native \(database\) data types are used for performing bulk-copy operations.
    -   **-S**  indicates the address to be used by the bcp tool to connect to the Microsoft SQL Server DB instance.
    -   **-U**  indicates the database username.
    -   **-b**  indicates the lines of data imported in a batch.

    Enter the database password as prompted.

    Example:

    ```
    C:\test>bcp test.dbo.t1 out c:\test\t1.txt -n -S localhost -U rdsuser -b 2000
    Enter password:
    ```

    After this command is executed, a  **t1.txt**  file will be generated as follows:

    ```
    C:\test>$ dir t1.txt
    2017/03/27  11:51         22 t1.txt
    ```

    Repeat the preceding steps to export data from the other tables in the database.


## Importing Data<a name="section522153031911"></a>

This section describes how to use an ECS or a device that can access RDS to connect to a DB instance and import the exported SQL file into RDS.

>![](/images/icon-notice.gif) **NOTICE:**   
>If the source database contains the full-text index, you need to create one on RDS.  

1.  Import data through tools.

    Method 1: Use sqlcmd to import database objects.

    The Microsoft SQL Server database or client provides sqlcmd.

    \>**sqlcmd -S**  "_server_"  **-d** _database_ **-U** _login\_id_ **-i** _inputfile_

    -   **-S**  indicates the IP address and port of the RDS DB instance.
    -   **-d**  indicates the name of the database to be imported.
    -   **-U**  indicates the username used to log in to the database.
    -   **-i**  indicates the SQL file to be executed.

    Enter the database password as prompted.

    Example:

    ```
    >sqlcmd -S "10.65.60.79,8636" -d test -U rdsuser -i C:\test\objects.sql
    Enter password:
    ```

    Method 2: Use bcp to import data.

    \>**bcp** _dbname.schema\_name.table\_name_ **in** _C:\\test\\table\_name.txt_ **-n -S** _Server_ **-U** _username_ **-b** _2000_

    -   **in**  indicates the directory which the data is imported to.
    -   **-n**  indicates that the native \(database\) data types are used for performing bulk-copy operations.
    -   **-S**  indicates the address to be used by the bcp tool to connect to the Microsoft SQL Server DB instance.
    -   **-U**  indicates the database username.
    -   **-b**  indicates the lines of data imported in a batch.

    Enter the database password as prompted.

    Example:

    ```
    C:\test>bcp test.dbo.t1 in c:\test\t1.txt -n -S "10.65.60.79,8636" -U rdsuser -b 2000
    Enter password:
    ```

2.  Check the data import result.

    ```
    select * from sys.databases;
    ```

    **Figure  1**  Data import result<a name="fig78561115185918"></a>  
    ![](figures/data-import-result.png "data-import-result")


