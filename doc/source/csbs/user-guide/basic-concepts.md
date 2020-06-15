# Basic Concepts<a name="EN-US_TOPIC_0056725845"></a>

## Backup Policies<a name="section68851082475"></a>

A backup policy is a set of rules for backing up data, including the policy name, policy status, execution time of backup jobs, backup period, and retention rules. The retention rules specify the retention duration and number of retained backups. After an ECS is associated with a backup policy, it can be automatically backed up according to the backup policy.

## Backup<a name="section253702644713"></a>

A backup is generated in a backup operation for a backup object. A backup can be used to restore data of the source backup object. It can be generated in a one-off or periodic method.

CSBS supports one-off backup and periodic backup. A one-off backup job is manually created by users and takes effect for only one time. Periodic backup jobs are automatically driven by a user-defined backup policy.

-   The name of a one-off backup is  **manualbk\_**_xxxx_. It can be user- or system-defined.
-   The name of a periodic backup is assigned automatically by the system. The name of a periodic backup is  **autobk\_**_xxxx_.

## Instant Restore<a name="section181448505477"></a>

Instant Restore is a feature that provides the instant restoration function for restoring ECS data and creating images for backups, which is much faster than the normal restoration function.

Backups generated before the Instant Restore feature is enabled do not support instant restoration. To use the feature, perform a full backup operation and select  **Enable**  next to  **Full Backup**  when creating the backup. For details, see  [Creating a CSBS Backup](creating-a-csbs-backup.md). After Instant Restore is enabled, manual backups for ECSs that have not been backed up automatically support instant restoration, without requiring the selection of  **Enable**  next to  **Full Backup**.

No matter whether an ECS has been backup or not, its automatic backups generated after Instant Restore is enabled do not support instant restoration, unless you manually perform a full backup on it.

## Enhanced backup<a name="section2976161016418"></a>

Backups whose backup type is  **Common backup**  do not support Instant Restore. Backups whose backup type is  **Enhanced backup**  support Instant Restore.

## Project<a name="section1307153125317"></a>

Projects are used to group and isolate OpenStack resources \(computing, storage, and network resources\). A project can be a department or a project team. Multiple projects can be created for one account.

