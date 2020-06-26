# What Types of DB Engines Does RDS Support for Importing Data?<a name="rds_faq_0025"></a>

-   Exporting or importing data between DB engines of the same type is called homogeneous database export or import.
-   Exporting or importing data between DB engines of different types is called heterogeneous database export or import. For example, import data from Oracle to DB engines supported by RDS.

    Data cannot be exported or imported between heterogeneous databases due to different data formats. However, if the data formats are compatible, table data can also be imported theoretically.

    Generally, third-party software is required for data replication to export and import between heterogeneous databases. For example, you can use a third-party tool to export table records from Oracle in .txt format. Then, you can use Load statements to import the exported table records to the DB engines supported by RDS.


