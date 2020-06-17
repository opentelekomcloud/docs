# Migrating MySQL Data Using mysqldump<a name="en-us_topic_migration_mysql"></a>

## Preparing for Data Migration<a name="section8743122116813"></a>

You can access RDS DB instances through an EIP or ECS.

1.  Prepare an ECS for accessing DB instances in the same VPC subnet or prepare a device for accessing RDS through a public network.
    -   To connect to a DB instance through an ECS, you must first create an ECS.

        For details about how to create and connect to an ECS, see  [How Can I Create and Connect to an ECS?](how-can-i-create-and-connect-to-an-ecs.md)

    -   To connect to a DB instance through an EIP, you must:
        1.  Bind the EIP to the DB instance. For details, see  [Binding an EIP](binding-and-unbinding-an-eip.md#section3199593620428).
        2.  Ensure that the local device can access the EIP that has been bound to the DB instance.

2.  Install the MySQL client on the prepared ECS or device.

    For details, see  [How Can I Install the MySQL Client?](how-can-i-install-the-mysql-client.md)

    >![](/images/icon-note.gif) **NOTE:**   
    >The MySQL client version must be the same as the version of RDS for MySQL. The MySQL database or client will provide mysqldump and mysql.  


## Exporting Data<a name="section692873015104"></a>

Before migrating an existing MySQL database to RDS, you need to export the MySQL database.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   The export tool must match the DB engine version.  
>-   Database migration is performed offline. Before the migration, you must stop any applications using the source database.  

1.  Log in to the prepared ECS or device that can access RDS DB instances.
2.  <a name="li16251172911136"></a>Use the mysqldump tool to export metadata into an SQL file.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >The MySQL database is required for RDS management. When exporting metadata, do not specify  **--all-database**. Otherwise, the MySQL database will be unavailable.  

    **mysqldump** **--databases**  <_DB\_NAME_\>  **--single-transaction --order-by-primary --hex-blob --no-data --routines --events --set-gtid-purged=OFF**  -u <_DB\_USER_\>  **-p -h**  <_DB\_ADDRESS_\>  **-P **<_DB\_PORT_\>  **|sed -e 's/DEFINER\[ \]\*=\[ \]\*\[^\*\]\*\\\*/\\\*/' -e 's/DEFINER\[ \]\*=.\*FUNCTION/FUNCTION/' -e 's/DEFINER\[ \]\*=.\*PROCEDURE/PROCEDURE/' -e 's/DEFINER\[ \]\*=.\*TRIGGER/TRIGGER/' -e 's/DEFINER\[ \]\*=.\*EVENT/EVENT/' \>** _<BACKUP\_FILE\>_

    -   **_DB\_NAME_**  indicates the name of the database to be migrated.
    -   **_DB\_USER_**  indicates the database username.
    -   **_DB\_ADDRESS_**  indicates the database address.
    -   **_DB\_PORT_**  indicates the database port.
    -   **_BACKUP\_FILE_**  indicates the name of the file to which the data will be exported.

    Enter the database password as prompted.

    Example:

    **mysqldump --databases rdsdb --single-transaction --order-by-primary --hex-blob --no-data --routines --events --set-gtid-purged=OFF -u root -p -h 192.168.151.18 -P 3306 |sed -e 's/DEFINER\[ \]\*=\[ \]\*\[^\*\]\*\\\*/\\\*/' -e 's/DEFINER\[ \]\*=.\*FUNCTION/FUNCTION/' -e 's/DEFINER\[ \]\*=.\*PROCEDURE/PROCEDURE/' -e 's/DEFINER\[ \]\*=.\*TRIGGER/TRIGGER/' -e 's/DEFINER\[ \]\*=.\*EVENT/EVENT/' \> dump-defs.sql**

    **Enter password:**

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use mysqldump with a version earlier than 5.6, remove  **--set-gtid-purged=OFF**  before running this command.  

    After this command is executed, a  **dump-defs.sql**  file will be generated as follows:

    ```
    [rds@localhost ~]$ ll dump-defs.sql
    -rw-r-----. 1 rds rds 2714 Sep 21 08:23 dump-defs.sql
    ```

3.  Use the mysqldump tool to export data into an SQL file.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >The MySQL database is required for RDS management. When exporting metadata, do not specify  **--all-database**. Otherwise, the MySQL database will be unavailable.  

    **mysqldump --databases**  <_DB\_NAME_\>  **--single-transaction --hex-blob --set-gtid-purged=OFF --no-create-info --skip-triggers** **-u**  <_DB\_USER_\>  **-p** **-h**  <_DB\_ADDRESS_\>  **-P**  <_DB\_PORT_\>  **-r**  <_BACKUP\_FILE_\>

    For details on the parameters in the preceding command, see  [2](#li16251172911136).

    Enter the database password as prompted.

    Example:

    **mysqldump --databases rdsdb --single-transaction --hex-blob --set-gtid-purged=OFF --no-create-info --skip-triggers -u root -p -h 192.168.151.18 -P  **8635**  -r dump-data.sql**

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use mysqldump with a version earlier than 5.6, remove  **--set-gtid-purged=OFF**  before running this command.  

    After this command is executed, a  **dump-data.sql**  file will be generated as follows:

    ```
    [rds@localhost ~]$ ll dump-data.sql
    -rw-r-----. 1 rds rds 2714 Sep 21 08:23 dump-data.sql
    ```


## Importing Data<a name="section9816229161211"></a>

This section describes how to use an ECS or a device that can access RDS to connect to a DB instance and import the exported SQL file into RDS.

>![](/images/icon-notice.gif) **NOTICE:**   
>If the source database contains triggers, storage processes, functions, or event invocation, you must set  **log\_bin\_trust\_function\_creators**  to  **ON**  for the destination database before importing data.  

1.  Import metadata into RDS.

    Use the mysql tool to connect to the RDS DB instance, enter the password, and run the following command to import metadata:

    \#  **mysql -f -h** _<RDS\_ADDRESS\>_ **-P**  <_DB\_PORT_\>  **-u**  root  **-p < **_<BACKUP\_DIR\>_**/dump-defs.sql**

    -   **_RDS\_ADDRESS_**  indicates the IP address of the RDS DB instance.
    -   **_DB\_PORT_**  indicates the RDS DB instance port.
    -   **_BACKUP\_DIR_**  indicates the directory where  **dump-defs.sql**  is stored.

    Example:

    **\# mysql -f -h 172.16.66.198 -P 3306 -u root -p < dump-defs.sql**

    **Enter password:**

2.  Import data into RDS.

    \#  **mysql -f -h** _<RDS\_ADDRESS\>_ **-P**  <_DB\_PORT_\>  **-u**  root  **-p** **< **_<BACKUP\_DIR\>_**/dump-data.sql**

    -   **_RDS\_ADDRESS_**  indicates the IP address of the RDS DB instance.
    -   **_DB\_PORT_**  indicates the RDS DB instance port.
    -   **_BACKUP\_DIR_**  indicates the directory where  **dump-data.sql**  is stored.

    Example:

    **\# mysql -f -h 172.16.66.198 -P 3306 -u root -p < dump-data.sql**

    **Enter password:**

3.  View the import result.

    **mysql\> show databases;**

    In this example, the database named  **my\_db**  has been imported.

    ```
    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | my_db              |
    | mysql              |
    | performance_schema |
    +--------------------+
    4 rows in set (0.00 sec)
    ```


