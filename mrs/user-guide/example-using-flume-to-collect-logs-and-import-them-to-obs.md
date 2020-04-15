# Example: Using Flume to Collect Logs and Import Them to OBS<a name="EN-US_TOPIC_0125375345"></a>

## Scenario<a name="s6db336fdb41e413ab0311887a35779f3"></a>

This section describes how to use Flume to import log information to OBS.

## Prerequisites<a name="s610ca06f8b24496d92658fef9785ed67"></a>

-   A streaming cluster has been created.
-   The Flume client has been installed on the node where logs are generated. For details, see  [Installing the Flume Client](installing-the-flume-client.md).
-   The streaming cluster can properly communicate with the node where logs are generated.
-   The node where logs are generated can parse the domain name of OBS.

## Procedure<a name="se2a5c8bf5f1d4f7da9ad193add77e731"></a>

1.  Create the  **core-site.xml** file and save it to the **conf**  directory of the Flume client.

    An example of parameter file content is as follows:

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <configuration>
    <property>
    <name>fs.s3a.connection.ssl.enabled</name>
    <value>true</value>
    </property>
    <property>
    <name>fs.s3a.endpoint</name>
    <value></value>
    </property>
    </configuration>
    ```

    The value of  **fs.s3a.endpoint** is an OBS access address. The address must be in the same region as MRS. The parameter value can be either a domain name or an IP address. On MRS Manager, you can choose  **Service \> Flume \> Service Configuration**, set  **Type**  to  **All**, and view the value of  **s3service.s3-endpoint**  in S3service.

2.  Encrypt SK using the encryption tool of the Flume client. For details, see  [Using the Encryption Tool of the Flume Client](using-the-encryption-tool-of-the-flume-client.md).
3.  Run the following command to modify the  **properties.properties**  configuration file of the Flume client:

    **vi** **_conf_/fusioninsight-flume-1.6.0/conf/properties.properties**

    Add the following information to the file:

    ```
    client.sources = linux
    client.channels = flume
    client.sinks = obs
    
    client.sources.linux.type = spooldir
    client.sources.linux.spoolDir = /tmp/nemon
    client.sources.linux.montime = 
    client.sources.linux.fileSuffix = .COMPLETED
    client.sources.linux.deletePolicy = never
    client.sources.linux.trackerDir = .flumespool
    client.sources.linux.ignorePattern = ^$
    client.sources.linux.batchSize = 1000
    client.sources.linux.inputCharset = UTF-8
    client.sources.linux.selector.type = replicating
    client.sources.linux.fileHeader = false
    client.sources.linux.fileHeaderKey = file
    client.sources.linux.basenameHeader = true
    client.sources.linux.basenameHeaderKey = basename
    client.sources.linux.deserializer = LINE
    client.sources.linux.deserializer.maxBatchLine = 1
    client.sources.linux.deserializer.maxLineLength = 2048
    client.sources.linux.channels = flume
    
    client.channels.flume.type = memory
    client.channels.flume.capacity = 10000
    client.channels.flume.transactionCapacity = 1000
    client.channels.flume.channelfullcount = 10
    client.channels.flume.keep-alive = 3
    client.channels.flume.byteCapacity = 
    client.channels.flume.byteCapacityBufferPercentage = 20
    
    client.sinks.obs.type = hdfs
    client.sinks.obs.hdfs.path = s3a://AK:SK@obs-nemon-sink/obs-sink
    client.sinks.obs.montime = 
    client.sinks.obs.hdfs.filePrefix = obs_%{basename}
    client.sinks.obs.hdfs.fileSuffix = 
    client.sinks.obs.hdfs.inUsePrefix = 
    client.sinks.obs.hdfs.inUseSuffix = .tmp
    client.sinks.obs.hdfs.idleTimeout = 0
    client.sinks.obs.hdfs.batchSize = 1000
    client.sinks.obs.hdfs.codeC =  
    client.sinks.obs.hdfs.fileType = DataStream
    client.sinks.obs.hdfs.maxOpenFiles = 5000
    client.sinks.obs.hdfs.writeFormat = Writable
    client.sinks.obs.hdfs.callTimeout = 1000000
    client.sinks.obs.hdfs.threadsPoolSize = 10
    client.sinks.obs.hdfs.rollTimerPoolSize = 1
    client.sinks.obs.hdfs.round = false
    client.sinks.obs.hdfs.roundUnit = second
    client.sinks.obs.hdfs.useLocalTimeStamp = false
    client.sinks.obs.hdfs.failcount = 10
    client.sinks.obs.hdfs.fileCloseByEndEvent = true
    client.sinks.obs.hdfs.rollInterval = 30
    client.sinks.obs.hdfs.rollSize = 1024
    client.sinks.obs.hdfs.rollCount = 10
    client.sinks.obs.hdfs.batchCallTimeout = 0
    client.sinks.obs.serializer.appendNewline = true
    client.sinks.obs.channel = flume 
    ```

    Modify the following parameters as required. Then save and exit the file.

    -   **spoolDir**
    -   **trackerDir**
    -   **hdfs.path**  \(AK and SK in the path must be actual values. SK is the encrypted one.\)

4.  The Flume client automatically loads the information in the  **properties.properties**  file.

    After new log files are generated in the directory specified by  **spoolDir**, the logs will be sent to OBS.


