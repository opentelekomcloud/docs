# Precautions for Modifying MySQL Parameters<a name="rds_08_00001"></a>

Parameters are key configuration items in a database system. Improperly setting parameters may adversely affect the stable running of databases. This section describes some important parameters for reference. For details, see  [MySQL official website](http://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html).

## Sensitive Parameters<a name="section37541120104511"></a>

Example parameters are as follows:

-   **lower\_case\_table\_names**

    Default value:  **1**

    Function: Controls whether database and tables stored on disks are case sensitive. If the parameter value is set to  **1**, database and table names are lowercase by default. If the parameter value is set to  **0**, names stored and name queries are case sensitive.

    Impact: If you change the parameter value of a primary DB instance, you should also change the parameter values for associated read replica instances and DB instances restored from the backup. For example, tables  **abc**  and  **Abc**  in a primary DB instance is case sensitive, but tables in associated read replica instances and DB instances restored from the backup are case insensitive. During data synchronization and restoration, errors may occur because the table named  **abc**  already exists.

-   **innodb\_flush\_log\_at\_trx\_commit**

    Default value:  **1**

    Function: Controls the balance between strict ACID compliance for commit operations and higher performance. The default setting of  **1**  is required for full ACID compliance. Logs are written and flushed to disk at each transaction commit. If the value is set to  **0**, logs are written and flushed to disk once per second. If the value is set to  **2**, logs are written at each transaction commit and flushed to disk every two seconds.

    Impact: If this parameter is not set to  **1**, data security is not guaranteed. When the system fails, data may be lost.

-   **sync\_binlog**

    Default value:  **1**

    Function: Controls how often the MySQL server synchronizes binary logs to the disk. The default setting of  **1**  requires synchronization of the binary log to disk at each transaction commit. If the value is set to  **0**, synchronization of the binary log to disk is not controlled by the MySQL server but relies on the OS to flush the binary log to disk. This setting provides the best performance, but in the event of a power failure or OS crash, all binary log information in  **binlog\_cache**  is lost.

    Impact: If this parameter is not set to  **1**, data security is not guaranteed. When the system fails, data may be lost.


## Performance Parameters<a name="section5602829104512"></a>

Relevant parameters are as follows:

-   The values of  **innodb\_spin\_wait\_delay**  and  **query\_alloc\_block\_size**  are determined by the DB instance specifications. If you increase their values, database performance may be affected.
-   If  **key\_buffer\_size**  is set to a value smaller than  **4096**, the parameter modification will fail.
-   If  **max\_connections**  is set to a small value, database access will be affected.
-   The default values of the following parameters are determined by the DB instance specifications:  **innodb\_buffer\_pool\_size**,  **max\_connections**, and  **back\_log**. These parameter values are  **default**  before being specified.
-   The values of  **innodb\_io\_capacity\_max**  and  **innodb\_io\_capacity**  are determined by the storage type. These parameter values are  **default**  before being specified.

