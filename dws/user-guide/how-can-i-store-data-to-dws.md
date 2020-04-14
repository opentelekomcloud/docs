# How Can I Store Data to DWS?<a name="dws_03_0027"></a>

DWS supports efficient data import from multiple data sources. The following lists typical data import modes. For details, see section  **Data Import**  in the  [Data Warehouse Service Database Developer Guide](https://docs.otc.t-systems.com/en-us/dws/index.html).

-   Import data from OBS.

    Upload data to the OBS and import data from the OBS to data warehouse clusters. Data formats such as CSV and TEXT are supported.


-   Run the  **INSERT**  statement to insert data.

    Use the gsql client tool provided by DWS or the JDBC/ODBC driver to write data to DWS from upper-layer applications. DWS supports complete database transaction-level CRUD operations. This is the simplest method and is applicable to scenarios with small data volume and low concurrency.


-   Import data from MRS and use MRS as the ETL. 

-   Run the  **COPY FROM STDIN**  command to import data.

    You can run the  **COPY FROM STDIN**  command to write data to a table.

-   Use GDS to import data from a remote server to DWS.

    When you need to import data files from a common file system \(for example, an ECS\) to DWS, use the GDS data import function provided by DWS.


