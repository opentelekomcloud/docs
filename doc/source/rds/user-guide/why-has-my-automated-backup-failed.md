# Why Has My Automated Backup Failed?<a name="rds_faq_0053"></a>

Automated backup failures may be caused by the following reasons:

1.  The network environment is unstable, due to issues such as network delay or interruption. RDS will detect these problems and trigger an automated backup after half an hour. You can also perform a manual backup before then.
2.  Multi-task executions are complicated, resulting in problems such as task waiting or interruption. RDS will detect these problems and trigger an automated backup half an hour later. You can also perform a manual backup in time.
3.  A DB instance status is unavailable, possibly because the DB instance is faulty or being modified. RDS will trigger an automated backup after the DB instance status becomes available. You can also perform a manual backup before then.
4.  A parameter change is incorrect. For example, a DB instance may be faulty after a parameter template containing incorrectly changed parameters apply to it. You can check whether original and current values are correct, check whether any related parameters also need to be changed, reset the parameter template, or reboot the DB instance.
5.  An error has occurred during data import.

    For example, system table records get lost due to inappropriate data import.

    For MySQL, you can import data again by referring to section  [Migrating MySQL Data Using mysqldump](migrating-mysql-data-using-mysqldump.md).

    For PostgreSQL, you can import data again by referring to section  [Migrating PostgreSQL Data Using psql](migrating-postgresql-data-using-psql.md).

    For Microsoft SQL Server, you can import data again by referring to section  [Migrating SQL Server Data Using SQL Server Management Studio](migrating-sql-server-data-using-sql-server-management-studio.md).

    If the problem persists, contact technical support.


