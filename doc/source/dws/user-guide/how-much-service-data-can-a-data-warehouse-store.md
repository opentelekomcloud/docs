# How Much Service Data Can a Data Warehouse Store?<a name="dws_03_0028"></a>

Each node in a data warehouse cluster supports the storage capacity of 160 GB, 256 GB, 1.6 TB, 1.8 TB, or 13 TB by default. A cluster can house 3 to 32 nodes and the total storage capacity of the cluster expands proportionally as the cluster scale grows.

To enhance the reliability, each node has a replica. The replicas occupy half of the storage space.

The DWS system backs up data and generates indexes, temporary cache files, and run logs, which occupy storage space. Therefore, the actual storage space of each node is about half of the total storage capacity.

