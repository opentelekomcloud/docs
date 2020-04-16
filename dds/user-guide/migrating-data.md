# Migrating Data<a name="dds_03_0052"></a>

## **Scenarios**<a name="section25341248175518"></a>

DDS supports access through EIPs by enabling public accessibility. You can also access a database through an ECS in the private network.

Before migrating data from a  MongoDB database  to DDS, transfer data to a .json file using the mongoexport tool. This section guides you on how to import the data from the JSON files to DDS using the mongoimport tool on the ECS or the device that can access DDS.

## **Preparations**<a name="section8361919133059"></a>

1.  An ECS or a device that can access DDS is ready for use.
    -   To connect to a  DDS DB instance  from an ECS, you need to create and log in to the ECS. For details, see  [How Can I Create and Log In to an ECS?](how-can-i-create-and-log-in-to-an-ecs.md)
    -   To bind an EIP to a  DB instance:
        1.  Bind an EIP to a node in the DB instance. For details about how to bind an EIP to a node, see "Binding and Unbinding an EIP" in section "Cluster" or "Replica Set".
        2.  Ensure that your local device can access the EIP that has been bound to the DB instance.

2.  A migration tool has been installed on the prepared ECS or the device.

    For details on how to install the migration tool, see  [How Can I Install a MongoDB Client?](how-can-i-install-a-mongodb-client.md)

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The MongoDB client provides the mongoexport and mongoimport tools.  


## Exporting Data<a name="section990018367329"></a>

1.  Log in to the ECS or the device that can access DDS.
2.  Use the mongoexport tool to transfer data from the source database to a .json file.

    The SSL connection is used as an example. If you select a common connection, delete  **--ssl --sslAllowInvalidCertificates**  from the following command.

    ./**mongoexport** **--host** _<__DB\_ADDRESS\>_ **_--_port** _<DB\_PORT\>_ **_--_ssl** **--sslAllowInvalidCertificates** **--type json** **--authenticationDatabase** _<AUTH\_DB_\>  **-u** _<DB\_USER\>_ **--db**  <_DB\_NAME_\>  **--collection**  <_DB\_COLLECTION_\>  **--out**  <_DB\_PATH_\>

    -   **DB\_ADDRESS**  indicates the database address.
    -   **DB\_PORT**  indicates the database port.
    -   **AUTH\_DB**  indicates the database for storing DB\_USER information. Generally, this value is  **admin**.
    -   **DB\_USER**  indicates the database user.
    -   **DB\_NAME**  indicates the name of the database from which data will be exported.
    -   **DB\_COLLECTION**  indicates the collection of the database from which data will be exported.
    -   **DB\_PATH**  indicates the path where the .json file is located.

    Enter the database administrator password when prompted:

    ```
    Enter password:
    ```

    The following is an example. After the command is executed, the  **exportfile.json**  file will be generated:

    **./mongoexport --host 192.168.1.21 --port 8635 --ssl --sslAllowInvalidCertificates  --type json  --authenticationDatabase admin -u rwuser --db test02 --collection Test --out /tmp/mongodb/export/exportfile.json**

3.  Check the result.

    If information similar to the following is displayed, the data is successfully exported.  **x**  indicates the number of exported data records.

    ```
    exported x records
    ```

4.  Compress the exported .json file.

    **gzip exportfile.json**

    Compressing the file helps reduce the time needed to transmit all the data. The compressed file is  **exportfile.json.gz**.


## Importing Data<a name="section5895195683218"></a>

1.  Log in to the ECS or the device that can access DDS.
2.  Upload the data to be imported to the ECS or the device that can access DDS.

    Select an uploading method based on the OS you are using. In Linux, for example, run the following command:

    scp  _<__IDENTITY\_FILE\>_ _<REMOTE\_USER\>_@_<REMOTE\_ADDRESS\>_:_<REMOTE\_DIR\>_

    -   **IDENTITY\_FILE**  indicates the directory where the  **exportfile.json.gz**  file is located. The file access permission is 600.
    -   **REMOTE\_USER**  indicates the ECS OS user.
    -   **REMOTE\_ADDRESS**  indicates the ECS address.
    -   **REMOTE\_DIR**  indicates the directory of the ECS to which the  **exportfile.json.gz**  file is uploaded.

    In Windows, upload  **exportfile.json.gz**  to the ECS using file transfer tools.

3.  Decompress the package.

    **gzip** **-d** _exportfile.json.gz_

4.  Import the JSON file to the DDS database.

    The SSL connection is used as an example. If you select a common connection, delete  **--ssl --sslAllowInvalidCertificates**  from the following command.

    ./**mongoimport --host**  <_DB\_ADDRESS_\>  **--port**  <_DB\_PORT_\>  **--ssl --sslAllowInvalidCertificates --type json --authenticationDatabase**  <_AUTH\_DB_\>  **-u**  <_DB\_USER_\>  **--db**  <_DB\_NAME_\>  **--collection**  <_DB\_COLLECTION_\>  **--file**  <_DB\_PATH_\>

    -   **DB\_ADDRESS**  indicates the DB instance IP address.
    -   **DB\_PORT**  indicates the database port.
    -   **AUTH\_DB**  indicates the database that authenticates DB\_USER. Generally, this value is  **admin**.
    -   **DB\_USER**  indicates the account name of the database administrator.
    -   **DB\_NAME**  indicates the name of the database to which data will be imported.
    -   **DB\_COLLECTION**  indicates the collection of the database to which data will be imported.
    -   **DB\_PATH**  indicates the path where the .json file is located.

    Enter the database administrator password when prompted:

    ```
    Enter password:
    ```

    The following is an example:

    **./mongoimport --host 192.168.1.21 --port 8635 --ssl --sslAllowInvalidCertificates   --type json  --authenticationDatabase admin -u rwuser --db test02 --collection Test --file /tmp/mongodb/export/exportfile.json**

5.  Check the result.

    If information similar to the following is displayed, the data is successfully imported.  **x**  indicates the number of imported data records.

    ```
    imported x records
    ```


