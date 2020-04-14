# Step 3: Sending Data to DIS<a name="dis_01_0603"></a>

## Function<a name="section1815156"></a>

Local data is continuously uploaded to DIS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Data can be stored in DIS and OBS. To configure a storage location, see "Dump Management" in  [Creating a Dump Task](creating-a-dump-task.md).  
>-   The maximum number of days for DIS to preserve data cannot exceed  **Data Retention \(days\)**.  

## Sample Code<a name="section16336406"></a>

The example code file is the  **ProducerDemo.java**  file in the  **\\dis-sdk-demo\\src\\main\\java\\com\\bigdata\\dis\\sdk\\demo**  directory decompressed from the  **dis-sdk-1.2.3.zip**  package. The compression package is downloaded in  [Step 2: Preparing a DIS Application Development Environment](step-2-preparing-a-dis-application-development-environment.md).

## Running the Producer Program<a name="section12809933"></a>

Right-click the producer application and choose  **Run As**  \>  **1 Java Application**  from the shortcut menu.

**Figure  1**  Running a producer application<a name="fig15069943162017"></a>  
![](figures/running-a-producer-application.png "running-a-producer-application")

While data is being sent to DIS, the DIS console displays DIS stream information. If information similar to the following is displayed, the data has been successfully sent to DIS:

```
14:40:20.090 [main] INFOcom.bigdata.dis.sdk.DISConfig - get from classLoader
14:40:20.093 [main] INFODEMOT - ========== BEGIN PUT ============
14:40:21.186 [main] INFOcom.bigdata.dis.sdk.util.config.ConfigurationUtils - get from classLoader
14:40:21.187 [main] INFOcom.bigdata.dis.sdk.util.config.ConfigurationUtils - propertyMapFromFile size : 2
14:40:22.092 [main] INFOcom.bigdata.dis.sdk.demo.ProducerDemo - Put 3 records[3 successful / 0 failed].
14:40:22.092 [main] INFOcom.bigdata.dis.sdk.demo.ProducerDemo - [hello world.] put success, partitionId [shardId-0000000000], partitionKey [964885], sequenceNumber [0]
14:40:22.092 [main] INFOcom.bigdata.dis.sdk.demo.ProducerDemo - [hello world.] put success, partitionId [shardId-0000000000], partitionKey [910960], sequenceNumber [1]
14:40:22.092 [main] INFOcom.bigdata.dis.sdk.demo.ProducerDemo - [hello world.] put success, partitionId [shardId-0000000000], partitionKey [528377], sequenceNumber [2]
14:40:22.092 [main] INFOcom.bigdata.dis.sdk.demo.ProducerDemo - ========== PUT OVER ============
```

