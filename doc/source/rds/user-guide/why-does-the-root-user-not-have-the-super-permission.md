# Why Does the Root User Not Have the Super Permission?<a name="rds_faq_0075"></a>

Most relational database cloud service platforms do not provide the super permission for the  **root**  user. Once a user has the super permission, the user can execute many management commands, such as reset master, set global, kill, and reset slave. This may cause abnormal primary/standby relationships. This is a major difference between public cloud databases and on-premises MySQL databases. To ensure stable running of DB instances, RDS does not provide the super permission for the  **root**  user.

If you require the super permission, RDS can provide service capabilities or use other methods to bypass the super permission constraints.

For example:

1.  You are not allowed to log in to a database and run the following command to modify parameter values. You can only use the RDS console to modify parameter values.

    **set global parameter name=_Parameter value_;**

    If the script contains the  **set global**  command and causes the super permission loss, delete the  **set global**  command and modify parameter values through the RDS console.

2.  An error will be reported after you run the following command. This is because the  **root**  user does not have the super permission. You can delete  **define='root'**  from the command to solve the problem.

    **create definer='root'@'%' trigger\(procedure\)...**

    If you do not have the super permission, you can use mysqldump to import data. For details, see  [Migrating MySQL Data Using mysqldump](migrating-mysql-data-using-mysqldump.md).

3.  If you do not have the super permission when creating a PostgreSQL plugin, follow the instructions provided in  [Plugin Management](plugin-management.md).

