# Migrating PostgreSQL Data Using psql<a name="en-us_topic_0029128106"></a>

## Preparing for Data Migration<a name="section182818561660"></a>

PostgreSQL  supports logical backups. You can use the  pg\_dump  logical backup function to export backup files and then import them to RDS using psql.

You can access RDS DB instances through an EIP or ECS.

## **Preparations**<a name="section15764126154156"></a>

1.  <a name="li61751156194257"></a>Prepare an ECS for accessing DB instances in the same VPC subnet or prepare a device for accessing RDS through a public network.
    -   To connect to a DB instance through an ECS, you must first create an ECS.

        For details about how to create and connect to an ECS, see  [How Can I Create and Connect to an ECS?](how-can-i-create-and-connect-to-an-ecs.md)

    -   To connect to a DB instance through an EIP, you must:
        1.  Bind the EIP to the DB instance. For details, see  [Binding an EIP](binding-and-unbinding-an-eip.md#section3199593620428).
        2.  Ensure that the local device can access the EIP that has been bound to the DB instance.

2.  Install the PostgreSQL client on the ECS or device that was prepared in  [step 1](#li61751156194257).

    For details, see  [How Can I Install the PostgreSQL Client?](how-can-i-install-the-postgresql-client.md)

    >![](/images/icon-note.gif) **NOTE:**   
    >The PostgreSQL client version must be the same as the version of RDS for PostgreSQL. The PostgreSQL database or client will provide pg\_dump and psql.  


## Exporting Data<a name="section859519371476"></a>

Before migrating an existing PostgreSQL database to RDS, you need to export the PostgreSQL database.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   The export tool must match the DB engine version.  
>-   Database migration is performed offline. Before the migration, you must stop any applications using the source database.  

1.  Log in to the prepared ECS or device that can access RDS DB instances.
2.  Use the pg\_dump tool to export the source database into an SQL file.

    **pg\_dump** **--username=**_<DB\_USER\>_**_ _--host=**_<DB\_ADDRESS\>_** --port=**_<DB\_PORT\> _**--format=plain --file=**_<BACKUP\_FILE\>_ _<DB\_NAME\>_

    -   **_DB\_USER_**  indicates the database username.
    -   **_DB\_ADDRESS_**  indicates the database address.
    -   **_DB\_PORT_**  indicates the database port.
    -   **_BACKUP\_FILE_**  indicates the name of the file to which the data will be exported.
    -   **_DB\_NAME_**  indicates the name of the database to be migrated.

    Enter the database password as prompted.

    Example:

    **$ pg\_dump --username=root --host=192.168.151.18 --port=**5432**  --format=plain --file=backup.sql my\_db**

    **Password for user root:**

    After this command is executed, a  **backup.sql**  file will be generated as follows:

    \[rds@localhost \~\]$ ll backup.sql

    ```
    -rw-r-----. 1 rds rds 2714 Sep 21 08:23 backup.sql
    ```


## Importing Data<a name="section113968181188"></a>

This section describes how to use an ECS or a device that can access RDS to connect to a DB instance and import the exported SQL file into RDS.

1.  Ensure that the destination database to which data is to be imported exists.

    If the destination database does not exist, run the following command to create a database:

    **\# psql --host=**_<RDS\_ADDRESS\>_ **--port=**<_DB\_PORT_\>  **--username=**_root_ **--dbname=postgres** **-c **"**create database** _<DB\_NAME\>_;"

    -   **_RDS\_ADDRESS_**  indicates the IP address of the RDS DB instance.
    -   **_DB\_PORT_**  indicates the RDS DB instance port.
    -   **_DB\_NAME_**  indicates the name of the database to be imported.

2.  Import the exported file into RDS.

    **\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--username=**_root_ **--dbname=**_<DB\_NAME\>_ **--file=**_<BACKUP\_DIR\>_/backup.sql

    -   **_RDS\_ADDRESS_**  indicates the IP address of the RDS DB instance.
    -   **_DB\_PORT_**  indicates the RDS DB instance port.
    -   **_DB\_NAME_**  indicates the name of the database to which data is to be imported. Ensure that the database exists.
    -   **_BACKUP\_DIR_**  indicates the directory where the  **backup.sql**  file is stored.

    Enter the password for the RDS DB instance as prompted.

    Example:

    **\# psql --host=172.16.66.198 --port=****5432****  --username=root --dbname=my\_db --file=backup.sql**

    **Password for user root:**

3.  View the import result.

    **my\_db=\> \\l my\_db**

    In this example, the database named  **my\_db**  has been imported.

    ```
    my_db=> \l my_db
    List of databases
    Name  | Owner | Encoding | Collate     | Ctype       | Access privileges
    ------+-------+----------+-------------+-------------+-----------
    my_db | root  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
    (1 row)
    ```


