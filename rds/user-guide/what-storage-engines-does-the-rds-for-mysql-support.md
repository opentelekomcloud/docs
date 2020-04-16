# What Storage Engines Does the RDS for MySQL Support?<a name="rds_faq_0041"></a>

Database storage engine is a core service for  **storing, processing, and protecting data**. It can be used to control access permissions and rapidly process transactions to meet enterprise requirements.

For MySQL databases, only the InnoDB storage engine supports backup and restoration functions and is therefore recommended.

For versions later than MySQL 5.6.40 and 5.7.22, some storage engines are no longer supported.

RDS for MySQL now does not support MyISAM due to the following reasons:

-   MyISAM engine tables do not support transactions and support only table-level locks. As a result, read and write operations conflict with each other.
-   MyISAM has a defect in protecting data integrity, which may cause database data damage or even data loss.
-   If data is damaged, MyISAM does not support data restoration provided by RDS for MySQL and requires manual restoration.
-   Data can be transparently migrated from MyISAM to InnoDB, which does not require code modification for tables.

RDS for MySQL now does not support FEDERATED due to the following reasons:

-   Same DML operations are repeatedly executed on remote databases, causing data disorder.
-   During the PITR restoration, data on remote databases is not restored to the status when the full backup is created after the full restoration phase is complete. Applying data during the incremental restoration will disorder FEDERATED table data.

RDS for MySQL now does not support MEMORY due to the following reasons:

-   If a memory table becomes empty after a restart, the database generates a DELETE event to the binlog when the table is opened. If primary/standby DB instances use memory tables and the standby database \(or read-only database\) is restarted, a GTID is generated, which is inconsistent with that of the primary database. As a result, the standby database is rebuilt.
-   Using memory tables may cause out-of-memory \(OOM\) and even service termination.

