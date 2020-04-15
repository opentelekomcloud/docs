# Deleting a CarbonData Table<a name="EN-US_TOPIC_0125375423"></a>

## Scenario<a name="s06809ac5a988461298f56f1bdbc8677c"></a>

Unused CarbonData tables can be deleted. After a CarbonData table is deleted, its metadata and loaded data are deleted together.

## Procedure<a name="s958672930b05437b94bd6283ab977949"></a>

1.  Run the following command to delete a CarbonData table.

    **DROP TABLE  _\[IF EXISTS\] \[db\_name.\]table\_name_;**

    **db\_name** is optional. If **db\_name** is not specified, the table named **table\_name**  in the current database is deleted.

    For example, run the following command to delete the  **productSalesTable** table in the **productdb**  database:

    **DROP TABLE productdb.productSalesTable;**

2.  Run the following command to check whether the table is deleted.

    **SHOW TABLES;**


