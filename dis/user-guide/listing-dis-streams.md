# Listing DIS Streams<a name="dis_01_0011"></a>

The  **Stream Management**  page displays all DIS streams created. After clicking a stream, you can view the following information about this stream:

**Figure  1**  Stream Management<a name="fig1657418112911"></a>  
![](figures/stream-management.jpg "stream-management")

-   **Name/ID**: Unique name of the DIS stream to be created. A stream name is 1 to 64 characters long. Only letters, digits, hyphens \(-\), and underscores \(\_\) are allowed.
-   **Status**: Stream status.
-   **Stream Type**:  **Common**  and  **Advanced**.
    -   **Common**: Each partition supports a maximum read speed of 2 MB/s and a maximum write speed of 1 MB/s or 1,000 records/s.
    -   **Advanced**: Each partition supports a maximum read speed of 10 MB/s and a maximum write speed of 5 MB/s or 2,000 records/s.

-   **Partitions**: The number of partitions into which data records in the newly created DIS stream will be distributed. Multiple partitions of a stream can concurrently transmit data to improve efficiency.
-   **Data Retention \(hours\)**: The maximum number of hours for DIS to preserve data. Data will be deleted when the retention period expires. Value range: an integer ranging from 24 to 72. Unit: hour
-   **Created**: Time at which the DIS stream is created. The creation time is in the yyyy/MM/dd HH:mm:ss GMT format. For example, 2017/05/09 08:00:00 GMT+08:00.
-   **Operation**: Supported operations include  **Delete**, and  **View Dump Task**.

