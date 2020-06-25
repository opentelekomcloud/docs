# Hive<a name="EN-US_TOPIC_0125375907"></a>

Hive is a data warehouse framework built on Hadoop. It stores structured data using the Hive query language \(HiveQL\), a language similar to SQL.

Hive converts HiveQL statements to MapReduce or HDFS tasks to query and analyze massive data stored in Hadoop clusters. The console provides the interface to enter Hive Script and supports the online submission of HiveQL statements.

Hive supports the HDFS Colocation, column encryption, HBase deletion, row delimiter, and CSV SerDe functions, as detailed below.

## HDFS Colocation<a name="sc5dc14ad36984011b77107d92d19bf8b"></a>

HDFS Colocation is the data location control function provided by HDFS. The HDFS Colocation interface stores associated data or data on which associated operations are performed on the same storage node.

Hive supports the HDFS Colocation function. When Hive tables are created, after the locator information is set for table files, the data files of related tables are stored on the same storage node. This ensures convenient and efficient data computing among associated tables.

## Column Encryption<a name="sab4419ffd8ed4677846225534b8c199f"></a>

Hive supports encryption of one or more columns. The columns to be encrypted and the encryption algorithm can be specified when a Hive table is created. When data is inserted into the table using the insert statement, the related columns are encrypted.

The Hive column encryption mechanism supports two encryption algorithms that can be selected to meet site requirements during table creation:

-   AES \(the encryption class is  **org.apache.hadoop.hive.serde2.AESRewriter**\)
-   SMS4 \(the encryption class is  **org.apache.hadoop.hive.serde2.SMS4Rewriter**\)

## HBase Deletion<a name="sa8d6162012584fae903ae0e60b01f386"></a>

Due to the limitations of underlying storage systems, Hive does not support the ability to delete a single piece of table data. In Hive on HBase, MRS Hive supports the ability to delete a single piece of HBase table data. Using a specific syntax, Hive can delete one or more pieces of data from an HBase table.

## Row Delimiter<a name="se1888eaf88164d889eb3bd1e3bf9efbb"></a>

In most cases, a carriage return character is used as the row delimiter in Hive tables stored in text files, that is, the carriage return character is used as the terminator of a row during searches. However, some data files are delimited by special characters, and not a carriage return character.

MRS Hive allows users to use different characters or character combinations to delimit rows of Hive text data. When creating a table, set  **inputformat** to **SpecifiedDelimiterInputFormat**, and set the following parameter before each search.

```
set hive.textinput.record.delimiter='';
```

The table data is then queried by the specified delimiter.

## CSV SerDe<a name="s8b9607b3160644d4a290d18bdc65d0a8"></a>

Comma separated value \(CSV\) is a common text file format. CSV stores table data \(digits and texts\) in texts and uses a comma \(,\) as the text delimiter.

CSV files are universal. Many applications allow users to view and edit CSV files in Windows Office or conventional databases.

MRS Hive supports CSV files. Users can import CSV files to Hive tables or export user Hive table data as CSV files to use them in other applications.

