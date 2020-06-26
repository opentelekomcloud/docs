# Where Should I Store the NDF Files for Microsoft SQL Server?<a name="rds_faq_0092"></a>

When you add NDF files of the custom database and the tempdb database, do not place them in C drive. If you place them in the C drive, the system disk space will be exhausted and services may be interrupted. You need to store the NDF auxiliary file of the custom database in  **D:\\RDSDBDATA\\DATA**  and the NDF auxiliary file of the tempdb database in  **D:\\RDSDBDATA\\Temp**.

