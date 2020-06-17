# Creating a Manual Backup<a name="en-us_topic_sqlserver_0037111719"></a>

## **Scenarios**<a name="section16519414134910"></a>

RDS allows you to  create manual backups  of a running primary DB instance. You can use these backups to restore data.

>![](/images/icon-note.gif) **NOTE:**   
>When you delete a DB instance, its automated backups are also deleted but its manual backups are retained.  

## Method 1<a name="section4536153994816"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Create Backup**  in the  **Operation**  column.
5.  In the displayed dialog box, enter a backup name, select a target database for which to create the backup, and enter a description. Then, click  **OK**. If you want to cancel the backup creation task, click  **Cancel**.

    -   The backup name must consist of 4 to 64 characters and start with a letter. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=
    -   The time required for creating a manual backup depends on the data volume.

    >![](/images/icon-note.gif) **NOTE:**   
    >System databases are backed up by default.  

6.  After a manual backup has been created, you can view and manage it on the  **Backup Management**  page.

    Alternatively, click the target DB instance. On the  **Backups & Restorations**  page, you can view and manage the manual backups.


## Method 2<a name="section205381839134819"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Backups & Restorations**  page, click  **Create Backup**. In the displayed dialog box, enter a backup name, select a target database for which to create the backup, and enter a description. Then, click  **OK**.

    -   The backup name must consist of 4 to 64 characters and start with a letter. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=
    -   During the creation process, the DB instance status is  **Backing up**. The time required for creating a manual backup depends on the data volume.

    >![](/images/icon-note.gif) **NOTE:**   
    >System databases are backed up by default.  

6.  After a manual backup has been created, you can view and manage it on the  **Backup Management**  page.

    Alternatively, click the target DB instance. On the  **Backups & Restorations**  page, you can view and manage the manual backups.


## Method 3<a name="section115401139164810"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Backup Management**  page, click  **Create Backup**.
5.  In the displayed dialog box, select a Microsoft SQL Server DB instance, enter a backup name, select a target database for which to create the backup, and enter a description. Then, click  **OK**. If you want to cancel the backup creation task, click  **Cancel**.

    -   A backup can only be created for an available primary DB instance. You cannot create a backup for a DB instance that is being backed up or for which a backup is already being created.
    -   The backup name must consist of 4 to 64 characters and start with a letter. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=
    -   During the creation process, the DB instance status is  **Backing up**. The time required for creating a manual backup depends on the data volume.

    >![](/images/icon-note.gif) **NOTE:**   
    >System databases are backed up by default.  

6.  After a manual backup has been created, you can view and manage it on the  **Backup Management**  page.

    Alternatively, click the target DB instance. On the  **Backups & Restorations**  page, you can view and manage the manual backups.


