# CSBS<a name="EN-US_TOPIC_0056725842"></a>

Cloud Server Backup Service \(CSBS\) offers the backup protection service for Elastic Cloud Servers \(ECSs\). It works based on the consistency snapshot technology for Elastic Volume Service \(EVS\) disks, meaning you can seamlessly use backup data to restore ECS data.

CSBS enhances data integrity and service continuity. For example, if an ECS is faulty or a misoperation causes data loss, you can use data backups to restore data quickly.

By default, CSBS executes a full backup for an ECS that has not been backed up using CSBS, and performs incremental backups subsequently. Both full backup and incremental backup can restore an ECS to the state at the backup point in time.

CSBS combines ECS and Object Storage Service \(OBS\) to back up ECS data to object storage, enhancing backup data security.  [Figure 1](#fig11831525164545)  shows the CSBS product architecture.

**Figure  1**  CSBS product architecture<a name="fig11831525164545"></a>  
![](figures/csbs-product-architecture.png "csbs-product-architecture")

## Main Functions<a name="section9652143823013"></a>

CSBS provides the following functions:

-   Policy-driven data backup
-   Data backup management
-   Image creation using backups

