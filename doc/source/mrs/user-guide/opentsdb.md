# OpenTSDB<a name="EN-US_TOPIC_0221415039"></a>

OpenTSDB is a distributed, scalable time series database based on HBase. OpenTSDB is designed to collect monitoring information of a large-scale cluster and implement second-level data query, eliminating the limitations of querying and storing massive amounts of monitoring data in common databases.

Application scenarios of OpenTSDB have the following features: 

-   The collected metrics have a unique value at a time point and do not have a complex structure or relationship.
-   Monitoring metrics change with time.
-   Like HBase, OpenTSDB features high throughput and good scalability.

OpenTSDB provides an HTTP based application programming interface to enable integration with external systems. Almost all OpenTSDB features are accessible via the API such as querying time series data, managing metadata, and storing data points. For details, visit  [http://opentsdb.net/docs/build/html/api\_http/index.html](http://opentsdb.net/docs/build/html/api_http/index.html).

