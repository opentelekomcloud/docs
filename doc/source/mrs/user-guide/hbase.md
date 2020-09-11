# HBase<a name="EN-US_TOPIC_0125375664"></a>

HBase is a column-oriented distributed cloud storage system. It features enhanced reliability, excellent performance, and elastic scalability.

It is applicable in distributed computing and the storage of massive data. With HBase, users can filter and analyze data with ease and get responses in milliseconds, thereby rapidly mining data.

HBase applies to the following scenarios:

-   Massive data storage

    Users can use HBase to build a storage system capable of storing TB or PB of data. It also provides dynamic scaling capabilities so that users can adjust cluster resources to meet specific performance or capacity requirements.

-   Real-time query

    The columnar and key-value storage models apply to the ad-hoc querying of enterprise user details. The low-latency point query, based on the master key, reduces the response latency to seconds or milliseconds, facilitating real-time data analysis.


HBase has the following highlights:

-   Provides automatic Region recovery from an exception, ensuring reliability of data access.
-   Enables data imported to the active cluster using BulkLoad to be automatically synchronized to the disaster recovery backup cluster. HBase also enhances the Replication feature, for example, supporting table structure synchronization, data synchronization between tables with system permissions, and the cluster readonly function.
-   Improves performance of the BulkLoad feature, accelerating data import.

For details about HBase architecture and principles, see  [http://hbase.apache.org/book.html](http://hbase.apache.org/book.html).

