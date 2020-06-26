# Using a Client to Execute Query Statements<a name="EN-US_TOPIC_0221415075"></a>

You can perform an interactive query on an MRS cluster client. For clusters with Kerberos authentication enabled, users who submit topologies must belong to the  **presto**  group.

## Prerequisites<a name="s26390c77824e48628302cd27728a109b"></a>

-   The password of user  **admin**  has been obtained. The password of user  **admin**  is specified by you during MRS cluster creation.
-   The client has been updated.

## Procedure<a name="section15757123718144"></a>

1.  <a name="li9368161132311"></a>Log in to MRS Manager of a cluster with Kerberos authentication enabled, create a user in the  **presto**  group or use user  **admin**  to download the user authentication file. For details, see  [Creating a User](creating-a-user.md)  and  [Downloading a User Authentication File](downloading-a-user-authentication-file.md).
2.  <a name="li861292619304"></a>Upload the downloaded  **user.keytab**  and  **krb5.conf**  files to the node where the MRS client resides.

    >![](/images/icon-note.gif) **NOTE:**   
    >For clusters with Kerberos authentication enabled,  [1](#li9368161132311)  and  [2](#li861292619304)  must be performed. For normal clusters, start from  [3](#l6bafa992ef354ebc8c1e16387160ae24).  

3.  <a name="l6bafa992ef354ebc8c1e16387160ae24"></a>Log in to the node where the client is installed.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Updating the Client](updating-the-client.md).

4.  Run the following command to switch the user:

    **sudo su - omm**

5.  Run the following command to switch to the client directory, for example,  **/opt/client**.

    **cd /opt/client**

6.  Run the following command to configure environment variables:

    **source bigdata\_env**

7.  Connect to the Presto Server. The following provides two client connection methods based on the client type.
    -   Using the client provided by MRS
        -   For clusters with Kerberos authentication disabled, run the following command to connect to the Presto Server of the cluster:

            **presto\_cli.sh**

        -   For clusters with Kerberos authentication disabled, run the following command to connect to the Presto Server of other clusters. In the command,  **ip**  indicates the Presto Server IP address of the cluster, and  **port**  indicates the Presto Server port number. The default port is  **7520**.

            **presto\_cli.sh --server  _http://ip:port_**

        -   For clusters with Kerberos authentication enabled, run the following command to connect to the Presto Server of the cluster:

            **presto\_cli.sh --krb5-config-path  _krb5.conf file path_  --krb5-principal  _User's principal_  --krb5-keytab-path  _user.keytab file path_**

        -   For clusters with Kerberos authentication enabled, run the following command to connect to the Presto Server of other clusters. In the command,  **ip**  indicates the Presto Server IP address of the cluster, and  **port**  indicates the Presto Server port number. The default port is  **7521**.

            **presto\_cli.sh --krb5-config-path  _krb5.conf file path_  --krb5-principal  _User's principal_  --krb5-keytab-path  _user.keytab file path_   --server  _https://ip:port_  --krb5-remote-service-name  _Presto Server name_**

    -   Using the native client

        The native client of Presto is  **Presto/presto/bin/presto**  in the client directory. For details about how to use the client, see  [https://prestodb.io/docs/0.215/installation/cli.html](https://prestodb.io/docs/0.215/installation/cli.html)  and  [https://prestodb.io/docs/0.215/security/cli.html](https://prestodb.io/docs/0.215/security/cli.html).

8.  Run a query statement, for example,  **show catalogs**. For more statements, see  [https://prestodb.io/docs/0.215/sql.html](https://prestodb.io/docs/0.215/sql.html).

    >![](/images/icon-note.gif) **NOTE:**   
    >For clusters with Kerberos authentication enabled, when querying  **Hive Catalog**  data, the user who runs the Presto client must have the permission to access Hive tables and run the  **grant all on table \[table\_name\] to group hive**  command in Hive beeline to grant permissions to the Hive group.  

9.  After the query is complete, run the following command to exit the client:

    **quit**


