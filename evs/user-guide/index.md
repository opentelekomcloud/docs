# User Guide

-   [Overview]
    -   [What Is Elastic Volume Service?](what-is-elastic-volume-service.md)
    -   [Disk Types and Disk Performance](disk-types-and-disk-performance.md)
    -   [Device Types and Usage Instructions](device-types-and-usage-instructions.md)
    -   [Shared EVS Disks and Usage Instructions](shared-evs-disks-and-usage-instructions.md)
    -   [EVS Disk Encryption](evs-disk-encryption.md)
    -   [EVS Disk Backup](evs-disk-backup.md)
    -   [EVS Snapshot](evs-snapshot.md)
    -   [EVS Replication \(Deprecated\)](evs-replication-(deprecated).md)
    -   [Differences Among EVS Disk Backup/EVS Snapshot/EVS Replication](differences-among-evs-disk-backup-evs-snapshot-evs-replication.md)
    -   [EVS and Other Services](evs-and-other-services.md)
    -   [Basic Concepts]
        -   [Region and AZ](region-and-az.md)


-   [Getting Started]
    -   [Basic Operation Procedure](basic-operation-procedure.md)
    -   [Create an EVS Disk](create-an-evs-disk.md)
    -   [Attach an EVS Disk]
        -   [Attaching a Non-Shared Disk](attaching-a-non-shared-disk.md)
        -   [Attaching a Shared Disk](attaching-a-shared-disk.md)

    -   [Initialize an EVS Data Disk]
        -   [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md)
        -   [Initializing a Windows Data Disk \(Windows Server 2008\)](initializing-a-windows-data-disk-(windows-server-2008).md)
        -   [Initializing a Windows Data Disk \(Windows Server 2016\)](initializing-a-windows-data-disk-(windows-server-2016).md)
        -   [Initializing a Linux Data Disk \(fdisk\)](initializing-a-linux-data-disk-(fdisk).md)
        -   [Initializing a Linux Data Disk \(parted\)](initializing-a-linux-data-disk-(parted).md)


-   [Disk Capacity Expansion]
    -   [Expansion Overview](expansion-overview.md)
    -   [Expanding Capacity for an In-use EVS Disk](expanding-capacity-for-an-in-use-evs-disk.md)
    -   [Expanding Capacity for an Available EVS Disk](expanding-capacity-for-an-available-evs-disk.md)
    -   [Extending Disk Partitions and File Systems \(Windows\)](extending-disk-partitions-and-file-systems-(windows).md)
    -   [Extending Disk Partitions and File Systems \(Linux\)]
        -   [Partition and File System Extension Preparations \(Linux\)](partition-and-file-system-extension-preparations-(linux).md)
        -   [Extending Partitions and File Systems for System Disks \(Linux\)](extending-partitions-and-file-systems-for-system-disks-(linux).md)
        -   [Extending Partitions and File Systems for Data Disks \(Linux\)](extending-partitions-and-file-systems-for-data-disks-(linux).md)
        -   [Extending Partitions and File Systems for SCSI Disks \(Linux\)](extending-partitions-and-file-systems-for-scsi-disks-(linux).md)


-   [Detaching an EVS Disk]
    -   [Detaching a System Disk](detaching-a-system-disk.md)
    -   [Detaching a Data Disk](detaching-a-data-disk.md)

-   [Deleting an EVS Disk](deleting-an-evs-disk.md)
-   [Managing an Encrypted EVS Disk](managing-an-encrypted-evs-disk.md)
-   [Managing a Shared EVS Disk](managing-a-shared-evs-disk.md)
-   [Managing EVS Backup](managing-evs-backup.md)
-   [Managing EVS Replication \(Deprecated\)]
    -   [EVS Replication Operation Procedure \(Deprecated\)](evs-replication-operation-procedure-(deprecated).md)
    -   [Creating a DR ECS \(Deprecated\)](creating-a-dr-ecs-(deprecated).md)
    -   [Configuring a Virtual IP Address for the Server \(Deprecated\)](configuring-a-virtual-ip-address-for-the-server-(deprecated).md)
    -   [Collecting ECS Information \(Deprecated\)](collecting-ecs-information-(deprecated).md)
    -   [Creating an EVS Replication Pair \(Deprecated\)](creating-an-evs-replication-pair-(deprecated).md)
    -   [Creating a Replication Consistency Group \(Deprecated\)](creating-a-replication-consistency-group-(deprecated).md)
    -   [Updating a Replication Consistency Group \(Deprecated\)](updating-a-replication-consistency-group-(deprecated).md)
    -   [Planned Migration \(Deprecated\)](planned-migration-(deprecated).md)
    -   [Failover \(Deprecated\)](failover-(deprecated).md)
    -   [Reprotection \(Deprecated\)](reprotection-(deprecated).md)
    -   [Expanding EVS Disks in a Replication Consistency Group \(Deprecated\)](expanding-evs-disks-in-a-replication-consistency-group-(deprecated).md)

-   [Managing EVS Disk Transfer](managing-evs-disk-transfer.md)
-   [Managing Snapshots]
    -   [Snapshot Overview](snapshot-overview.md)
    -   [Creating a Snapshot](creating-a-snapshot.md)
    -   [Deleting a Snapshot](deleting-a-snapshot.md)
    -   [Rolling Back Data from a Snapshot](rolling-back-data-from-a-snapshot.md)
    -   [Creating an EVS Disk from a Snapshot](creating-an-evs-disk-from-a-snapshot.md)

-   [Managing a Tag]
    -   [Tag Overview](tag-overview.md)
    -   [Adding a Tag](adding-a-tag.md)
    -   [Modifying a Tag](modifying-a-tag.md)
    -   [Deleting a Tag](deleting-a-tag.md)
    -   [Searching Disks by Tags](searching-disks-by-tags.md)

-   [Viewing EVS Monitoring Data](viewing-evs-monitoring-data.md)
-   [FAQs]
    -   [General FAQs]
        -   [Can EVS Disks Be Used Alone?](can-evs-disks-be-used-alone.md)
        -   [Can I Change the AZ of My Disk?](can-i-change-the-az-of-my-disk.md)
        -   [What Should I Do If an Error Occurs on My EVS Disk?](what-should-i-do-if-an-error-occurs-on-my-evs-disk.md)
        -   [Why Some of My EVS Disks Do Not Have WWN Information?](why-some-of-my-evs-disks-do-not-have-wwn-information.md)
        -   [What Should I Do If My EVS Replication Quotas Are Insufficient? \(Deprecated\)](what-should-i-do-if-my-evs-replication-quotas-are-insufficient-(deprecated).md)

    -   [Disk Capacity Expansion FAQs]
        -   [Can I Reduce the Disk Capacity?](can-i-reduce-the-disk-capacity.md)
        -   [Do I Need to Restart the Server After Expanding the Disk Capacity?](do-i-need-to-restart-the-server-after-expanding-the-disk-capacity.md)
        -   [Do I Need to Detach the Disk from Its Server Before Expanding the Disk Capacity?](do-i-need-to-detach-the-disk-from-its-server-before-expanding-the-disk-capacity.md)
        -   [What Should I Do If My Disk Capacity Exceeds 2 TB After Expansion?](what-should-i-do-if-my-disk-capacity-exceeds-2-tb-after-expansion.md)
        -   [Why My Disk Capacity Remains Unchanged on the Server After Capacity Expansion?](why-my-disk-capacity-remains-unchanged-on-the-server-after-capacity-expansion.md)

    -   [Disk Attachment FAQs]
        -   [Can I Attach a Disk to Multiple Servers?](can-i-attach-a-disk-to-multiple-servers.md)
        -   [Can I Attach a Disk to a Server That Belongs to Another AZ?](can-i-attach-a-disk-to-a-server-that-belongs-to-another-az.md)
        -   [Why I Cannot View the Attached Data Disk on the Server?](why-i-cannot-view-the-attached-data-disk-on-the-server.md)
        -   [How Can I Add a Data Disk to a Server?](how-can-i-add-a-data-disk-to-a-server.md)

    -   [Disk Detachment FAQs]
        -   [Will Data in the EVS Disk Be Lost After the EVS Disk Is Detached?](will-data-in-the-evs-disk-be-lost-after-the-evs-disk-is-detached.md)
        -   [Why My Disk Cannot Be Detached?](why-my-disk-cannot-be-detached.md)

    -   [Capacity FAQs]
        -   [What Is the Maximum Capacity Supported for System Disk and Data Disk Respectively?](what-is-the-maximum-capacity-supported-for-system-disk-and-data-disk-respectively.md)
        -   [What Should I Do If My Disk Space Is Insufficient?](what-should-i-do-if-my-disk-space-is-insufficient.md)
        -   [What Should I Do When My Disk Capacity That Exceeds 2 TB Cannot Be Displayed After I Initialize It Using fdisk?](what-should-i-do-when-my-disk-capacity-that-exceeds-2-tb-cannot-be-displayed-after-i-initialize-it-u.md)
        -   [How Do I View the Space on My Disk?](how-do-i-view-the-space-on-my-disk.md)

    -   [Shared Disk FAQs]
        -   [Do I Must Deploy a Cluster for Using Shared Disks?](do-i-must-deploy-a-cluster-for-using-shared-disks.md)
        -   [How Many Servers Can I Attach a Shared Disk to?](how-many-servers-can-i-attach-a-shared-disk-to.md)


-   [Appendix]
    -   [EVS Disk Status](evs-disk-status.md)
    -   [EVS Snapshot Status](evs-snapshot-status.md)

-   [Change History]
-   [Glossary]

