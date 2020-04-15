# Functions<a name="dws_01_0091"></a>

DWS provides you with various methods of using this service, such as the DWS management console, DWS client, and REST APIs. This section describes the main functions of DWS.

## Cluster Management<a name="section158601494244"></a>

A data warehouse cluster contains nodes with the same flavor in the same subnet. These nodes jointly provide services. DWS provides a professional, efficient, and centralized management console, allowing you to quickly apply for clusters, easily manage data warehouses, and focus on data and services.

Main functions of cluster management are described as follows:

-   Creating clusters

    You can specify the node quantity and node type based on service requirements to quickly create a cluster or purchase prepaid nodes and create a cluster.

-   Managing snapshots

    A snapshot is a complete backup that records point-in-time configuration data and service data of a data warehouse cluster. A snapshot can be used to restore a cluster at a certain point in time. You can manually create snapshots for a cluster or enable automatic snapshot creation \(periodic\). Automatic snapshots have a limited retention period. You can copy automatic snapshots to generate manual snapshots for long-term retention.

    When you restore a cluster from a snapshot, the system creates a new cluster with the same flavor and node quantity as the original one, and imports the snapshot data.

    You can delete snapshots that are no longer needed to release the storage space.

-   Scaling out clusters

    As the service volume increases, the current scale of a cluster may not meet service requirements. In this case, you can scale out the cluster by adding compute nodes to it. Services are not interrupted during the scale-out.

-   Restarting clusters

    Restarting a cluster may cause data loss in running services. If you have to restart a cluster, ensure that there is no running service and all data has been saved.

-   Deleting clusters

    You can delete a cluster when you do not need it. Deleting a cluster is risky and may cause data loss. Therefore, exercise caution when performing this operation.


DWS allows you to manage clusters and snapshots in either of the following ways:

-   Management console

    Use the management console to access data warehouse clusters. After you have registered a public cloud account, log in to the management console and choose  **Data Warehouse Service**.

    For more information about cluster management, see section  [Managing Clusters](managing-clusters.md).

-   REST APIs

    Use REST APIs provided by DWS to manage clusters. If you need to integrate DWS into a third-party system for secondary development, use APIs to access the service.

    For details, see the  [Data Warehouse Service API Reference](https://docs.otc.t-systems.com/en-us/api/dws/dws_02_0033.html).


## Enterprise-Class Data Warehouses and Compatibility with Standard SQL<a name="section186951149175617"></a>

After a data warehouse cluster is created, you can use the SQL client to connect to the cluster and perform operations such as creating a database, managing the database, importing and exporting data, and querying data.

DWS provides petabyte-level \(PB-level\) high-performance databases with the following features:

-   MPP computing framework, hybrid row-column storage, and vectorized execution, enabling response to billion-level data correlation analysis within seconds
-   Optimized in-memory computing based on Hash Join of Bloom Filter, improving the performance by 2 to 10 times

-   Optimized communication between large-scale clusters based on telecommunication technologies, improving data transmission efficiency between compute nodes
-   Cost-based intelligent optimizers, helping generate the optimal plan based on the cluster scale and data volume to improve execution efficiency

DWS has comprehensive SQL capabilities:

-   Supports SQL 92 and SQL 2003 standards, stored procedures, GBK and UTF-8 character sets, and SQL standard functions and OLAP analysis functions.
-   Compatible with the PostgreSQL ecosystem and supports interconnection with mainstream database Extract-Transform-Load \(ETL\) and Business Intelligence \(BI\) tools provided by third-party vendors.

For details about the SQL syntax and database operation guidance, see the  [Data Warehouse Service Database Developer Guide](https://docs.otc.t-systems.com/en-us/dws/index.html).

## Diverse Data Import Modes<a name="section275112712410"></a>

DWS supports efficient data import from multiple data sources. The following lists typical data import modes. For details, see  **Data Import**  in the  [Data Warehouse Service Database Developer Guide](https://docs.otc.t-systems.com/en-us/dws/index.html).

-   Using Object Storage Service \(OBS\) for data import and export
-   Using General Data Service \(GDS\) to import and export data
-   Running the  **INSERT**  statement to insert data
-   Running the  **COPY FROM STDIN**  statement to write data to DWS tables
-   Importing data from MapReduce Service \(MRS\) to DWS

In addition, DWS supports data import using mainstream third-party ETL tools.

## Application Programming Interfaces<a name="section1261249165818"></a>

You can call standard interfaces, such as Java Database Connectivity \(JDBC\), Open Database Connectivity \(ODBC\), Python, and third-party psycopg2 to access databases in clusters.

For details, see sections  [Using the JDBC and ODBC Drivers to Connect to the Cluster](using-the-jdbc-and-odbc-drivers-to-connect-to-the-cluster.md)  and  [Using the Third-Party Function Library psycopg2 of Python to Connect to a Cluster](using-the-third-party-function-library-psycopg2-of-python-to-connect-to-a-cluster.md).

## High Reliability<a name="section1516285819583"></a>

-   Supports instance and data redundancy, ensuring zero single points of failure \(SPOF\) in the entire system.
-   Supports multiple data backups, and all data can be manually backed up to OBS.
-   Automatically isolates the faulty node, uses the backup to restore data, and replaces the faulty node when necessary.
-   Combines automatic snapshot creation and OBS storage, implementing cross-AZ disaster recovery \(DR\).

## Security Management<a name="section139161462009"></a>

-   Isolates tenants and controls access permissions to protect the privacy and data security of systems and users based on the network isolation and security group rules and security hardening measures.
-   Supports SSL Internet connections, user permission management, and password management, ensuring data security at the Internet, management, application, and system layers.

    For details, see sections  [Configuring SSL Connection](configuring-ssl-connection.md)  and  [Separating Rights of Roles](separating-rights-of-roles.md).


## Monitoring and Auditing<a name="section17618481497"></a>

-   Monitoring Clusters

    DWS integrates with Cloud Eye, allowing you to monitor compute nodes and databases in the cluster in real time. For details, see section  [Monitoring a Cluster](monitoring-a-cluster.md).

-   Audit Logs
    -   DWS integrates with Cloud Trace Service \(CTS\), allowing you to audit operations performed on the management console and API invocation operations. For details, see section  [Viewing Audit Logs of Key Operations on the Management Console](viewing-audit-logs-of-key-operations-on-the-management-console.md).
    -   DWS records all SQL operations, including connection attempts, query attempts, and database changes. For details, see section  [Configuring the Database Audit Log](configuring-the-database-audit-log.md).


## Multiple Database Tools<a name="section138816277512"></a>

DWS provides the following self-developed tools. You can download corresponding tool packages on the DWS management console. For details about how to use the tools, see the .

-   gsql tool

    gsql is a command line SQL client tool running on the Linux OS. It is used to connect to the database in a data warehouse cluster and operate and maintain the database.

-   Data Studio tool

    Data Studio is a Graphical User Interface \(GUI\) SQL client tool running on the Windows OS. It is used to connect to the database in a data warehouse cluster, manage the database and database objects, edit, run, and debug SQL scripts, and view the execution plans.

-   GDS tool

    GDS is a data service tool provided by DWS. It works with the foreign table mechanism to implement high-speed data import and export.

    The GDS tool package needs to be installed on the server where the data source file is located. This server is called the data server or the GDS server.


