# Cluster Management Function<a name="EN-US_TOPIC_0125375288"></a>

This section describes the Web interface functions of MRS clusters.

MRS provides a Web interface, the functions of which are described as follows:

-   Creating a cluster:

    Users can create a cluster on MRS. The application scenarios of a cluster are as follows:

    -   Data storage and computing are performed separately. Data is stored in the Object Storage Service \(OBS\), which features a low-cost and unlimited storage capacity and clusters can be terminated at any time. The computing performance is determined by the OBS access performance and is lower than that of Hadoop Distributed File System \(HDFS\). OBS is recommended when data computing is infrequent.
    -   Data storage and computing are performed together. Data is stored in HDFS, which features high cost, high computing performance, and limited storage capacity. Before terminating clusters, you must export and store the data. HDFS is recommended when data computing is frequent.

-   Add Task Node:

    The Task node processes data rather than storing cluster data. When the number of clusters does not change much but the clusters' service processing capabilities need to be remarkably and temporarily improved, add Task nodes to address the following situations:

    -   The volume of temporary services is increased, for example, report processing at the end of the year.
    -   Long-term tasks must be completed in a short time, for example, some urgent analysis tasks.

-   Expanding clusters:

    To expand clusters and handle peak service loads, add core nodes or Task nodes.

-   Shrinking clusters:

    Reduce the number of Core nodes or Task nodes to shrink the cluster so that MRS delivers better storage and computing capabilities at lower O&M costs based on service requirements.

-   Auto Scaling:

    Automatically adjust computing resources based on service requirements and the preset policies, so that the number of Task nodes can be automatically scaled out and scaled-in with service load changes, ensuring stable service running.

-   Managing clusters:

    After completing data processing and analysis, you can manage and terminate clusters.

    -   Querying alarms:

        If either the system or a cluster is faulty, Elastic BigData will collect fault information and report it to the network management system. Maintenance personnel will then be able to locate the faults.

    -   Querying logs:

        To help locate faults in the case of faulty clusters, operation information is recorded.

    -   Managing files:

        MRS supports the ability to import data from the OBS system to HDFS and also export data that has already been processed and analyzed. You can store data in HDFS.


-   Adding a job:

    A job is an executable program provided by MRS to process and analyze user data. Currently, MRS supports MapReduce jobs, Spark jobs, and Hive jobs, and allows users to submit Spark SQL statements online to query and analyze data.

-   Adding tags:

    Tags are cluster identifiers. Adding tags to clusters can help you identify and manage your cluster resources.

    You can add a maximum of 10 tags to a cluster when creating the cluster or add them on the details page of the created cluster.

-   Adding bootstrap actions:

    Bootstrap actions indicate that you can run your scripts on a specified cluster node before or after starting big data components. You can run bootstrap actions to install third-party software, modify the cluster running environment, and perform other customizations. If you choose to run bootstrap actions when expanding a cluster, the bootstrap actions will be run on the newly added nodes in the same way.

-   Managing jobs:

    Jobs can be managed, stopped, or deleted. You can also view details of completed jobs along with detailed configurations. Spark SQL jobs, however, cannot be stopped.

-   Providing management interfaces:

    MRS Manager functions as a unified management platform for MRS clusters.

    -   Cluster monitoring enables you to quickly see the health status of hosts and services.
    -   Graphical indicator monitoring and customization enable you to quickly obtain key information about the system.
    -   Service property configurations  can  meet service performance requirements.
    -   Cluster, service, and role instance operations enable you to start or stop services and clusters in one-click mode.


