# What Is a Data Warehouse?<a name="dws_03_0002"></a>

A data warehouse is a type of database used to store and analyze structured data. Data warehouses excel at aggregating and associating data from diverse sources and mines business value from the data. They play a critical role in business operation decision-making and intelligence analysis. 

With the rapid development of database technology and distributed technology, data warehouses evolve towards to distributed databases. The mainstream distributed data warehouse architecture is the massively parallel processing \(MPP\) architecture, which has the following characteristics:

-   An MPP architecture-based data warehouse consists of multiple equal compute nodes. 
-   Data in an MPP architecture-based data warehouse is almost evenly distributed onto each compute node based on specific rules. 
-   Each compute node has its own computing resources \(CPU and memory resources\) and allocated data. 
-   No computing resources or data is shared among the nodes. For this reason, this architecture is also known as Share Nothing architecture. 
-   An MPP architecture-based data warehouse provides a unified computing entry for customers' applications. The upper-layer applications do not detect the cluster node scale and data slices in the data warehouse. 
-   The main characteristic of the MPP architecture is that query tasks can be concurrently executed on all compute nodes, which accelerates the return of computing results and remarkably reduces the required time. 
-   The MPP architecture can change system capacity by adding or reducing compute nodes to cope with ever-changing enterprise computing requirements. 

MPP architecture-based data warehouses feature excellent performance and compatibility \(with underlying hardware and upper-layer applications\), flexible scalability, and controllable costs, which explains why its popularity among enterprise customers in recent years.

In addition, you can migrate PostgreSQL data to a data warehouse cluster. A data warehouse cluster is a database for OLAP scenarios and the PostgreSQL is a stand-alone database for OLTP scenarios. Therefore, moving the DWS database to a PostgreSQL is not supported.

