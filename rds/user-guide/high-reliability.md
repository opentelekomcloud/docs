# High Reliability<a name="rds_01_0005"></a>

## Dual-host Hot Standby<a name="section15162145184712"></a>

RDS uses the hot standby architecture, in which failover upon fault occurrence takes only some seconds.

## Data Backup<a name="section144894164812"></a>

RDS automatically backs up data every day and uploads backup files to Object Storage Service \(OBS\). The backup files can be stored for 732 days and can be restored with just a few clicks. You can set a custom backup policy and create manual backups at any time.

## Data Restoration<a name="section986045820483"></a>

You can restore data from backups or to any point in time during the backup retention period. In most scenarios, you can use backup files to restore data to an existing or a new DB instance at any time point within 732 days. After the data is verified, data can be migrated back to the primary RDS DB instance.

