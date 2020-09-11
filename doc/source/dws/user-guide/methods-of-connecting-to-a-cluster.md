# Methods of Connecting to a Cluster<a name="en-us_topic_0056326005"></a>

If you have created a data warehouse cluster, you can use the SQL client tool or a third-party driver such as JDBC and ODBC to connect to the cluster and access the database in the cluster.

The procedure for connecting to a cluster is as follows:

1.  [Obtaining the Cluster Connection Address](obtaining-the-cluster-connection-address.md)
2.  If SSL encryption is used, perform the following steps:
    1.  [Configuring SSL Connection](configuring-ssl-connection.md)
    2.  [Downloading the SSL Certificate File](downloading-the-ssl-certificate-file.md)

3.  Connect to the cluster and access the database in the cluster. You can choose any one of the following methods to connect to a cluster:
    -   Use the SQL client tool to connect to the cluster.
        -   [Using the gsql Client to Connect to a Cluster](using-the-gsql-client-to-connect-to-a-cluster.md)
        -   [Using pgAdmin to Connect to a Cluster](using-pgadmin-to-connect-to-a-cluster.md)
        -   [Using the Data Studio GUI Client to Connect to a Cluster](using-the-data-studio-gui-client-to-connect-to-a-cluster.md)

    -   Use JDBC, ODBC, and psycopg2 third-party drivers to connect to the cluster.
        -   [Using a JDBC Driver to Connect to the Database](using-a-jdbc-driver-to-connect-to-the-database.md)
        -   [Using an ODBC Driver to Connect to the Database](using-an-odbc-driver-to-connect-to-the-database.md)
        -   [Using the Third-Party Function Library psycopg2 of Python to Connect to a Cluster](using-the-third-party-function-library-psycopg2-of-python-to-connect-to-a-cluster.md)
        -   [Configuring the JDBC Connection to Connect to a Cluster Using IAM Authentication](overview.md)



