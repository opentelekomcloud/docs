# What Is DIS?<a name="dis_01_0001"></a>

Data Ingestion Service \(DIS\) addresses the challenge of transmitting data from outside the cloud to inside the cloud. DIS builds data intake streams for custom applications capable of processing or analyzing streaming data. DIS continuously captures, transmits, and stores terabytes of data from hundreds of thousands of sources every hour, such as logs, social media feeds, website clickstreams, and location-tracking events.

## Basic Concepts<a name="section63248778"></a>

-   Stream: A DIS stream is an ordered sequence of data records. Streams are distinguished from each other by the stream names assigned during DIS stream creation. When reading or writing streaming data, you need to specify the name of DIS stream from or to which data will be read or written.
-   Partition: Data records in DIS streams are distributed into partitions. A partition is a base throughput unit of a DIS stream. When creating a DIS stream, you are expected to specify the number of partitions needed within your stream.
-   Record: A record is a unit of data stored in a DIS stream. A record consists of a serial number, partition key, and data block. Data blocks are important data that your data producer adds to the data stream. The maximum size of a data block \(data payload before base64 encoding\) is 1 MB.
-   Sequence number: Each data record has a sequence number that is unique within its partition. The sequence number is assigned by DIS when a data producer calls PutRecords to add data to a DIS stream. 

    Sequence numbers for the same partition key generally increase over time; the longer the time period between write requests \(PutRecords requests\), the larger the sequence numbers become.

-   DIS application: DIS applications write, read, and process data in DIS streams. You can develop DIS applications using the client library software development kit \(SDK\).
-   SDK: SDK is a Java-based client library. With SDK, you can build DIS applications easily to write, read, and process data in DIS streams.
-   Project: Projects are used to group and isolate OpenStack resources \(computing resources, storage resources, and network resources\). A project can be a department or a project team. Multiple projects can be created for one tenant account. A region has multiple projects, but one project is related to one region. DIS streams in different projects cannot communicate with each other.
-   Checkpoint: When an application consumes data, the latest serial number of the consumed data is recorded as a checkpoint. When the data is reconsumed, the consumption can be continued based on this checkpoint.
-   Application: When multiple applications consume data in the same stream, an APP is used as an identifier to distinguish consumption checkpoints of different applications.

