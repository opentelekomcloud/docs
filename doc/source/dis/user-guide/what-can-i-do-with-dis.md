# What Can I Do with DIS?<a name="dis_01_0002"></a>

You can use DIS for rapid data intake from producers and continuous data processing. The following are typical scenarios for using DIS:

-   Accelerated log and data feed intake

    You do not need to batch data on servers before you submit it for intake. Instead, you can have producers push data into streams immediately after data is produced.

    For example, system and application logs are pushed as they are streaming in and they will be available for processing in seconds. This prevents the data from being lost if the data producer fails.

-   Real-time metrics and reporting

    You can retrieve data from DIS streams for simple data analysis and reporting in real time. For example, your DIS applications can work on metrics and reporting for system and application logs as streaming data is being pushed to DIS streams using application programming interfaces \(APIs\), rather than wait to receive batches of data.

-   Real-time data analysis: DIS can be used to analyze real-time data. For example, you can transform data into valuable information and business intelligence by simply putting data into a DIS stream. This can be done in minutes instead of hours or days.
-   Complex stream processing

    You can create Directed Acyclic Graphs \(DAGs\) of DIS applications and streams. This typically involves putting data from one or multiple DIS applications into another stream for downstream processing by a different DIS application.


