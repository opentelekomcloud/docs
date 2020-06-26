# Relationships with Other Services<a name="EN-US_TOPIC_0125375790"></a>

This section describes the relationships between MRS and other services.

-   Virtual Private Cloud \(VPC\)

    MRS clusters are created in the subnets of a VPC. VPCs provide secure, isolated, logical network environments for MRS clusters.

-   Object Storage Service \(OBS\)

    OBS stores the following user data:

    -   MRS job input data, such as user programs and data files
    -   MRS job output data, such as result files and log files of jobs

    In MRS clusters, the HDFS, Hive, MapReduce, Yarn, Spark, Flume, and Loader modules can import or export data from OBS.

-   Elastic Cloud Server \(ECS\)

    Each node in an MRS cluster is an ECS.

-   Identity and Access Management \(IAM\)

    IAM provides authentication for MRS.

-   Cloud Trace Service \(CTS\)

    CTS provides operation records, including requests for operating MRS resources and the request results, for users to query, audit, and trace back the recorded problems.


