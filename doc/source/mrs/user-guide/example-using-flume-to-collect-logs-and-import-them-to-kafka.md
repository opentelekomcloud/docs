# Example: Using Flume to Collect Logs and Import Them to Kafka<a name="EN-US_TOPIC_0125375454"></a>

## Scenario<a name="s9ead5033231f41659c1fba8beeeb3d32"></a>

This section describes how to use Flume to import log information to Kafka.

## Prerequisites<a name="sed9287e8b0104e429f51c24058276e3e"></a>

-   A streaming cluster with Kerberos authentication enabled has been created.
-   The Flume client has been installed on the node where logs are generated. For details, see  [Installing the Flume Client](installing-the-flume-client.md).
-   The streaming cluster can properly communicate with the node where logs are generated.

## **Procedure**<a name="sa75fada4826d4362b079264fb19a5e93"></a>

>![](/images/icon-note.gif) **NOTE:**   
>Start from Step 7 for a non-security cluster.  

1.  Copy the configuration file of the authentication server from the Master1 node to the  **conf**  directory on the Flume client node.
    -   In versions earlier than MRS 1.9.2, the full path of the file is  **/opt/Bigdata/FusionInsight/etc/1\_X\_KerberosClient/kdc.conf**
    -   For MRS 1.9.2 or later, the full path of the file is  **/opt/Bigdata/MRS\_Current/1\_X\_KerberosClient/etc/kdc.conf**

        **XXX**  is MRS version and  **X** is a random number. The file must be saved by the user who installs the Flume client, for example, user **root**.

2.  Log in to MRS Manager. Choose  **Service**  \>  **Flume**  \>  **Instance**. Query the **Business IP Address**  of any node on which the Flume role is deployed.
3.  Copy the user authentication file from this node to the  **conf**  directory on the Flume client node.
    -   In versions earlier than MRS 1.9.2, the full path of the file is  **/opt/Bigdata/FusionInsight/FusionInsight-Flume-1.6.0/flume/conf/flume.keytab**
    -   For MRS 1.9.2 or later, the full path of the file is  /opt/Bigdata/MRS\_XXX/install/FusionInsight-Flume-1.6.0/flume/conf/flume.keytab

        **XXX**  is MRS version. The file must be saved by the user who installs the Flume client, for example, user **root**.

4.  Copy the  **jaas.conf** file from this node to the **conf**  directory on the Flume client node.
    -   In versions earlier than MRS 1.9.2, the full path of the file is  **/opt/Bigdata/FusionInsight/etc/1\_X\_Flume/jaas.conf**
    -   For MRS 1.9.2 or later, the full path of the file is  /opt/Bigdata/MRS\_Current/1\_X\_Flume/etc/jaas.conf

        **XXX**  is MRS version and  **X** is a random number. The file must be saved by the user who installs the Flume client, for example, user **root**.

5.  Log in to the Flume client node and go to the client installation directory. Run the following command to edit the file:

    **vi conf/jaas.conf**

    Set the  **keyTab**  parameter to the full path of the user authentication file on the Flume client. Then save and exit the file.

6.  Run the following command to modify the  **flume-env.sh**  configuration file of the Flume client:

    **vi** _Flume client installation directory_**/fusioninsight-flume-1.6.0/conf/flume-env.sh**

    Add the following information after  **-XX:+UseCMSCompactAtFullCollection**:

    ```
    -Djava.security.krb5.conf=Flume client installation directory/fusioninsight-flume-1.6.0/conf/kdc.conf -Djava.security.auth.login.config=Flume client installation directory/fusioninsight-flume-1.6.0/conf/jaas.conf -Dzookeeper.server.principal=zookeeper/hadoop.xxx.com -Dzookeeper.request.timeout=120000
    ```

    Change  _Flume client installation directory_ to the actual one and modify  **zookeeper.server.principal**. Then save and exit the file.

7.  Assume that the Flume client is installed in  **/opt/FlumeClient**. Run the following commands to restart the Flume client:

    **cd /opt/FlumeClient/fusioninsight-flume-1.6.0/bin**

    **./flume-manage.sh restart**

8.  Run the following command to modify the  **properties.properties**  configuration file of the Flume client:

    **vi** _Flume client installation directory_**/fusioninsight-flume-1.6.0/conf/properties.properties**

    Add the following information to the file:

    ```
    #########################################################################################
    client.sources = static_log_source  
    client.channels = static_log_channel 
    client.sinks = kafka_sink
    #########################################################################################
    #LOG_TO_HDFS_ONLINE_1
    
    client.sources.static_log_source.type = spooldir
    client.sources.static_log_source.spoolDir = PATH
    client.sources.static_log_source.fileSuffix = .COMPLETED
    client.sources.static_log_source.ignorePattern = ^$
    client.sources.static_log_source.trackerDir = PATH
    client.sources.static_log_source.maxBlobLength = 16384
    client.sources.static_log_source.batchSize = 51200
    client.sources.static_log_source.inputCharset = UTF-8
    client.sources.static_log_source.deserializer = LINE
    client.sources.static_log_source.selector.type = replicating
    client.sources.static_log_source.fileHeaderKey = file
    client.sources.static_log_source.fileHeader = false
    client.sources.static_log_source.basenameHeader = true
    client.sources.static_log_source.basenameHeaderKey = basename
    client.sources.static_log_source.deletePolicy = never
    
    client.channels.static_log_channel.type = file
    client.channels.static_log_channel.dataDirs = PATH
    client.channels.static_log_channel.checkpointDir = PATH
    client.channels.static_log_channel.maxFileSize = 2146435071
    client.channels.static_log_channel.capacity = 1000000
    client.channels.static_log_channel.transactionCapacity = 612000
    client.channels.static_log_channel.minimumRequiredSpace = 524288000
    
    client.sinks.kafka_sink.type = org.apache.flume.sink.kafka.KafkaSink
    client.sinks.kafka_sink.kafka.topic = flume_test
    client.sinks.kafka_sink.kafka.bootstrap.servers = XXX.XXX.XXX.XXX:21007,XXX.XXX.XXX.XXX:21007,XXX.XXX.XXX.XXX:21007
    client.sinks.kafka_sink.flumeBatchSize = 1000
    client.sinks.kafka_sink.kafka.producer.type = sync
    client.sinks.kafka_sink.kafka.security.protocol  = SASL_PLAINTEXT
    client.sinks.kafka_sink.kafka.kerberos.domain.name = hadoop.XXX.com
    client.sinks.kafka_sink.requiredAcks = 0
    
    client.sources.static_log_source.channels = static_log_channel
    client.sinks.kafka_sink.channel = static_log_channel
    ```

    Modify the following parameters as required. Then save and exit the file.

    -   **spoolDir**
    -   **trackerDir**
    -   **dataDirs**
    -   **checkpointDir**
    -   **topic**

        If the topic does not exist in Kafka, it will be automatically created by default.

    -   **kafka.bootstrap.servers**

        By default, the port for a security cluster is port 21007 and that for a non-security cluster is port 21005.

    -   **kafka.kerberos.domain.name**

        This parameter value is the value of  **default\_realm**  of kerberos in the Kafka cluster.

9.  The Flume client automatically loads the information in the  **properties.properties**  file.

    After new log files are generated in the directory specified by  **spoolDir**, the logs will be sent to Kafka producers and can be consumed by Kafka consumers.


