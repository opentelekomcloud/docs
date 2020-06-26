# Using the Metadata Browser on the Hue WebUI<a name="EN-US_TOPIC_0125376152"></a>

## Scenario<a name="sa0b3fd49e97b4c4cac638ad732bae017"></a>

After Kerberos authentication is enabled for an MRS cluster, users can use the Hue WebUI to manage Hive metadata in the cluster.

## Prerequisites<a name="s1c00062404c643799e721495e7ef115a"></a>

The MRS cluster administrator has assigned the permission for using Hive to the user. For details, see  [Creating a Role](creating-a-role.md).

## Accessing the Metadata Browser<a name="section1025775173647"></a>

1.  Access the Hue WebUI.
2.  Choose  **Data Browsers**  \>  **Metastore Tables** to access **Metastore Manager**.

    **Metastore Manager**  supports the following functions.

    -   Creating a Hive table from a file
    -   Manually creating a Hive table
    -   Viewing Hive table metadata


## Creating a Hive Table from a File<a name="section5307604817374"></a>

1.  Access  **Metastore Manager** and select a database in **Databases**.

    The default database is  **default**.

2.  Click  ![](figures/icon_mrs_dbcrate.jpg) to access the **Create a new table from a file**  page.
3.  Select a file.
    1.  In  **Table Name**, enter a Hive table name.

        A Hive table name contains no more than 128 letters, numbers, or underscores \(\_\) and must start with a letter or number.

    2.  In  **Description**, enter description about the Hive table as required.
    3.  In  **Input File or Location**, click ![](figures/icon_mrs_dbmanu.jpg)  and select a file in HDFS for creating a Hive table. The file is used to store new data of the Hive table.

        If the file is not stored in HDFS, click  **Upload a file**  to upload the file from the local directory to HDFS. Multiple files can be simultaneously uploaded. The files cannot be empty.

    4.  If you want to import data in the file to the Hive table, select  **Import data** \(selected by default\) in **Load method**.

        If you select  **Create External Table**, an external Hive table is created.

        >![](/images/icon-note.gif) **NOTE:**   
        >If you select  **Create External Table**, select a path in **Input File or Location**.  

        If you select  **Leave Empty**, an empty Hive table is created.

    5.  Click  **Next**.

4.  Set a delimiter.
    1.  In  **Delimiter**, select one.

        If the delimiter you want to select is not in the list, select  **Other..**  and enter a delimiter.

    2.  Click  **Preview**  to preview data processing.
    3.  Click  **Next**.

5.  Define a column.
    1.  If you click  ![](figures/icon_mrs_hue_columnname.jpg) on the right side of **Use first row as column names**, the first row of data in the file is used as a column name. If you do not click it, the first row of data is not used as the column name.
    2.  In  **Column name**, set a name for each column.

        A Hive table name contains no more than 128 letters, numbers, or underscores \(\_\) and must start with a letter or number.

        >![](/images/icon-note.gif) **NOTE:**   
        >You can rename columns in batches by clicking  ![](figures/icon_mrs_edit.jpg) on the right side of **Bulk edit column names**. Enter all column names and separate them by commas \(,\).  

    3.  In  **Column Type**, select a type for each column.

6.  Click  **Create Table**  to create the table. Wait for Hue to display information about the Hive table.

## Manually Creating a Hive Table<a name="section65667144173717"></a>

1.  Access  **Metastore Manager** and select a database in **Databases**.

    The default database is  **default**.

2.  Click  ![](figures/icon_mrs_jiahao.png) to access the **Create a new table manually**  page.
3.  Set a table name.
    1.  In  **Table Name**, enter a Hive table name.

        A Hive table name contains no more than 128 letters, numbers, or underscores \(\_\) and must start with a letter or number.

    2.  In  **Description**, enter description about the Hive table as required.
    3.  Click  **Next**.

4.  Select a data storage format.
    -   If data needs to be separated by delimiters, select  **Delimited** and perform [5](#li47125026173721).
    -   If data needs to be stored in serialization format, select  **SerDe** and perform [6](#li63447897173721).

5.  <a name="li47125026173721"></a>Set a delimiter.
    1.  In  **Field terminator**, set a column delimiter.

        If the delimiter you want to select is not in the list, select  **Other..**  and enter a delimiter.

    2.  In  **Collection terminator**, set a delimiter to separate the data set of columns of the **array** type in Hive. For example, the type of a column is array. A value needs to store **employee** and **manager**. The user specifies a colon\(**:**\) as the delimiter. Therefore, the final value is **employee:manager**.
    3.  In  **Map key terminator**, set a delimiter to separate the data set of columns of the **array** type in Hive. For example, the type of a column is map. A value needs to store **home** that is described as **aaa** and **company** that is described as **bbb**. The user defines **|** as the delimiter. Therefore, the final value is **home|aaa:company|bbb**.
    4.  Click  **Next** and perform [7](#li46640436173721).

6.  <a name="li63447897173721"></a>Set serialization properties.
    1.  In  **SerDe Name**, enter the class name of the serialization format: **org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe**.

        Users can expand Hive to support more user-defined serialization classes.

    2.  In  **Serde properties**, enter the value of the serialization format: **"field.delim"="," "colelction.delim"=":" "mapkey.delim"="|"**.
    3.  Click  **Next** and perform [7](#li46640436173721).

7.  <a name="li46640436173721"></a>Select a data table format and click  **Next**.
    -   **TextFile**: indicates that data is stored in text files.
    -   **SequenceFile**: indicates that data is stored in binary files.
    -   **InputFormat**: indicates that data in files is used in the user-defined input and output formats.

        Users can expand Hive to support more user-defined formatting classes.

        1.  In  **InputFormat Class**, enter the class used by input data: **org.apache.hadoop.hive.ql.io.RCFileInputFormat**.
        2.  In  **OutputFormat Class**, enter the class used by output data: **org.apache.hadoop.hive.ql.io.RCFileOutputFormat**.

8.  Select a file storage location and click  **Next**.

    **Use default location** is selected by default. If you want to customize a storage location, deselect the default value and specify a file storage location in **External location**.

9.  Set columns of the Hive table.
    1.  In  **Column name**, set a column name.

        A Hive table name contains no more than 128 letters, numbers, or underscores \(\_\) and must start with a letter or number.

    2.  In  **Column type**, select a column type.

        Click  **Add a column**  to add a new column.

    3.  Click  **Add a partition**  to add partitions for the Hive table, which can improve query efficiency.

10. Click  **Create Table**  to create the table. Wait for Hue to display information about the Hive table.

## Managing the Hive Table<a name="section30310704173731"></a>

1.  Access  **Metastore Manager** and select a database in **Databases**. All tables in the database are displayed on the page.

    The default database is  **default**.

2.  Click a table name in the database to view table details.

    The following operations are supported: importing data, browsing data, deleting tables, and viewing file storage location.

    >![](/images/icon-note.gif) **NOTE:**   
    >When viewing all tables in the database, you can select tables and perform the following operations: viewing tables, browsing data, and delete tables.  


