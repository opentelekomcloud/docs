# Why an Error is Reported When I Attempt to Delete a Database from RDS SQL Server Primary/Standby DB Instances?<a name="rds_faq_0094"></a>

## Symptom<a name="section1194933317013"></a>

An error shown in  [Figure 1](#fig162510431417)  is reported on SQL Server Management Studio when a database is being deleted from RDS SQL Server primary/standby DB instances.

**The database 'xxxx' is enabled for database mirroring.Database mirroring must be removed before you drop the database. Error: 3743**

**Figure  1**  Error information<a name="fig162510431417"></a>  
![](figures/error-information.png "error-information")

## Possible Causes<a name="section17291036522"></a>

According to the error information, the SQL Server DB instance type is primary/standby and database mirroring is enabled for the standby DB instance. As a result, the database cannot be deleted.

## Solution<a name="section630415471754"></a>

Before deleting the database, run the following commands to disable the mirroring:

**Use master**

**go**

**ALTER DATABASE **_\[Database\_Name\]_** SET PARTNER OFF;**

**GO**

After the database mirroring is disabled, the database can be deleted.

