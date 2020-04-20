# User Guide

-   [Introduction]
    -   [What Is DDS?](what-is-dds.md)
    -   [Basic Concepts]
        -   [Cluster](cluster.md)
        -   [Database Parameter Group](database-parameter-group.md)
        -   [Regions and AZs](regions-and-azs.md)

    -   [Product Advantages]
        -   [High Reliability](high-reliability.md)
        -   [High Security](high-security.md)
        -   [Ease of Use](ease-of-use.md)
        -   [Scalability](scalability.md)

    -   [Cluster Architecture](cluster-architecture.md)
    -   [Replica Set Architecture](replica-set-architecture.md)
    -   [DDS DB Instance]
        -   [DB Instance Specifications](db-instance-specifications.md)
        -   [Database Engine and Version](database-engine-and-version.md)
        -   [Database Status](database-status.md)

    -   [Typical Application Scenarios](typical-application-scenarios.md)
    -   [Related Services](related-services.md)
    -   [User Permissions](user-permissions.md)

-   [Logging In to the DDS Console](logging-in-to-the-dds-console.md)
-   [Cluster]
    -   [Service Process](service-process(cluster).md)
    -   [Restrictions](restrictions(cluster).md)
    -   [Creating a Cluster Instance](creating-a-cluster-instance.md)
    -   [Setting a Security Group](setting-a-security-group(cluster).md)
    -   [Connecting to a Cluster Instance]
        -   [Binding and Unbinding an EIP](binding-and-unbinding-an-eip(cluster).md)
        -   [Enabling or Disabling SSL](enabling-or-disabling-ssl(cluster).md)
        -   [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(cluster).md)


-   [Replica Set]
    -   [Service Process](service-process(replica-set).md)
    -   [Restrictions](restrictions(replica-set).md)
    -   [Creating a Replica Set Instance](creating-a-replica-set-instance.md)
    -   [Setting a Security Group ](setting-a-security-group(replica-set).md)
    -   [Connecting to a Replica Set Instance]
        -   [Binding and Unbinding an EIP](binding-and-unbinding-an-eip(replica-set).md)
        -   [Enabling or Disabling SSL](enabling-or-disabling-ssl(replica-set).md)
        -   [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(replica-set).md)


-   [Managing DDS DB Instances]
    -   [DB Instance Operations]
        -   [Modifying the DB Instance Name](modifying-the-db-instance-name.md)
        -   [Manually Switching the Primary and Secondary Nodes of a Replica Set](manually-switching-the-primary-and-secondary-nodes-of-a-replica-set.md)
        -   [Restarting a DB Instance or a Node](restarting-a-db-instance-or-a-node.md)
        -   [Deleting a DB instance](deleting-a-db-instance.md)

    -   [Managing Database Accounts](managing-database-accounts.md)
    -   [Migrating Data](migrating-data.md)
    -   [Backup and Restore]
        -   [Setting Automated Backup Policy](setting-automated-backup-policy.md)
        -   [Creating a Manual Backup](creating-a-manual-backup.md)
        -   [Restoring a Cluster Instance from a Backup](restoring-a-cluster-instance-from-a-backup.md)
        -   [Restoring a Replica Set Instance from a Backup](restoring-a-replica-set-instance-from-a-backup.md)
        -   [Downloading Backup Files](downloading-backup-files.md)
        -   [Deleting a Manual Backup](deleting-a-manual-backup.md)
        -   [Deleting an Automated Backup](deleting-an-automated-backup.md)

    -   [Parameter Group]
        -   [Creating a Parameter Group](creating-a-parameter-group.md)
        -   [Editing a Parameter Group](editing-a-parameter-group.md)
        -   [Comparing Two Parameter Groups](comparing-two-parameter-groups.md)
        -   [Replicating a Parameter Group](replicating-a-parameter-group.md)
        -   [Changing Associated Parameter Group](changing-associated-parameter-group.md)
        -   [Resetting a Parameter Group](resetting-a-parameter-group.md)
        -   [Changing a Parameter Group Description](changing-a-parameter-group-description.md)
        -   [Deleting a Parameter Group](deleting-a-parameter-group.md)

    -   [Storage]
        -   [Adding Cluster Instance Nodes](adding-cluster-instance-nodes.md)
        -   [Reverting Cluster Instance Nodes](reverting-cluster-instance-nodes.md)
        -   [Scaling Up Storage Space](scaling-up-storage-space.md)

    -   [Changing DB Instance Classes]
        -   [Changing the CPU or Memory of a Cluster DB Instance](changing-the-cpu-or-memory-of-a-cluster-db-instance.md)
        -   [Changing the CPU or Memory of a Replica Set DB Instance](changing-the-cpu-or-memory-of-a-replica-set-db-instance.md)

    -   [Security]
        -   [Resetting the Administrator Password](resetting-the-administrator-password.md)
        -   [Changing the Database Port](changing-the-database-port.md)
        -   [Changing a Security Group](changing-a-security-group.md)

    -   [Tag](tag.md)
    -   [Task Center](task-center.md)

-   [Monitoring]
    -   [Interconnected with Cloud Eye]
        -   [DDS Metrics](dds-metrics.md)
        -   [Setting Alarm Rules](setting-alarm-rules.md)
        -   [Viewing DDS Metrics](viewing-dds-metrics.md)

    -   [Interconnecting with CTS]
        -   [Key Operations Recorded by CTS](key-operations-recorded-by-cts.md)
        -   [Querying Traces](querying-traces.md)

    -   [Error Log](error-log.md)
    -   [Slow Query Log](slow-query-log.md)

-   [FAQs]
    -   [Common FAQs]
        -   [What Precautions Should Be Taken When Using DDS?](what-precautions-should-be-taken-when-using-dds.md)
        -   [What Is the Availability of DDS DB Instances?](what-is-the-availability-of-dds-db-instances.md)
        -   [Can I Use a Template to Create DDS DB Instances?](can-i-use-a-template-to-create-dds-db-instances.md)
        -   [Will My DDS DB Instances Be Affected by Other Users' DDS DB Instances?](will-my-dds-db-instances-be-affected-by-other-users-dds-db-instances.md)

    -   [Management FAQs]
        -   [What Should I Do If My Query Is Slow?](what-should-i-do-if-my-query-is-slow.md)
        -   [What Is the Time Delay for Primary/Secondary Synchronization in a Replica Set?](what-is-the-time-delay-for-primary-secondary-synchronization-in-a-replica-set.md)
        -   [Why Is Data Missing from My Database?](why-is-data-missing-from-my-database.md)
        -   [Will My Backups Be Deleted If I Delete My Cloud Account?](will-my-backups-be-deleted-if-i-delete-my-cloud-account.md)
        -   [Are My DDS DB Instances Available When Scaling?](are-my-dds-db-instances-available-when-scaling.md)
        -   [Does DDS Support Read/Write Splitting?](does-dds-support-read-write-splitting.md)

    -   [Connection and Access FAQs]
        -   [Can an External Server Access the DDS DB Instance?](can-an-external-server-access-the-dds-db-instance.md)
        -   [What Is the Number of DDS Database Connections?](what-is-the-number-of-dds-database-connections.md)
        -   [What Should I Do If the ECS Cannot Connect to a DDS DB Instance?](what-should-i-do-if-the-ecs-cannot-connect-to-a-dds-db-instance.md)
        -   [What Should I Do If a Database Client Problem Causes a Connection Failure?](what-should-i-do-if-a-database-client-problem-causes-a-connection-failure.md)
        -   [What Should I Do If a DDS Server Problem Causes a Connection Failure?](what-should-i-do-if-a-dds-server-problem-causes-a-connection-failure.md)
        -   [How Can My Applications Access a DDS DB Instance in a VPC?](how-can-my-applications-access-a-dds-db-instance-in-a-vpc.md)
        -   [Do Applications Need to Support Automatic Reconnecting to the DDS Database?](do-applications-need-to-support-automatic-reconnecting-to-the-dds-database.md)
        -   [How Can I Create and Log In to an ECS?](how-can-i-create-and-log-in-to-an-ecs.md)
        -   [How Can I Install a MongoDB Client?](how-can-i-install-a-mongodb-client.md)

    -   [Parameter and Metric FAQs]
        -   [What DB Instance Monitoring Metrics Do I Need to Pay Attention To?](what-db-instance-monitoring-metrics-do-i-need-to-pay-attention-to.md)

    -   [Network and Security FAQs]
        -   [What Security Protection Policies Does DDS Have?](what-security-protection-policies-does-dds-have.md)
        -   [Do I Need to Use DDS in a VPC?](do-i-need-to-use-dds-in-a-vpc.md)
        -   [How Do I Ensure the Security of DDS in a VPC?](how-do-i-ensure-the-security-of-dds-in-a-vpc.md)

    -   [Storage FAQs]
        -   [How Do I Back Up DDS to ECS?](how-do-i-back-up-dds-to-ecs.md)
        -   [How Long Does DDS Store Backup Data For?](how-long-does-dds-store-backup-data-for.md)
        -   [What Is the DDS DB Instance Storage Configuration?](what-is-the-dds-db-instance-storage-configuration.md)
        -   [What Should I Do If My Data Exceeds the Database Storage Space of a DDS DB Instance?](what-should-i-do-if-my-data-exceeds-the-database-storage-space-of-a-dds-db-instance.md)
        -   [Which Items Occupy the Storage Space on My Purchased DDS DB Instances?](which-items-occupy-the-storage-space-on-my-purchased-dds-db-instances.md)
        -   [What Overhead Does the Storage Space Have After I Applied for a DDS DB Instance?](what-overhead-does-the-storage-space-have-after-i-applied-for-a-dds-db-instance.md)
        -   [Which Types of Logs and Files Occupy DDS DB Instance Storage Space?](which-types-of-logs-and-files-occupy-dds-db-instance-storage-space.md)

    -   [Which Commands are Supported or Restricted by DDS?](which-commands-are-supported-or-restricted-by-dds.md)

-   [Glossary](glossary.md)

