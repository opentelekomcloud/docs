# MRS User Guide

-   [Overview]
    -   [Introduction](introduction.md)
    -   [Application Scenarios](application-scenarios.md)
    -   [Functions]
        -   [Cluster Management Function](cluster-management-function.md)
        -   [Hadoop](hadoop.md)
        -   [Spark](spark.md)
        -   [Spark SQL](spark-sql.md)
        -   [HBase](hbase.md)
        -   [Hive](hive.md)
        -   [Hue](hue.md)
        -   [Kerberos Authentication](kerberos-authentication.md)
        -   [Kafka](kafka.md)
        -   [Storm](storm.md)
        -   [CarbonData](carbondata.md)
        -   [Flume](flume.md)
        -   [Loader](loader.md)
        -   [Presto](presto.md)
        -   [Tez: High-speed Computing Engine Supporting DAG Models](tez-high-speed-computing-engine-supporting-dag-models.md)
        -   [KafkaManager](kafkamanager.md)
        -   [OpenTSDB](opentsdb.md)
        -   [Flink](flink.md)
        -   [Alluxio](alluxio.md)
        -   [Ranger](ranger.md)

    -   [Relationships with Other Services](relationships-with-other-services.md)
    -   [Required Permission for Using MRS](required-permission-for-using-mrs.md)
    -   [Limitations](limitations.md)
    -   [Basic Concepts](basic-concepts.md)

-   [MRS Quick Start]
    -   [Introduction to the Operation Process](introduction-to-the-operation-process.md)
    -   [Quick Start]
        -   [Creating a Cluster](creating-a-cluster_quick-start.md)
        -   [Managing Files](managing-files.md)
        -   [Creating a Job](creating-a-job.md)


-   [Security]
    -   [Security Configuration Suggestions for Clusters with Kerberos Authentication Disabled](security-configuration-suggestions-for-clusters-with-kerberos-authentication-disabled.md)

-   [Cluster Operation Guide]
    -   [Overview](overview_cluster.md)
    -   [Cluster List](cluster-list.md)
    -   [Creating a Cluster](creating-a-cluster.md)
    -   [Creating the Smallest Cluster](creating-the-smallest-cluster.md)
    -   [Managing Active Clusters]
        -   [Viewing Basic Information About an Active Cluster](viewing-basic-information-about-an-active-cluster.md)
        -   [Viewing Patch Information About an Active Cluster](viewing-patch-information-about-an-active-cluster.md)
        -   [Synchronizing IAM Users to MRS](synchronizing-iam-users-to-mrs.md)
        -   [Accessing the Cluster Management Page](accessing-the-cluster-management-page.md)
        -   [Expanding a Cluster](expanding-a-cluster.md)
        -   [Shrinking a Cluster](shrinking-a-cluster.md)
        -   [Using Auto Scaling in a Cluster](using-auto-scaling-in-a-cluster.md)
        -   [Configuring Auto Scaling Rules When Creating a Cluster](configuring-auto-scaling-rules-when-creating-a-cluster.md)
        -   [Scaling Up Master Node Specifications](scaling-up-master-node-specifications.md)
        -   [Terminating a Cluster](terminating-a-cluster.md)
        -   [Deleting a Failed Task](deleting-a-failed-task.md)
        -   [Managing Jobs in an Active Cluster](managing-jobs-in-an-active-cluster.md)
        -   [Managing Data Files](managing-data-files.md)
        -   [Viewing the Alarm List](viewing-the-alarm-list.md)
        -   [Configuring Message Notification](configuring-message-notification.md)
        -   [Authorizing O&M](authorizing-o-m.md)
        -   [Sharing Logs](sharing-logs.md)

    -   [Managing Historical Clusters]
        -   [Viewing Basic Information About a Historical Cluster](viewing-basic-information-about-a-historical-cluster.md)
        -   [Viewing Job Configurations in a Historical Cluster](viewing-job-configurations-in-a-historical-cluster.md)

    -   [Managing Jobs]
        -   [Introduction to Jobs](introduction-to-jobs.md)
        -   [Running a MapReduce Job](running-a-mapreduce-job.md)
        -   [Running a Spark Job](running-a-spark-job.md)
        -   [Running a HiveSql Job](running-a-hivesql-job.md)
        -   [Running a SparkSql Job](running-a-sparksql-job.md)
        -   [Running a Flink Job](running-a-flink-job.md)
        -   [Running a Kafka Job](running-a-kafka-job.md)
        -   [Viewing Job Configurations and Logs](viewing-job-configurations-and-logs.md)
        -   [Stopping Jobs](stopping-jobs.md)
        -   [Copying Jobs](copying-jobs.md)
        -   [Deleting Jobs](deleting-jobs.md)

    -   [Querying Operation Logs](querying-operation-logs.md)
    -   [Managing Cluster Tags](managing-cluster-tags.md)
    -   [Bootstrap Actions]
        -   [Introduction to Bootstrap Actions](introduction-to-bootstrap-actions.md)
        -   [Preparing the Bootstrap Action Script](preparing-the-bootstrap-action-script.md)
        -   [Adding a Bootstrap Action](adding-a-bootstrap-action.md)
        -   [View Execution Records](view-execution-records.md)
        -   [Sample Scripts](sample-scripts.md)


-   [Remote Operation Guide]
    -   [Overview](overview_logging.md)
    -   [Logging In to a Master Node]
        -   [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md)
        -   [Logging In to a Linux ECS Using a Key Pair \(SSH\)](logging-in-to-a-linux-ecs-using-a-key-pair-(ssh).md)
        -   [Logging In to a Linux ECS Using a Password \(SSH\)](logging-in-to-a-linux-ecs-using-a-password-(ssh).md)

    -   [Viewing Active and Standby Nodes](viewing-active-and-standby-nodes.md)
    -   [Client Management]
        -   [Updating the Client](updating-the-client.md)
        -   [Using the Client on a Cluster Node](using-the-client-on-a-cluster-node.md)
        -   [Using the Client on Another Node of a VPC](using-the-client-on-another-node-of-a-vpc.md)


-   [MRS Manager Operation Guide]
    -   [MRS Manager Introduction](mrs-manager-introduction.md)
    -   [Accessing MRS Manager](accessing-mrs-manager.md)
    -   [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md)
    -   [Viewing Running Tasks in a Cluster](viewing-running-tasks-in-a-cluster.md)
    -   [Monitoring Management]
        -   [Viewing the System Overview](viewing-the-system-overview.md)
        -   [Managing Service and Host Monitoring](managing-service-and-host-monitoring.md)
        -   [Managing Resource Distribution](managing-resource-distribution.md)
        -   [Configuring Monitoring Metric Dumping](configuring-monitoring-metric-dumping.md)

    -   [Alarm Management]
        -   [Viewing and Manually Clearing an Alarm](viewing-and-manually-clearing-an-alarm.md)
        -   [Configuring an Alarm Threshold](configuring-an-alarm-threshold.md)
        -   [Configuring Syslog Northbound Interface](configuring-syslog-northbound-interface.md)
        -   [Configuring SNMP Northbound Interface](configuring-snmp-northbound-interface.md)

    -   [Alarm Reference]
        -   [ALM-12001 Audit Log Dump Failure](alm-12001-audit-log-dump-failure.md)
        -   [ALM-12002 HA Resource Is Abnormal](alm-12002-ha-resource-is-abnormal.md)
        -   [ALM-12004 OLdap Resource Is Abnormal](alm-12004-oldap-resource-is-abnormal.md)
        -   [ALM-12005 OKerberos Resource Is Abnormal](alm-12005-okerberos-resource-is-abnormal.md)
        -   [ALM-12006 Node Fault](alm-12006-node-fault.md)
        -   [ALM-12007 Process Fault](alm-12007-process-fault.md)
        -   [ALM-12010 Manager Heartbeat Interruption Between the Active and Standby Nodes](alm-12010-manager-heartbeat-interruption-between-the-active-and-standby-nodes.md)
        -   [ALM-12011 Manager Data Synchronization Exception Between the Active and Standby Nodes](alm-12011-manager-data-synchronization-exception-between-the-active-and-standby-nodes.md)
        -   [ALM-12012 NTP Service Is Abnormal](alm-12012-ntp-service-is-abnormal.md)
        -   [ALM-12016 CPU Usage Exceeds the Threshold](alm-12016-cpu-usage-exceeds-the-threshold.md)
        -   [ALM-12017 Insufficient Disk Capacity](alm-12017-insufficient-disk-capacity.md)
        -   [ALM-12018 Memory Usage Exceeds the Threshold](alm-12018-memory-usage-exceeds-the-threshold.md)
        -   [ALM-12027 Host PID Usage Exceeds the Threshold](alm-12027-host-pid-usage-exceeds-the-threshold.md)
        -   [ALM-12028 Number of Processes in the D State on the Host Exceeds the Threshold](alm-12028-number-of-processes-in-the-d-state-on-the-host-exceeds-the-threshold.md)
        -   [ALM-12031 User omm or Password Is About to Expire](alm-12031-user-omm-or-password-is-about-to-expire.md)
        -   [ALM-12032 User ommdba or Password Is About to Expire](alm-12032-user-ommdba-or-password-is-about-to-expire.md)
        -   [ALM-12033 Slow Disk Fault](alm-12033-slow-disk-fault.md)
        -   [ALM-12034 Periodic Backup Failure](alm-12034-periodic-backup-failure.md)
        -   [ALM-12035 Unknown Data Status After Recovery Task Failure](alm-12035-unknown-data-status-after-recovery-task-failure.md)
        -   [ALM-12037 NTP Server Is Abnormal](alm-12037-ntp-server-is-abnormal.md)
        -   [ALM-12038 Monitoring Indicator Dump Failure](alm-12038-monitoring-indicator-dump-failure.md)
        -   [ALM-12039 GaussDB Data Is Not Synchronized](alm-12039-gaussdb-data-is-not-synchronized.md)
        -   [ALM-12040 Insufficient System Entropy](alm-12040-insufficient-system-entropy.md)
        -   [ALM-13000 ZooKeeper Service Unavailable](alm-13000-zookeeper-service-unavailable.md)
        -   [ALM-13001 Available ZooKeeper Connections Are Insufficient](alm-13001-available-zookeeper-connections-are-insufficient.md)
        -   [ALM-13002 ZooKeeper Heap Memory or Direct Memory Usage Exceeds the Threshold](alm-13002-zookeeper-heap-memory-or-direct-memory-usage-exceeds-the-threshold.md)
        -   [ALM-14000 HDFS Service Unavailable](alm-14000-hdfs-service-unavailable.md)
        -   [ALM-14001 HDFS Disk Usage Exceeds the Threshold](alm-14001-hdfs-disk-usage-exceeds-the-threshold.md)
        -   [ALM-14002 DataNode Disk Usage Exceeds the Threshold](alm-14002-datanode-disk-usage-exceeds-the-threshold.md)
        -   [ALM-14003 Number of Lost HDFS Blocks Exceeds the Threshold](alm-14003-number-of-lost-hdfs-blocks-exceeds-the-threshold.md)
        -   [ALM-14004 Number of Damaged HDFS Blocks Exceeds the Threshold](alm-14004-number-of-damaged-hdfs-blocks-exceeds-the-threshold.md)
        -   [ALM-14006 Number of HDFS Files Exceeds the Threshold](alm-14006-number-of-hdfs-files-exceeds-the-threshold.md)
        -   [ALM-14007 HDFS NameNode Memory Usage Exceeds the Threshold](alm-14007-hdfs-namenode-memory-usage-exceeds-the-threshold.md)
        -   [ALM-14008 HDFS DataNode Memory Usage Exceeds the Threshold](alm-14008-hdfs-datanode-memory-usage-exceeds-the-threshold.md)
        -   [ALM-14009 Number of Dead DataNodes Exceeds the Threshold](alm-14009-number-of-dead-datanodes-exceeds-the-threshold.md)
        -   [ALM-14010 NameService Service Is Abnormal](alm-14010-nameservice-service-is-abnormal.md)
        -   [ALM-14011 HDFS DataNode Data Directory Is Not Configured Properly](alm-14011-hdfs-datanode-data-directory-is-not-configured-properly.md)
        -   [ALM-14012 HDFS JournalNode Data Is Not Synchronized](alm-14012-hdfs-journalnode-data-is-not-synchronized.md)
        -   [ALM-16000 Percentage of Sessions Connected to the HiveServer to Maximum Number Allowed Exceeds the Threshold](alm-16000-percentage-of-sessions-connected-to-the-hiveserver-to-maximum-number-allowed-exceeds-the-t.md)
        -   [ALM-16001 Hive Warehouse Space Usage Exceeds the Threshold](alm-16001-hive-warehouse-space-usage-exceeds-the-threshold.md)
        -   [ALM-16002 Successful Hive SQL Operations Are Lower than the Threshold](alm-16002-successful-hive-sql-operations-are-lower-than-the-threshold.md)
        -   [ALM-16004 Hive Service Unavailable](alm-16004-hive-service-unavailable.md)
        -   [ALM-18000 Yarn Service Unavailable](alm-18000-yarn-service-unavailable.md)
        -   [ALM-18002 NodeManager Heartbeat Lost](alm-18002-nodemanager-heartbeat-lost.md)
        -   [ALM-18003 NodeManager Unhealthy](alm-18003-nodemanager-unhealthy.md)
        -   [ALM-18006 MapReduce Job Execution Timeout](alm-18006-mapreduce-job-execution-timeout.md)
        -   [ALM-19000 HBase Service Unavailable](alm-19000-hbase-service-unavailable.md)
        -   [ALM-19006 HBase Replication Synchronization Failed](alm-19006-hbase-replication-synchronization-failed.md)
        -   [ALM-25000 LdapServer Service Unavailable](alm-25000-ldapserver-service-unavailable.md)
        -   [ALM-25004 Abnormal LdapServer Data Synchronization](alm-25004-abnormal-ldapserver-data-synchronization.md)
        -   [ALM-25500 KrbServer Service Unavailable](alm-25500-krbserver-service-unavailable.md)
        -   [ALM-27001 DBService Unavailable](alm-27001-dbservice-unavailable.md)
        -   [ALM-27003 DBService Heartbeat Interruption Between the Active and Standby Nodes](alm-27003-dbservice-heartbeat-interruption-between-the-active-and-standby-nodes.md)
        -   [ALM-27004 Data Inconsistency Between Active and Standby DBServices](alm-27004-data-inconsistency-between-active-and-standby-dbservices.md)
        -   [ALM-28001 Spark Service Unavailable](alm-28001-spark-service-unavailable.md)
        -   [ALM-26051 Storm Service Unavailable](alm-26051-storm-service-unavailable.md)
        -   [ALM-26052 Number of Available Supervisors in Storm Is Lower Than the Threshold](alm-26052-number-of-available-supervisors-in-storm-is-lower-than-the-threshold.md)
        -   [ALM-26053 Slot Usage of Storm Exceeds the Threshold](alm-26053-slot-usage-of-storm-exceeds-the-threshold.md)
        -   [ALM-26054 Heap Memory Usage of Storm Nimbus Exceeds the Threshold](alm-26054-heap-memory-usage-of-storm-nimbus-exceeds-the-threshold.md)
        -   [ALM-38000 Kafka Service Unavailable](alm-38000-kafka-service-unavailable.md)
        -   [ALM-38001 Insufficient Kafka Disk Space](alm-38001-insufficient-kafka-disk-space.md)
        -   [ALM-38002 Heap Memory Usage of Kafka Exceeds the Threshold](alm-38002-heap-memory-usage-of-kafka-exceeds-the-threshold.md)
        -   [ALM-24000 Flume Service Unavailable](alm-24000-flume-service-unavailable.md)
        -   [ALM-24001 Flume Agent Is Abnormal](alm-24001-flume-agent-is-abnormal.md)
        -   [ALM-24003 Flume Client Connection Failure](alm-24003-flume-client-connection-failure.md)
        -   [ALM-24004 Flume Fails to Read Data](alm-24004-flume-fails-to-read-data.md)
        -   [ALM-24005 Data Transmission by Flume Is Abnormal](alm-24005-data-transmission-by-flume-is-abnormal.md)
        -   [ALM-12041 Permission of Key Files Is Abnormal](alm-12041-permission-of-key-files-is-abnormal.md)
        -   [ALM-12042 Key File Configurations Are Abnormal](alm-12042-key-file-configurations-are-abnormal.md)
        -   [ALM-23001 Loader Service Unavailable](alm-23001-loader-service-unavailable.md)
        -   [ALM-12357 Failed to Export Audit Logs to the OBS](alm-12357-failed-to-export-audit-logs-to-the-obs.md)
        -   [ALM-12014 Partition Lost](alm-12014-partition-lost.md)
        -   [ALM-12015 Partition Filesystem Readonly](alm-12015-partition-filesystem-readonly.md)
        -   [ALM-12043 DNS Resolution Duration Exceeds the Threshold](alm-12043-dns-resolution-duration-exceeds-the-threshold.md)
        -   [ALM-12045 Network Read Packet Dropped Rate Exceeds the Threshold](alm-12045-network-read-packet-dropped-rate-exceeds-the-threshold.md)
        -   [ALM-12046 Network Write Packet Dropped Rate Exceeds the Threshold](alm-12046-network-write-packet-dropped-rate-exceeds-the-threshold.md)
        -   [ALM-12047 Network Read Packet Error Rate Exceeds the Threshold](alm-12047-network-read-packet-error-rate-exceeds-the-threshold.md)
        -   [ALM-12048 Network Write Packet Error Rate Exceeds the Threshold](alm-12048-network-write-packet-error-rate-exceeds-the-threshold.md)
        -   [ALM-12049 Network Read Throughput Rate Exceeds the Threshold](alm-12049-network-read-throughput-rate-exceeds-the-threshold.md)
        -   [ALM-12050 Network Write Throughput Rate Exceeds the Threshold](alm-12050-network-write-throughput-rate-exceeds-the-threshold.md)
        -   [ALM-12051 Disk Inode Usage Exceeds the Threshold](alm-12051-disk-inode-usage-exceeds-the-threshold.md)
        -   [ALM-12052 TCP Temporary Port Usage Exceeds the Threshold](alm-12052-tcp-temporary-port-usage-exceeds-the-threshold.md)
        -   [ALM-12053 File Handle Usage Exceeds the Threshold](alm-12053-file-handle-usage-exceeds-the-threshold.md)
        -   [ALM-12054 The Certificate File Is Invalid](alm-12054-the-certificate-file-is-invalid.md)
        -   [ALM-12055 The Certificate File Is About to Expire](alm-12055-the-certificate-file-is-about-to-expire.md)
        -   [ALM-18008 Heap Memory Usage of Yarn ResourceManager Exceeds the Threshold](alm-18008-heap-memory-usage-of-yarn-resourcemanager-exceeds-the-threshold.md)
        -   [ALM-18009 Heap Memory Usage of MapReduce JobHistoryServer Exceeds the Threshold](alm-18009-heap-memory-usage-of-mapreduce-jobhistoryserver-exceeds-the-threshold.md)
        -   [ALM-20002 Hue Service Unavailable](alm-20002-hue-service-unavailable.md)
        -   [ALM-43001 Spark Service Unavailable](alm-43001-spark-service-unavailable.md)
        -   [ALM-43006 Heap Memory Usage of the JobHistory Process Exceeds the Threshold](alm-43006-heap-memory-usage-of-the-jobhistory-process-exceeds-the-threshold.md)
        -   [ALM-43007 Non-Heap Memory Usage of the JobHistory Process Exceeds the Threshold](alm-43007-non-heap-memory-usage-of-the-jobhistory-process-exceeds-the-threshold.md)
        -   [ALM-43008 Direct Memory Usage of the JobHistory Process Exceeds the Threshold](alm-43008-direct-memory-usage-of-the-jobhistory-process-exceeds-the-threshold.md)
        -   [ALM-43009 JobHistory GC Time Exceeds the Threshold](alm-43009-jobhistory-gc-time-exceeds-the-threshold.md)
        -   [ALM-43010 Heap Memory Usage of the JDBCServer Process Exceeds the Threshold](alm-43010-heap-memory-usage-of-the-jdbcserver-process-exceeds-the-threshold.md)
        -   [ALM-43011 Non-Heap Memory Usage of the JDBCServer Process Exceeds the Threshold](alm-43011-non-heap-memory-usage-of-the-jdbcserver-process-exceeds-the-threshold.md)
        -   [ALM-43012 Direct Memory Usage of the JDBCServer Process Exceeds the Threshold](alm-43012-direct-memory-usage-of-the-jdbcserver-process-exceeds-the-threshold.md)
        -   [ALM-43013 JDBCServer GC Time Exceeds the Threshold](alm-43013-jdbcserver-gc-time-exceeds-the-threshold.md)

    -   [Object Management]
        -   [Introduction](introduction_object.md)
        -   [Querying Configurations](querying-configurations.md)
        -   [Managing Services](managing-services.md)
        -   [Configuring Service Parameters](configuring-service-parameters.md)
        -   [Configuring Customized Service Parameters](configuring-customized-service-parameters.md)
        -   [Synchronizing Service Configurations](synchronizing-service-configurations.md)
        -   [Managing Role Instances](managing-role-instances.md)
        -   [Configuring Role Instance Parameters](configuring-role-instance-parameters.md)
        -   [Synchronizing Role Instance Configuration](synchronizing-role-instance-configuration.md)
        -   [Decommissioning and Recommissioning Role Instances](decommissioning-and-recommissioning-role-instances.md)
        -   [Managing a Host](managing-a-host.md)
        -   [Isolating a Host](isolating-a-host.md)
        -   [Canceling Isolation of a Host](canceling-isolation-of-a-host.md)
        -   [Starting and Stopping a Cluster](starting-and-stopping-a-cluster.md)
        -   [Synchronizing Cluster Configurations](synchronizing-cluster-configurations.md)
        -   [Exporting Configuration Data of a Cluster](exporting-configuration-data-of-a-cluster.md)

    -   [Log Management]
        -   [Viewing and Exporting Audit Logs](viewing-and-exporting-audit-logs.md)
        -   [Exporting Services Logs](exporting-services-logs.md)
        -   [Configuring Audit Log Export Parameters](configuring-audit-log-export-parameters.md)

    -   [Health Check Management]
        -   [Performing a Health Check](performing-a-health-check.md)
        -   [Viewing and Exporting a Check Report](viewing-and-exporting-a-check-report.md)
        -   [Configuring the Number of Health Check Reports to Be Reserved](configuring-the-number-of-health-check-reports-to-be-reserved.md)
        -   [Managing Health Check Reports](managing-health-check-reports.md)

    -   [Static Service Pool Management]
        -   [Viewing the Status of a Static Service Pool](viewing-the-status-of-a-static-service-pool.md)
        -   [Configuring a Static Service Pool](configuring-a-static-service-pool.md)

    -   [Tenant Management]
        -   [Introduction](introduction_tenant.md)
        -   [Creating a Tenant](creating-a-tenant.md)
        -   [Creating a Sub-tenant](creating-a-sub-tenant.md)
        -   [Deleting a Tenant](deleting-a-tenant.md)
        -   [Managing a Tenant Directory](managing-a-tenant-directory.md)
        -   [Recovering Tenant Data](recovering-tenant-data.md)
        -   [Creating a Resource Pool](creating-a-resource-pool.md)
        -   [Modifying a Resource Pool](modifying-a-resource-pool.md)
        -   [Deleting a Resource Pool](deleting-a-resource-pool.md)
        -   [Configuring a Queue](configuring-a-queue.md)
        -   [Configuring the Queue Capacity Policy of a Resource Pool](configuring-the-queue-capacity-policy-of-a-resource-pool.md)
        -   [Clearing the Configuration of a Queue](clearing-the-configuration-of-a-queue.md)

    -   [Backup and Restoration]
        -   [Introduction](introduction_backup_restoration.md)
        -   [Backing Up Metadata](backing-up-metadata.md)
        -   [Recovering Metadata](recovering-metadata.md)
        -   [Modifying a Backup Task](modifying-a-backup-task.md)
        -   [Viewing Backup and Recovery Tasks](viewing-backup-and-recovery-tasks.md)

    -   [Security Management]
        -   [Default Users of Clusters with Kerberos Authentication Disabled](default-users-of-clusters-with-kerberos-authentication-disabled.md)
        -   [Default Users of Clusters with Kerberos Authentication Enabled](default-users-of-clusters-with-kerberos-authentication-enabled.md)
        -   [Changing the Password for an OS User](changing-the-password-for-an-os-user.md)
        -   [Changing the Password for User admin](changing-the-password-for-user-admin.md)
        -   [Changing the Password for the Kerberos Administrator](changing-the-password-for-the-kerberos-administrator.md)
        -   [Changing the Password for the LDAP Administrator and the LDAP User \(including OMS LDAP\)](changing-the-password-for-the-ldap-administrator-and-the-ldap-user-(including-oms-ldap).md)
        -   [Changing the Password for a Component Running User](changing-the-password-for-a-component-running-user.md)
        -   [Changing the Password for the OMS Database Administrator](changing-the-password-for-the-oms-database-administrator.md)
        -   [Changing the Password for the Data Access User of the OMS Database](changing-the-password-for-the-data-access-user-of-the-oms-database.md)
        -   [Changing the Password for a Component Database User](changing-the-password-for-a-component-database-user.md)
        -   [Replacing HA Certificates](replacing-ha-certificates.md)
        -   [Updating the Key of a Cluster](updating-the-key-of-a-cluster.md)

    -   [Patch Operation Guide]
        -   [Patch Operation Guide for Versions Earlier than MRS 1.7.0](patch-operation-guide-for-versions-earlier-than-mrs-1-7-0.md)
        -   [Patch Operation Guide for MRS 1.7.0 or Later](patch-operation-guide-for-mrs-1-7-0-or-later.md)

    -   [Restoring Patches for the Isolated Hosts](restoring-patches-for-the-isolated-hosts.md)
    -   [Performing Rolling Restart](performing-rolling-restart.md)

-   [MRS Multi-User Permission Management]
    -   [Users and Permissions of Clusters with Kerberos Authentication Enabled](users-and-permissions-of-clusters-with-kerberos-authentication-enabled.md)
    -   [Default Users of Clusters with Kerberos Authentication Enabled](default-users-of-clusters-with-kerberos-authentication-enabled_kerberos.md)
    -   [Creating a Role](creating-a-role.md)
    -   [Creating a User Group](creating-a-user-group.md)
    -   [Creating a User](creating-a-user.md)
    -   [Modifying User Information](modifying-user-information.md)
    -   [Locking a User](locking-a-user.md)
    -   [Unlocking a User](unlocking-a-user.md)
    -   [Deleting a User](deleting-a-user.md)
    -   [Changing the Password of an Operation User](changing-the-password-of-an-operation-user.md)
    -   [Initializing the Password of a System User](initializing-the-password-of-a-system-user.md)
    -   [Downloading a User Authentication File](downloading-a-user-authentication-file.md)
    -   [Modifying a Password Policy](modifying-a-password-policy.md)
    -   [Configuring Cross-Cluster Mutual Trust Relationships](configuring-cross-cluster-mutual-trust-relationships.md)
    -   [Configuring Users to Access Resources of a Trusted Cluster](configuring-users-to-access-resources-of-a-trusted-cluster.md)

-   [Using MRS]
    -   [Accessing the UI of the Open Source Component]
        -   [List of Open Source Component Ports](list-of-open-source-component-ports.md)
        -   [Overview](web-uis-of-open-source-components.md)
        -   [Creating an SSH Channel to Connect an MRS Cluster and Configuring the Browser](creating-an-ssh-channel-to-connect-an-mrs-cluster-and-configuring-the-browser.md)
        -   [Configuring a Website Accessed by Browsers](configuring-a-website-accessed-by-browsers.md)

    -   [Using Hadoop from Scratch](using-hadoop-from-scratch.md)
    -   [Using Spark SQL from Scratch](using-spark-sql-from-scratch.md)
    -   [Using HBase from Scratch](using-hbase-from-scratch.md)
    -   [Using Hive from Scratch](using-hive-from-scratch.md)
    -   [Using Spark]
        -   [Using Spark from Scratch](using-spark-from-scratch.md)
        -   [Accessing the Spark Web UI](accessing-the-spark-web-ui.md)
        -   [Interconnecting Spark with OpenTSDB]
            -   [Creating a Table and Associating It with OpenTSDB](creating-a-table-and-associating-it-with-opentsdb.md)
            -   [Inserting Data to the OpenTSDB Table](inserting-data-to-the-opentsdb-table.md)
            -   [Querying an OpenTSDB Table](querying-an-opentsdb-table.md)
            -   [Modifying the Default Configuration Data](modifying-the-default-configuration-data.md)


    -   [Using Hue]
        -   [Accessing the Hue WebUI](accessing-the-hue-webui.md)
        -   [Using HiveQL Editor on the Hue WebUI](using-hiveql-editor-on-the-hue-webui.md)
        -   [Using the Metadata Browser on the Hue WebUI](using-the-metadata-browser-on-the-hue-webui.md)
        -   [Using File Browser on the Hue WebUI](using-file-browser-on-the-hue-webui.md)
        -   [Using Job Browser on the Hue WebUI](using-job-browser-on-the-hue-webui.md)

    -   [Using Kafka]
        -   [Managing Kafka Topics](managing-kafka-topics.md)
        -   [Querying Kafka Topics](querying-kafka-topics.md)
        -   [Managing Kafka User Permission](managing-kafka-user-permission.md)
        -   [Managing Messages in Kafka Topics](managing-messages-in-kafka-topics.md)

    -   [Using Storm]
        -   [Submitting Storm Topologies on the Client](submitting-storm-topologies-on-the-client.md)
        -   [Accessing the Storm WebUI](accessing-the-storm-webui.md)
        -   [Managing Storm Topologies](managing-storm-topologies.md)
        -   [Querying Storm Topology Logs](querying-storm-topology-logs.md)

    -   [Using CarbonData]
        -   [Getting Started with CarbonData](getting-started-with-carbondata.md)
        -   [About CarbonData Table](about-carbondata-table.md)
        -   [Creating a CarbonData Table](creating-a-carbondata-table.md)
        -   [Deleting a CarbonData Table](deleting-a-carbondata-table.md)

    -   [Using Flume]
        -   [Introduction](introduction_flume.md)
        -   [Installing the Flume Client](installing-the-flume-client.md)
        -   [Viewing Flume Client Logs](viewing-flume-client-logs.md)
        -   [Stopping or Uninstalling the Flume Client](stopping-or-uninstalling-the-flume-client.md)
        -   [Using the Encryption Tool of the Flume Client](using-the-encryption-tool-of-the-flume-client.md)
        -   [Flume Configuration Parameter Description](flume-configuration-parameter-description.md)
        -   [Example: Using Flume to Collect Logs and Import Them to Kafka](example-using-flume-to-collect-logs-and-import-them-to-kafka.md)
        -   [Example: Using Flume to Collect Logs and Import Them to OBS](example-using-flume-to-collect-logs-and-import-them-to-obs.md)
        -   [Example: Using Flume to Read OBS Files and Upload Them to HDFS](example-using-flume-to-read-obs-files-and-upload-them-to-hdfs.md)

    -   [Using Loader]
        -   [Introduction](introduction_loader.md)
        -   [Loader Link Configuration](loader-link-configuration.md)
        -   [Managing Loader Links](managing-loader-links.md)
        -   [Source Link Configurations of Loader Jobs](source-link-configurations-of-loader-jobs.md)
        -   [Destination Link Configurations of Loader Jobs](destination-link-configurations-of-loader-jobs.md)
        -   [Managing Loader Jobs](managing-loader-jobs.md)
        -   [Preparing a Driver for MySQL Database Link](preparing-a-driver-for-mysql-database-link.md)
        -   [Example: Using Loader to Import Data from OBS to HDFS](example-using-loader-to-import-data-from-obs-to-hdfs.md)

    -   [Using Presto]
        -   [Accessing the Presto Web UI](accessing-the-presto-web-ui.md)
        -   [Using a Client to Execute Query Statements](using-a-client-to-execute-query-statements.md)
        -   [Configuring Presto Permissions](configuring-presto-permissions.md)

    -   [Using KafkaManager]
        -   [Introduction to KafkaManager](introduction-to-kafkamanager.md)
        -   [Accessing the KafkaManager Web UI](accessing-the-kafkamanager-web-ui.md)
        -   [Managing Kafka Clusters](managing-kafka-clusters.md)
        -   [Kafka Cluster Monitoring Management](kafka-cluster-monitoring-management.md)

    -   [Using OpenTSDB]
        -   [Using an MRS Client to Operate OpenTSDB Metric Data](using-an-mrs-client-to-operate-opentsdb-metric-data.md)
        -   [Running the curl Command to Operate OpenTSDB](running-the-curl-command-to-operate-opentsdb.md)

    -   [Using Flink]
        -   [Using Flink from Scratch](using-flink-from-scratch.md)
        -   [Configuring and Managing Flink](configuring-and-managing-flink.md)
        -   [Security Configuration](security-configuration.md)
        -   [Security Hardening](security-hardening.md)
        -   [Introduction to Logs](introduction-to-logs.md)
        -   [Performance Tuning](performance-tuning.md)
        -   [Shell Commands](shell-commands.md)

    -   [Using Alluxio]
        -   [Configuring an Underlying Storage System](configuring-an-underlying-storage-system.md)
        -   [Accessing Alluxio Using a Data Application](accessing-alluxio-using-a-data-application.md)
        -   [Common Operations of Alluxio](common-operations-of-alluxio.md)

    -   [Using Ranger]
        -   [Creating a Ranger Cluster](creating-a-ranger-cluster.md)
        -   [Accessing the Ranger Web UI and Synchronizing Unix users to the Ranger Web UI](accessing-the-ranger-web-ui-and-synchronizing-unix-users-to-the-ranger-web-ui.md)
        -   [Configuring Hive Access Permissions in Ranger](configuring-hive-access-permissions-in-ranger.md)
        -   [Configuring HBase Access Permissions in Ranger](configuring-hbase-access-permissions-in-ranger.md)

    -   [Using MRS Components to Access OBS]
        -   [Accessing OBS Using s3a](accessing-obs-using-s3a.md)
        -   [Accessing OBS Using obs](accessing-obs-using-obs.md)


-   [FAQs]
    -   [What Is MRS?](what-is-mrs.md)
    -   [What Are the Highlights of MRS?](what-are-the-highlights-of-mrs.md)
    -   [What Is MRS Used For?](what-is-mrs-used-for.md)
    -   [How Do I Use MRS?](how-do-i-use-mrs.md)
    -   [How Do I Ensure Data and Service Running Security?](how-do-i-ensure-data-and-service-running-security.md)
    -   [How Do I Prepare a Data Source for MRS?](how-do-i-prepare-a-data-source-for-mrs.md)
    -   [What Is the Difference Between Data in OBS and That in HDFS?](what-is-the-difference-between-data-in-obs-and-that-in-hdfs.md)
    -   [How Do I View All Clusters?](how-do-i-view-all-clusters.md)
    -   [How Do I View Log Information?](how-do-i-view-log-information.md)
    -   [What Types of Jobs Are Supported by MRS?](what-types-of-jobs-are-supported-by-mrs.md)
    -   [How Do I Submit Developed Programs to MRS?](how-do-i-submit-developed-programs-to-mrs.md)
    -   [How Do I View Cluster Configurations?](how-do-i-view-cluster-configurations.md)
    -   [What Types of Host Specifications Are Supported by MRS?](what-types-of-host-specifications-are-supported-by-mrs.md)
    -   [What Components Are Supported by MRS?](what-components-are-supported-by-mrs.md)
    -   [What Is the Relationship Between Spark and Hadoop?](what-is-the-relationship-between-spark-and-hadoop.md)
    -   [What Types of Spark Jobs Are Supported by an MRS Cluster?](what-types-of-spark-jobs-are-supported-by-an-mrs-cluster.md)
    -   [Can a Spark Cluster Access Data in OBS?](can-a-spark-cluster-access-data-in-obs.md)
    -   [What Is the Relationship Between Hive and Other Components?](what-is-the-relationship-between-hive-and-other-components.md)
    -   [What Types of Distributed Storage Are Supported by MRS?](what-types-of-distributed-storage-are-supported-by-mrs.md)
    -   [Can MRS Cluster Nodes Be Changed on the MRS Management Console?](can-mrs-cluster-nodes-be-changed-on-the-mrs-management-console.md)

-   [ECS Specifications Used by MRS](ecs-specifications-used-by-mrs.md)
