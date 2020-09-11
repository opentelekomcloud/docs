# Creating a Manual Backup<a name="dds_03_0007"></a>

## **Scenarios**<a name="section618580621992"></a>

This section guides you on how to create a manual backup. Creating a backup for a DB instance helps ensure data can be restored if needed, ensuring data reliability.

>![](/images/icon-note.gif) **NOTE:**   
>When you delete a DB instance, its automated backups are also deleted but its manual backups are retained.  

## Method 1<a name="section5642991212401"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, locate an available DB instance and click  **Create Backup**  or choose  **More**  \>  **Create Backup**.
3.  In the displayed dialog box, specify  **Backup Name**  and  **Description**  and click  **OK**.
    -   The manual backup name can be 4 to 64 characters long. It must start with a letter and can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description contains a maximum of 256 characters and cannot contain the carriage return character and the following special characters: \>!<"&'=

4.  Check the result:
    -   During the creation of a manual backup, you can query the backup status on the  **Backup Management**  or the  **Backups & Restorations**  page. The backup status is  **Backing up**. The time it takes to complete the backup depends on the size of the job.
    -   If the manual backup is successfully created, the backup status is  **Complete**. The manual backup type is  **Manual**  and the backup method is  **Physical**.


## Method 2<a name="section40461508182024"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Backup Management**.
3.  On the  **Backup Management**  page, click  **Create Backup**.
4.  In the displayed dialog box, specify  **DB Instance Type**,  **DB Instance Name**,  **Backup Name**  and  **Description**  and click  **OK**.
    -   Only DB instances in  **Available**  status can be manually backed up.
    -   The manual backup name can be 4 to 64 characters long. It must start with a letter and can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description contains a maximum of 256 characters and cannot contain the carriage return character and the following special characters: \>!<"&'=

5.  Check the result:
    -   During the creation of a manual backup, you can query the backup status on the  **Backup Management**  or the  **Backups & Restorations**  page. The backup status is  **Backing up**. The time it takes to complete the backup depends on the size of the job.
    -   If the manual backup is successfully created, the backup status is  **Complete**. The manual backup type is  **Manual**  and the backup method is  **Physical**.


## Method 3<a name="section5636963115314"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click an available DB instance.
3.  In the navigation pane on the left, click  **Backups & Restorations**.
4.  On the  **Backups & Restorations**  page, click  **Create Backup**.
5.  In the displayed dialog box, specify  **Backup Name**  and  **Description**  and click  **OK**.
    -   The manual backup name can be 4 to 64 characters long. It must start with a letter and can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description contains a maximum of 256 characters and cannot contain the carriage return character and the following special characters: \>!<"&'=

6.  Check the result:
    -   During the creation of a manual backup, you can query the backup status on the  **Backup Management**  or the  **Backups & Restorations**  page. The backup status is  **Backing up**. The time it takes to complete the backup depends on the size of the job.
    -   If the manual backup is successfully created, the backup status is  **Complete**. The manual backup type is  **Manual**  and the backup method is  **Physical**.


