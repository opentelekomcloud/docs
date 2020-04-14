# How Long Does CSBS Take to Back Up and Restore an ECS?<a name="EN-US_TOPIC_0056584605"></a>

The initial backup for an ECS is a full backup and subsequent backup operations are all incremental backups. Therefore, the initial backup takes a long time and subsequent incremental operations take shorter times. For example, a full backup of a 100 GB ECS takes approximately 30 minutes, and an incremental backup of 15 GB takes approximately 6 minutes.

After the instant restoration function is enabled for CSBS, it takes about several minutes to restore 100 GB data.

