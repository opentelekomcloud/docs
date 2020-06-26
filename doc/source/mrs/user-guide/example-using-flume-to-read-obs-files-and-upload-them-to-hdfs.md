# Example: Using Flume to Read OBS Files and Upload Them to HDFS<a name="EN-US_TOPIC_0125375783"></a>

## Scenario<a name="sc8bcb12f0c1f4aa4a3ba20ca33090ff6"></a>

This section describes how to use Flume to read the specified OBS directory and upload files to HDFS.

## Prerequisites<a name="sa0417cadf6544b7c9fe0567b2cdc6ccf"></a>

-   A streaming cluster has been created.
-   The Flume client has been installed on the client node. For details, see  [Installing the Flume Client](installing-the-flume-client.md).
-   The client node can properly communicate with the streaming cluster and HDFS cluster nodes, including master and core nodes.
-   The client node can parse the domain name of OBS.

## Procedure<a name="s5d398f1ea58a41519826886af48be0d8"></a>

>![](/images/icon-note.gif) **NOTE:**   
>You do not need to perform Steps 2 to 4 for a non-security cluster.  

1.  Copy the  **core-site.xml** and **hdfs-site.xml** files from the HDFS cluster client to the **Flume client installation directory/fusioninsight-flume-1.6.0/conf**  directory of the Flume client node.

    Generally, the  **core-site.xml** and **hdfs-site.xml** files are saved in the **/HDFS/hadoop/etc/hadoop/**  HDFS client installation directory.

    The files must be saved as a Flume client installation user, for example, user  **root**.

2.  Download a user's authentication credential file from the HDFS cluster.
    1.  On MRS Manager, click  **System**.
    2.  In the  **Permission** area, click **Manage User**.
    3.  Select the user from the user list and click  **More**  to download the user's authentication credential file.
    4.  Decompress the authentication credential file to obtain the  **krb5.conf** and **user.keytab**  files.

3.  Copy the  **krb5.conf** and **user.keytab** files to the **Flume client installation directory/fusioninsight-flume-1.6.0/conf** directory of the Flume client node. The files must be saved as a Flume client installation user, for example, user **root**.
4.  Modify the  **flume-env.sh**  Flume client configuration file.

    Run the following command to edit the  **flume-env.sh**  file:

    **vi  _Flume client installation directory_/fusioninsight-flume-1.6.0/conf/flume-env.sh**

    Add the following information after  **-XX:+UseCMSCompactAtFullCollection**.

    ```
    -Djava.security.krb5.conf=Flume client installation directory/fusioninsight-flume-1.6.0/conf/krb5.conf 
    ```

    Change  _Flume client installation directory_  to the actual one. Then save and exit the configuration file.

5.  Add content that matches  **host** in the **/etc/hosts** file of the HDFS cluster to the **/etc/hosts**  file of the Flume client node.
6.  Restart the Flume client.

    Suppose the Flume client installation directory is  **/opt/FlumeClient**. Run the following command to restart the Flume client:

    **cd /opt/FlumeClient/fusioninsight-flume-1.6.0/bin**

    **./flume-manage.sh restart**

7.  Encrypt SK using the encryption tool of the Flume client. For details, see  [Using the Encryption Tool of the Flume Client](using-the-encryption-tool-of-the-flume-client.md).
8.  Run the following command to modify the  **properties.properties**  configuration file of the Flume client:

    **vi** _Flume client installation directory_**/fusioninsight-flume-1.6.0/conf/properties.properties**

    Add the following information to the  **properties.properties**  file:

    ```
    client.sources = obs
    client.channels = flume
    client.sinks = hdfs
    
    client.sources.obs.type=org.apache.flume.source.s3.OBSSource
    client.sources.obs.bucketName = obs-nemon-sink
    client.sources.obs.prefix = obs-source/
    client.sources.obs.accessKey = AK 
    client.sources.obs.secretKey = SK 
    client.sources.obs.backingDir = /tmp/obs/
    client.sources.obs.endPoint = 
    client.sources.obs.basenameHeader = true
    client.sources.obs.basenameHeaderKey = basename
    client.sources.obs.channels = flume 
    
    client.channels.flume.type = memory
    client.channels.flume.capacity = 10000
    client.channels.flume.transactionCapacity = 1000
    client.channels.flume.channelfullcount = 10
    client.channels.flume.keep-alive = 3
    client.channels.flume.byteCapacity = 
    client.channels.flume.byteCapacityBufferPercentage = 20
    
    
    client.sinks.hdfs.type = hdfs
    client.sinks.hdfs.hdfs.path = hdfs://hacluster/tmp
    client.sinks.hdfs.montime = 
    client.sinks.hdfs.hdfs.filePrefix = over_%{basename}
    client.sinks.hdfs.hdfs.fileSuffix = 
    client.sinks.hdfs.hdfs.inUsePrefix = 
    client.sinks.hdfs.hdfs.inUseSuffix = .tmp
    client.sinks.hdfs.hdfs.idleTimeout = 0
    client.sinks.hdfs.hdfs.batchSize = 1000
    client.sinks.hdfs.hdfs.codeC =  
    client.sinks.hdfs.hdfs.fileType = DataStream
    client.sinks.hdfs.hdfs.maxOpenFiles = 5000
    client.sinks.hdfs.hdfs.writeFormat = Writable
    client.sinks.hdfs.hdfs.callTimeout = 10000
    client.sinks.hdfs.hdfs.threadsPoolSize = 10
    client.sinks.hdfs.hdfs.rollTimerPoolSize = 1
    client.sinks.hdfs.hdfs.kerberosPrincipal = admin
    client.sinks.hdfs.hdfs.kerberosKeytab = /opt/FlumeClient/fusioninsight-flume-1.6.0/conf/user.keytab
    client.sinks.hdfs.hdfs.round = false
    client.sinks.hdfs.hdfs.roundUnit = second
    client.sinks.hdfs.hdfs.useLocalTimeStamp = false
    client.sinks.hdfs.hdfs.failcount = 10
    client.sinks.hdfs.hdfs.fileCloseByEndEvent = true
    client.sinks.hdfs.hdfs.rollInterval = 30
    client.sinks.hdfs.hdfs.rollSize = 1024
    client.sinks.hdfs.hdfs.rollCount = 10
    client.sinks.hdfs.hdfs.batchCallTimeout = 0
    client.sinks.hdfs.serializer.appendNewline = true
    client.sinks.hdfs.channel = flume 
    ```

    Modify the following parameters as required. Then save and exit the file.

    -   **bucketName**
    -   **prefix**
    -   **backingDir**
    -   **endPoint**
    -   **accessKey**

        \(Enter the actual AK value.\)

    -   **sercretKey**

        \(Enter the actual encrypted SK value.\)

    -   **kerberosPrincipal**

        \(The username must be configured in the security cluster.\)

    -   **kerberosKeytab**

        \(The absolute path of the user's authentication credential file must be configured in the security cluster.\)

9.  The Flume client automatically loads the information in the  **properties.properties**  file.

    After new log files are generated in the  **prefix** directory under **bucketName**, the logs will be sent to OBS.


