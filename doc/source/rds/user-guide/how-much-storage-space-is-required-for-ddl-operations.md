# How Much Storage Space Is Required for DDL Operations?<a name="rds_faq_0082"></a>

Data Definition Language \(DDL\) operations may increase storage space usage sharply. To ensure that services are running properly, do not perform DDL operations during peak hours. If DDL operations are required, ensure that storage space is 10 GB greater than or equal to twice the size of the tablespace. For example, if your tablespace is 500 GB, ensure that storage space is greater than or equal to 1010 GB \(500 GB x 2 + 10 GB\).

