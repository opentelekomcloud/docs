# Why Is the Performance of DWS Worse Than That of a Single-Server Database in Extreme Scenarios?<a name="dws_03_0036"></a>

Due to the MPP architecture limitation in DWS, a few PG system methods and functions cannot be pushed to the DataNodes for execution. As a result, performance bottlenecks occur on the Coordinator Nodes \(CNs\). 

**Explanation:**

-   An operation can be executed concurrently only when it is logically a concurrent operation. Take the SUM operation as an example. When this operation is performed on all DataNodes concurrently, the final summarization must be performed in a centralized manner on one CN. In this case, most of the summarization work has been completed on DataNodes, the work on the CN is relatively lightweight.
-   In some scenarios, the operation must be executed in a centralized manner \(on one node\). For example, assigning a globally unique name to a transaction ID. This task is implemented through the GTM in the system. Therefore, the GTM is also a globally unique component \(active/standby\). All globally unique tasks are implemented through the GTM in DWS, but software code is optimized to reduce this kind of tasks. Therefore, the GTM does not have many bottlenecks. In some scenarios, GTM-Free and GTM-Lite can be implemented.
-   To ensure excellent performance, services need to be slightly modified for adaptation during migration from the application development mode of the traditional single-node database to that of the parallel database, especially the development mode of the traditional nesting Oracle storage.

**Solutions:**

-   If such a problem occurs, see section  **Query Performance Optimization**  in the  _Data Warehouse Service Database Developer Guide_.
-   Alternatively, contact technical support engineers to modify and optimize service adaptation.

