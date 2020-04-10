# Is the Function of DWS the Same as That of Hive?<a name="dws_03_0037"></a>

DWS and Hive have different functions in the following aspects: 

1.  Hive is a data warehouse based on Hadoop MapReduce, and DWS is a data warehouse based on Postgres MPP.
2.  Hive data is stored on HDFS. DWS data can be stored locally or on OBS in foreign table forms.
3.  Hive does not support indexes. DWS supports indexes, so the query speed is higher.
4.  Hive does not support stored procedures, but DWS does. Therefore, DWS has more extensive application scenarios.
5.  DWS supports more SQL statements than Hive, including functions, customized functions, and stored procedures.
6.  Hive does not support transactions. DWS supports complete transactions.
7.  Both Hive and DWS support backups, so the reliability is the same.
8.  DWS delivers much better performance than Hive.

Based on their respective functions, Hive applies only to offline analysis, and DWS applies to online analysis and Ad hoc queries.

