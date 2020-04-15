# Overview<a name="dws_01_0134"></a>

DWS allows you to access databases using IAM authentication. When you use the JDBC application program to connect to a cluster, set the IAM username, credential, and other information as you configure the JDBC URL. After doing this, when you try to access a database, the system will automatically generate a temporary credential and a connection will be set up.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Currently, only clusters whose version is 1.3.1 or later \(including 1.3.1\) and corresponding JDBC driver provided by DWS can access the databases in IAM authentication mode.  

IAM supports two types of user credential: password and Access Key ID/Secret Access Key \(AK/SK\). JDBC connection requires latter.

The IAM account you use to access a database must be granted with the  **DWS Database Access**  permission. Without this permission, access to databases will fail due to authentication failure.

The process of accessing a database is as follows:

1.  [Granting an IAM Account the DWS Database Access Permission](granting-an-iam-account-the-dws-database-access-permission.md)
2.  [Creating an IAM User Credential](creating-an-iam-user-credential.md)
3.  [Configuring the JDBC Connection to Connect to a Cluster Using IAM Authentication](configuring-the-jdbc-connection-to-connect-to-a-cluster-using-iam-authentication.md)

