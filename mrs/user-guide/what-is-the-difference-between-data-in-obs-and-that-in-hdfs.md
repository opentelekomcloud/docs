# What Is the Difference Between Data in OBS and That in HDFS?<a name="EN-US_TOPIC_0125375309"></a>

The data source to be processed by MRS is from OBS or HDFS. OBS provides you with massive, highly reliable, and secure data storage capabilities at a low cost. MRS can process the data in OBS. You can view, manage, and use data by using OBS Console or an OBS client. In addition, you can use the REST APIs to manage or access data. You can use the REST APIs alone or integrate it with service programs.

-   OBS data storage: Data storage and computing are performed separately. OBS data storage features low cost and unlimited storage capacity. The clusters can be terminated at any time in OBS. The computing performance is determined by OBS access performance and is lower than that of HDFS. OBS is recommended when data computing is not frequent.
-   HDFS data storage: Data storage and computing are performed together. HDFS data storage features high cost, high computing performance, and limited storage capacity. Before terminating clusters, you must export and store the data. HDFS is recommended when data computing is frequent.

