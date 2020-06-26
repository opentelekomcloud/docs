# Using an MRS Client to Operate OpenTSDB Metric Data<a name="EN-US_TOPIC_0221415085"></a>

You can perform an interactive operation on an MRS cluster client. For a cluster with Kerberos authentication enabled, the user must belong to the  **opentsdb**,  **hbase**,  **opentsdbgroup**, and  **supergroup**  groups and have the HBase permission.

## Prerequisites<a name="section482010192610"></a>

-   The password of user  **admin**  has been obtained. The password of user  **admin**  is specified by you during MRS cluster creation.
-   The client has been updated. For details, see  [Updating the Client](updating-the-client.md).

## Using the Client<a name="section137578192714"></a>

1.  If Kerberos authentication is enabled for the current cluster, log in to MRS Manager and create a user that belongs to the  **opentsdb**,  **hbase**,  **opentsdbgroup**, and  **supergroup**  groups and has the HBase permission, for example,  **opentsdbuser**. If Kerberos authentication is disabled for the current cluster, skip this step.
2.  Log in to the node where the client is installed.

    For example, if you have updated the client on the Master2 node, log in to the Master2 node to use the client. For details, see  [Updating the Client](updating-the-client.md).

3.  Run the following command to switch the user:

    **sudo su - omm**

4.  Run the following command to switch to the client directory, for example,  **/opt/client**.

    **cd /opt/client**

5.  Run the following command to configure environment variables:

    **source bigdata\_env**

6.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate the user. If Kerberos authentication is disabled for the current cluster, skip this step.
    -   If the user is a human-machine user, run the  **kinit opentsdbuser**  command to authenticate the user.
    -   If the user is a machine-machine user, download the user authentication credential file, and save and decompress it to obtain the user's  **user.keytab**  and  **krb5.conf**  files. Go to the decompressed  **user.keytab**  directory, and run the  **kinit -kt user.keytab opentsdbuser**  command to authenticate the user.

7.  Operate the OpenTSDB data. For details, see  [Operating Data](#section46629451460).

## Operating Data<a name="section46629451460"></a>

-   Viewing help information

    Run the  **tsdb**  command to print all commands supported by OpenTSDB, for example,  **fsck**,  **import**,  **mkmetric**,  **query**,  **tsd**,  **scan**,  **search**,  **uid**, and  **version**.

    Command output:

    ```
    tsdb: error: unknown command ''
    usage: tsdb <command> [args]
    Valid commands: fsck, import, mkmetric, query, tsd, scan, search, uid, version
    ```

-   Creating an OpenTSDB metric

    Run the  **tsdb mkmetric**  command to create a metric. For example, run the  **tsdb mkmetric sys.cpu.user**  command to create a metric named  **sys.cpu.user**.

    Command output:

    ```
    Start run net.opentsdb.tools.UidManager, args: assign metrics sys.cpu.user
    metrics sys.cpu.user: [0, 0, 6]
    ```

-   Importing data to the OpenTSDB metric
    1.  Prepare a metric file, for example, the  **importData.txt**  file that contains following information.

        sys.cpu.user 1356998400 41 host=web01 cpu=0

        sys.cpu.user 1356998401 42 host=web01 cpu=0

        sys.cpu.user 1356998402 44 host=web01 cpu=0

        sys.cpu.user 1356998403 47 host=web01 cpu=0

        sys.cpu.user 1356998404 42 host=web01 cpu=0

        sys.cpu.user 1356998405 42 host=web01 cpu=0

    2.  Run the  **tsdb import**  command to import metric data. For example, run the  **tsdb import importData.txt**  command to import the  **importData.txt**  file.

        ```
        Start run net.opentsdb.tools.TextImporter, args: importData.txt
        2019-06-26
        15:45:22,091 INFO  [main] TextImporter:
        reading from file:importData.txt
        2019-06-26
        15:45:22,102 INFO  [main] TextImporter:
        Processed importData.txt in 11 ms, 6 data points (545.5 points/s)
        2019-06-26
        15:45:22,102 INFO  [main] TextImporter:
        Total: imported 6 data points in 0.012s (504.0 points/s)
        ```


-   Querying the OpenTSDB metric

    Run the  **tsdb uid metrics**  command to obtain the metric stored in OpenTSDB. For example, run the  **tsdb uid metrics sys.cpu.user**  command to query the data of the  **sys.cpu.user**  metric.

    Command output:

    ```
    Start run net.opentsdb.tools.UidManager, args: metrics sys.cpu.user
    metrics sys.cpu.user: [0, 0, 6]
    ```

    To obtain more information, run the  **tsdb uid**  command.

    ```
    Start run net.opentsdb.tools.UidManager, args:
    Not enough arguments
    Usage: uid <subcommand> args
    Sub commands:
      grep [kind] <RE>: Finds matching IDs.
      assign <kind> <name> [names]: Assign an ID for the given name(s).
      rename <kind> <name> <newname>: Renames this UID.
      delete <kind> <name>: Deletes this UID.
      fsck: [fix] [delete_unknown] Checks the consistency of UIDs.
            fix            - Fix errors. By default errors are logged.
            delete_unknown - Remove columns with unknown qualifiers.
                             The "fix" flag must be supplied as well.
      [kind] <name>: Lookup the ID of this name.
      [kind] <ID>: Lookup the name of this ID.
      metasync: Generates missing TSUID and UID meta entries, updates created timestamps
      metapurge: Removes meta data entries from the UID table
      treesync: Process all timeseries meta objects through tree rules
      treepurge <id> [definition]: Purge a tree and/or the branches from storage. Provide an integer Tree ID and                                                       optionally add "true" to delete the tree definition
    Example values for [kind]: metrics, tagk (tag name), tagv (tag value).
      --config=PATH    Path to a configuration file (default: Searches for file see docs).
      --idwidth=N      Number of bytes on which the UniqueId is encoded.
      --ignore-case    Ignore case distinctions when matching a regexp.
      --table=TABLE    Name of the HBase table where to store the time series (default: tsdb).
      --uidtable=TABLE Name of the HBase table to use for Unique IDs (default: tsdb-uid).
      --verbose        Print more logging messages and not just errors.
      --zkbasedir=PATH Path under which is the znode for the -ROOT- region (default: /hbase).
      --zkquorum=SPEC  Specification of the ZooKeeper quorum to use (default: localhost).
      -i               Short for --ignore-case.
      -v               Short for --verbose.
    ```

-   Scanning the OpenTSDB metric data

    Run the  **tsdb query**  command to query the imported metric data in batches. The command format is as follows:  **_tsdb query <START-DATE\> <END-DATE\> <aggregator\> <metric\> <tagk=tagv\>_**. For example, run the  **tsdb query 0 1h-ago sum sys.cpu.user host=web01**  command.

    ```
    Start run net.opentsdb.tools.CliQuery, args: 0 1h-ago sum sys.cpu.user host=web01
    sys.cpu.user 1356998400000 41 {host=web01, cpu=0}
    sys.cpu.user 1356998401000 42 {host=web01, cpu=0}
    sys.cpu.user 1356998402000 44 {host=web01, cpu=0}
    sys.cpu.user 1356998403000 47 {host=web01, cpu=0}
    sys.cpu.user 1356998404000 42 {host=web01, cpu=0}
    sys.cpu.user 1356998405000 42 {host=web01, cpu=0}
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >**<START-DATE\>**: start time of the metric to be queried  
    >**<END-DATE\>**: end time of the metric to be queried  
    >**<aggregator\>**: aggregation mode of the data query  
    >**<metric\>**: name of the metric to be queried  
    >**<tagk=tagv\>**: key and value of a tag  

-   Deleting the imported OpenTSDB metric

    Run the  **tsdb uid delete**  command to delete the imported metric and its value. For example, to delete the  **sys.cpu.user**  metric, run the  **tsdb uid delete metrics sys.cpu.user**  command.

    ```
    Start run net.opentsdb.tools.UidManager, args: delete metrics sys.cpu.user
    ```


